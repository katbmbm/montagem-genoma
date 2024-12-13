# Instalar o import do customtkinter rodando o seguinte codigo no Terminal:

# pip install customtkinter

# Em seguida, rodar esse arquivo por inteiro

import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog, messagebox
import time

def select_fasta_file():
    file_path = filedialog.askopenfilename(
        title="Selecione um arquivo FASTA", filetypes=[("FASTA DNA", "*.fna"), ("All Files", "*.*")]
    )

    if file_path.endswith(".fna"):
        entry_input.delete(0, ctk.END)
        entry_input.insert(0, file_path)
    else:
        messagebox.showerror("Erro", "Por favor, selecione um arquivo FASTA válido.")

def start_assembly():
    input_file = entry_input.get()
    
    if not input_file:
        messagebox.showerror("Erro", "Por favor, selecione um arquivo FASTA.")
        return

    # Disable the button
    button_start.configure(state="disabled", fg_color="gray")

    result_label.configure(text=f"Montagem em progresso\nArquivo: {input_file}")

    # Create and start the progress bar
    create_progress_bar()
    simulate_progress()

def create_progress_bar():
    progress_bar.pack(pady=10)
    percent_label.pack(pady=0)

def simulate_progress():
    total = 100
    progress = 0

    while progress <= total:
        if progress < 1:
            time.sleep(2)
        else:
            time.sleep(5) 

        progress_bar.set(progress / total)
        percent_label.configure(text=f"{progress}%")
        app.update_idletasks()
        progress += 1

    result_label.configure(text="Montagem concluída!\nRealize o download do genoma montado.")

# Abrir a janela
app = ctk.CTk()
app.title("Montagem de Genoma Bacteriano")
app.geometry("800x570")
ctk.set_appearance_mode("dark")

# Titulo
title_label = ctk.CTkLabel(
    app, text="Montagem de Genoma Bacteriano",
    font=ctk.CTkFont(size=23, weight="bold")
)
title_label.pack(pady=20)

# Indicações
indications_title = ctk.CTkLabel(
    app, text="Indicações para Melhores Resultados:",
    font=ctk.CTkFont(size=17, weight="bold"), justify="left", anchor="w" 
)
indications_title.pack(pady=(10, 0))
indications_label = ctk.CTkLabel(
    app, text=("Realize a quantificação precisa do DNA para assegurar a concentração ideal.\n"
               "Utilize o Ligation Sequencing Kit da Oxford Nanopore para a geração de dados brutos de alta qualidade.\n"
               "Execute a montagem genômica em um computador com no mínimo 32 GB de memória RAM.\n"
               "Recomendamos o uso de Linux ou Windows com o WSL devidamente configurado."), 
    font=ctk.CTkFont(size=15), justify="left", wraplength=550
)
indications_label.pack(pady=10, padx=20)

# Input
input_frame = ctk.CTkFrame(app)
input_frame.pack(pady=20, padx=20)
entry_input = ctk.CTkEntry(input_frame, width=370)
entry_input.grid(row=0, column=0, padx=5, pady=10)

# Botões
browse_button = ctk.CTkButton(input_frame, text="Selecionar .FASTA", command=select_fasta_file, font=ctk.CTkFont(size=13))
browse_button.grid(row=0, column=1, padx=5, pady=10)
button_start = ctk.CTkButton(
    app, text="Iniciar Montagem", command=start_assembly, font=ctk.CTkFont(size=14), width=160, height=35
)
button_start.pack(pady=30)

# Barra de progresso
progress_bar = ctk.CTkProgressBar(app, width=500)
progress_bar.set(0)
percent_label = ctk.CTkLabel(app, text="0%", font=ctk.CTkFont(size=14))
result_label = ctk.CTkLabel(app, text="", font=ctk.CTkFont(size=14))
result_label.pack(pady=5)

# Rodar a aplicação
app.mainloop()
