from pytube import YouTube
import tkinter as tk
from tkinter import simpledialog, messagebox
from tqdm import tqdm
import time

ROOT = tk.Tk()
ROOT.withdraw()

continuar = True

while continuar:

    print("Digite 1 para baixar um video ou 0 para sair")

    opcao = int(input("Opção: "))

    if opcao == 1:

        def input_data(title, prompt):
            result = simpledialog.askstring(title=title, prompt=prompt)
            return result

        video_link = input_data("Video Link", "Insira o link do vídeo: ")

        yt = YouTube(video_link)

        print(f'Título: {yt.title}')

        yd = yt.streams.get_highest_resolution()

        download_path = input_data("Download", "Insira o caminho do download: ")

        yd.download(download_path)


        messagebox.showinfo("Mensagem", f'Download concluido com sucesso em {download_path}')
    elif opcao == 0:
        continuar = False
    else:
        print("opcao invalida!")
        continuar = False