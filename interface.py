# Instalar o import do customtkinter rodando os seguintes comandos no Terminal:

# pip install customtkinter
# pip install tqdm
# pip install requests

# Em seguida, rodar esse arquivo por inteiro

# Import required libraries
import customtkinter as ctk
import tkinter as tk
from tkinter import filedialog, messagebox
import time
from tqdm import tqdm
import requests
import os
import sys
import zipfile
import shutil
import subprocess


def select_fasta_file():
    """Opens a file dialog to select a .fna file"""
    file_path = filedialog.askopenfilename(
        title="Selecione um arquivo FASTA", filetypes=[("FASTA DNA", "*.fna"), ("All Files", "*.*")]
    )

    if file_path.endswith(".fna"):
        entry_input.delete(0, ctk.END)
        entry_input.insert(0, file_path)
    else:
        messagebox.showerror("Erro", "Por favor, selecione um arquivo FASTA válido.")


def download_newest_version():
    """Handles the download logic and updates GUI"""
    chunk_size = 1024
    url = "https://raw.githubusercontent.com/katbmbm/montagem-genoma/main/instalacao.sh"
    try:
        result_label.configure(text="Iniciando download do script...")
        button_download.pack_forget()


        # Simulate download progress
        with requests.get(url, stream=True) as r:
            total_size = int(r.headers['content-length'])
            with open('instalacao.sh', 'wb') as f:
                for data in tqdm(iterable=r.iter_content(chunk_size=chunk_size), total=total_size / chunk_size, unit='KB'):
                    f.write(data)
                    app.update_idletasks()
        
        # Wait 5 seconds before showing completion
        time.sleep(5)

        result_label.configure(text="Download Concluído com Sucesso.")
        
    except Exception as e:
        result_label.configure(text=f"Erro no download: {e}")


def start_assembly():
    """Starts assembly and begins simulation"""
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
    """Display the progress bar"""
    progress_bar.pack(pady=10)
    percent_label.pack(pady=0)


def simulate_progress():
    """Simulates progress and enables the download button at 100%."""
    total = 100
    progress = 0

    while progress <= total:
        if progress < 1:
            time.sleep(2)
        else:
            time.sleep(0.05)  # Simulate quick progress after reaching a point

        progress_bar.set(progress / total)
        percent_label.configure(text=f"{progress}%")
        app.update_idletasks()
        progress += 1

        if progress == 100:  # Trigger showing the download button
            show_download_button()


def show_download_button():
    """Show the download button only when the progress bar is full"""
    if not button_download.winfo_ismapped():  # Check if it's already visible
        button_download.pack(pady=10)
        button_download.configure(state="normal", fg_color="#2E8B57")  # Set color same as other buttons
        result_label.configure(text="Montagem concluída! Clique para fazer o download.")


# Main application window
app = ctk.CTk()
app.title("Montagem de Genoma Bacteriano")
app.geometry("800x580")
ctk.set_appearance_mode("dark")

# Title label
title_label = ctk.CTkLabel(
    app, text="Montagem de Genoma Bacteriano",
    font=ctk.CTkFont(size=23, weight="bold")
)
title_label.pack(pady=20)

# Indications section
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

# Input section
input_frame = ctk.CTkFrame(app)
input_frame.pack(pady=20, padx=20)
entry_input = ctk.CTkEntry(input_frame, width=370)
entry_input.grid(row=0, column=0, padx=5, pady=10)

# Buttons
browse_button = ctk.CTkButton(input_frame, text="Selecionar .FASTA", command=select_fasta_file, font=ctk.CTkFont(size=13))
browse_button.grid(row=0, column=1, padx=5, pady=10)

button_start = ctk.CTkButton(
    app, text="Iniciar Montagem", command=start_assembly, font=ctk.CTkFont(size=14), width=160, height=35
)
button_start.pack(pady=30)

button_download = ctk.CTkButton(
    app, text="Download Script", command=download_newest_version, font=ctk.CTkFont(size=14), width=160, height=35,
    state="disabled"
)

# Progress bar & UI elements
progress_bar = ctk.CTkProgressBar(app, width=500)
progress_bar.set(0)
percent_label = ctk.CTkLabel(app, text="0%", font=ctk.CTkFont(size=14))
result_label = ctk.CTkLabel(app, text="", font=ctk.CTkFont(size=14))
result_label.pack(pady=5)

# Run the application
app.mainloop()
