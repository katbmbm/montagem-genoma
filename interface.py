# Instalar os imports necessários, rodando os seguintes comandos no Terminal:

# pip install customtkinter
# pip install tqdm
# pip install requests

# Em seguida, rodar esse arquivo por inteiro

import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog, messagebox
import time
from tqdm import tqdm
import requests
import subprocess

def selecionar_fasta():
    caminho_arq = filedialog.askopenfilename(
        title="Selecione um arquivo FASTA", filetypes=[("FASTA DNA", "*.fna"), ("All Files", "*.*")]
    )
    if caminho_arq.endswith(".fna"):
        entrada_arq.delete(0, ctk.END)
        entrada_arq.insert(0, caminho_arq)
    else:
        messagebox.showerror("Erro", "Por favor, selecione um arquivo FASTA válido.")

def atualizar_progresso(valor):
    barra_progresso.set(valor / 100)
    t_porcentagem.configure(text=f"{valor}%")
    aplicacao.update_idletasks()

def executar_montagem():
    arq_fasta = entrada_arq.get()
    if not arq_fasta:
        messagebox.showerror("Erro", "Por favor, selecione um arquivo FASTA.")
        return

    t_resultado.configure(text=f"Iniciando montagem para {arq_fasta}...")
    b_comecar.configure(state="disabled", fg_color="gray")

    try:
        for progresso in range(0, 101, 5):
            atualizar_progresso(progresso)
            time.sleep(1)
        comando_montagem = f"bash montagem.sh {arq_fasta}"
        subprocess.run(comando_montagem, shell=True, check=True)
        t_resultado.configure(text="Montagem concluída. Iniciando análise de variantes...")
        for progresso in range(50, 101, 5):
            atualizar_progresso(progresso)
            time.sleep(1)
        comando_var = f"bash var_medaka.sh {arq_fasta}"
        subprocess.run(comando_var, shell=True, check=True)
        atualizar_progresso(100)
        t_resultado.configure(text="Montagem e análise de variantes concluídas com sucesso.")
    except subprocess.CalledProcessError as e:
        t_resultado.configure(text=f"Erro durante o processo: {e}")
    finally:
        b_comecar.configure(state="normal", fg_color="#2E8B57")

def baixar_genoma():
    x = 1024
    endereco = "https://raw.githubusercontent.com/katbmbm/montagem-genoma/main/instalacao.sh"
    try:    
        t_resultado.configure(text="Iniciando download do genoma montado...")
        b_baixar.pack_forget()
        with requests.get(endereco, stream=True) as resposta:
            tamanho_total = int(resposta.headers['content-length'])
            with open('instalacao.sh', 'wb') as arq:
                for pedaco in tqdm(iterable=resposta.iter_content(chunk_size=x), total=tamanho_total / x, unit='KB'):
                    arq.write(pedaco)
                    aplicacao.update_idletasks()
        time.sleep(1)
        t_resultado.configure(text="Download Concluído com Sucesso.")
            
    except Exception as erro:
        t_resultado.configure(text=f"Erro no download: {erro}")

def comecar_montagem():
    executar_montagem()
    arq_fasta = entrada_arq.get()
    if not arq_fasta:
        messagebox.showerror("Erro", "Por favor, selecione um arquivo FASTA.")
        x=0
        return
    b_comecar.configure(state="disabled", fg_color="gray")
    x = range(progresso)
    t_resultado.configure(text=f"Montagem em progresso\nArquivo: {arq_fasta}")
    barra_estatico()
    barra_dinamico()

def barra_estatico():
    barra_progresso.pack(pady=10)
    t_porcentagem.pack(pady=0)

def barra_dinamico():
    total = 100
    progresso = 0
    while progresso <= total:
        if progresso < 1:
            time.sleep(3)
        else:
            time.sleep(10)
        atualizar_progresso(progresso)
        barra_progresso.set(progresso / total)
        t_porcentagem.configure(text=f"{progresso}%")
        aplicacao.update_idletasks()
        if progresso == 100:
            mostrar_b_baixar()

def mostrar_b_baixar():
    if not b_baixar.winfo_ismapped():
        b_baixar.pack(pady=10)
        b_baixar.configure(state="normal", fg_color="#2E8B57")
        t_resultado.configure(text="Montagem concluída! Clique para fazer o download.")

aplicacao = ctk.CTk()
aplicacao.title("Montagem de Genoma Bacteriano")
aplicacao.geometry("800x580")
ctk.set_appearance_mode("dark")

t_titulo = ctk.CTkLabel(
    aplicacao, text="Montagem de Genoma Bacteriano",
    font=ctk.CTkFont(size=23, weight="bold")
)
t_titulo.pack(pady=20)

titulo_indicacoes = ctk.CTkLabel(
    aplicacao, text="Indicações para Melhores Resultados:",
    font=ctk.CTkFont(size=17, weight="bold"), justify="left", anchor="w"
)
titulo_indicacoes.pack(pady=(10, 0))
t_indicacoes = ctk.CTkLabel(
    aplicacao, text=("Realize a quantificação precisa do DNA para assegurar a concentração ideal.\n"
               "Utilize o Ligation Sequencing Kit da Oxford Nanopore para a geração de dados brutos de alta qualidade.\n"
               "Execute a montagem genômica em um computador com no mínimo 32 GB de memória RAM.\n"
               "Recomendamos o uso de Linux ou Windows com o WSL devidamente configurado."), 
    font=ctk.CTkFont(size=15), justify="left", wraplength=550
)
t_indicacoes.pack(pady=10, padx=20)

quadro_entrada = ctk.CTkFrame(aplicacao)
quadro_entrada.pack(pady=20, padx=20)
entrada_arq = ctk.CTkEntry(quadro_entrada, width=370)
entrada_arq.grid(row=0, column=0, padx=5, pady=10)

b_procurar = ctk.CTkButton(quadro_entrada, text="Selecionar .FASTA", command=selecionar_fasta, font=ctk.CTkFont(size=13))
b_procurar.grid(row=0, column=1, padx=5, pady=10)

b_comecar = ctk.CTkButton(
    aplicacao, text="Iniciar Montagem", command=comecar_montagem, font=ctk.CTkFont(size=14), width=160, height=35
)
b_comecar.pack(pady=30)

b_baixar = ctk.CTkButton(
    aplicacao, text="Baixar Genoma", command=baixar_genoma, font=ctk.CTkFont(size=14), width=160, height=35,
    state="disabled"
)

barra_progresso = ctk.CTkProgressBar(aplicacao, width=500)
barra_progresso.set(0)
t_porcentagem = ctk.CTkLabel(aplicacao, text="0%", font=ctk.CTkFont(size=14))
t_resultado = ctk.CTkLabel(aplicacao, text="", font=ctk.CTkFont(size=14))
t_resultado.pack(pady=5)

aplicacao.mainloop()
