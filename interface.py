# Instalar o import do customtkinter rodando o seguinte codigo no Prompt de Commando ou Terminal:
# pip install customtkinter
# Em seguida, rodar esse arquivo por inteiro

import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog, messagebox

def select_fasta_file():
    file_path = filedialog.askopenfilename(
        title="Selecione um arquivo .FASTA", filetypes=[("FASTA Files", "*.fasta"), ("All Files", "*.*")]
    )

    if file_path.endswith(".fasta"):
        entry_input.delete(0, ctk.END)
        entry_input.insert(0, file_path)
    else:
        messagebox.showerror("Erro", "Por favor, selecione um arquivo .FASTA válido.")

# Comecar montagem
def start_assembly():
    input_file = entry_input.get()
    
    if not input_file:
        messagebox.showerror("Erro", "Por favor, selecione um arquivo .FASTA.")
        return

    result_label.configure(text=f"Iniciando montagem...\nArquivo: {input_file}")

# Abrir a janela
app = ctk.CTk()
app.title("Montagem de Genoma Bacteriano")
app.geometry("700x450")
ctk.set_appearance_mode("dark")

# Titulo
title_label = ctk.CTkLabel(
    app, text="Montagem de Genoma Bacteriano",
    font=ctk.CTkFont(size=20, weight="bold")
)
title_label.pack(pady=20)

# Indicações
indications_title = ctk.CTkLabel(
    app, text="Indicações para Melhores Resultados:",
    font=ctk.CTkFont(size=14, weight="bold"), justify="left", anchor="w" 
)
indications_title.pack(pady=(10, 0))
indications_label = ctk.CTkLabel(
    app, text=("Realize a quantificação precisa do DNA para assegurar a concentração ideal.\n"
               "Utilize o Ligation Sequencing Kit da Oxford Nanopore para a geração de dados brutos de alta qualidade.\n"
               "Execute a montagem genômica em um computador com no mínimo 32 GB de memória RAM.\n"
               "Recomendamos o uso de Linux ou Windows com o WSL devidamente configurado."), 
    font=ctk.CTkFont(size=13), justify="left", wraplength=500
)
indications_label.pack(pady=10, padx=20)

# Input
input_frame = ctk.CTkFrame(app)
input_frame.pack(pady=20, padx=20)
entry_input = ctk.CTkEntry(input_frame, width=350)
entry_input.grid(row=0, column=0, padx=5, pady=10)

# Botões
browse_button = ctk.CTkButton(input_frame, text="Selecionar .FASTA", command=select_fasta_file)
browse_button.grid(row=0, column=1, padx=5, pady=10)
button_start = ctk.CTkButton(
    app, text="Iniciar Montagem", command=start_assembly, font=ctk.CTkFont(size=14), width=160, height=35
)
button_start.pack(pady=30)

# Result label (you missed this part, assuming you want to show the assembly result status)????????????????
result_label = ctk.CTkLabel(app, text="", font=ctk.CTkFont(size=14))
result_label.pack(pady=10)

# Rodar a aplicação
app.mainloop()
