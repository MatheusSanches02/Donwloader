from pytube import YouTube
import tkinter as tk
from tkinter import simpledialog, messagebox

ROOT = tk.Tk()
ROOT.withdraw()

continuar = True

def input_data(title, prompt):
    result = simpledialog.askstring(title=title, prompt=prompt)
    return result

while continuar:
   
    opcao = input_data("Opção.", "Digite 1 para baixar ou 0 para sair: ")

    if opcao == "1":
        
        video_link = input_data("Video Link", "Insira o link do vídeo: ")

        if video_link != "":
            yt = YouTube(video_link)
            print(f'Título: {yt.title}')
            yd = yt.streams.get_highest_resolution()
            download_path = input_data("Download", "Insira o caminho do download: ")
            yd.download(download_path)
            messagebox.showinfo("Mensagem", f'Download concluido com sucesso em {download_path}')
        else:
            messagebox.showwarning("Mensagem", f'Por favor, insira um link válido')
            opcao = 1 
    elif opcao == "0":
        continuar = False
    else:
        messagebox.showerror("Erro", f'Opção Inválida')
        continuar = False