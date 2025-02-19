import socket
import threading
from tkinter import *
import tkinter
from tkinter import simpledialog

class chat:
    def __init__(self):
        HOST1 = '127.0.0.1'
        PORT1 = 55555
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((HOST1, PORT1))  # Corrigido para HOST1 e PORT1
        login = Tk()
        login.withdraw()

        self.janela_carregada = False
        self.ativo = True

        self.nome = simpledialog.askstring('Nome', 'Digite seu nome!', parent=login)
        self.sala = simpledialog.askstring('sala', 'Digite o nome que deseja entrar!', parent=login)

        thread = threading.Thread(target=self.conecta)
        thread.start()  # Corrigido a digitação de 'start'
        self.janela()

    def janela(self):
        self.root = Tk()
        self.root.geometry("800x800")
        self.root.title('chat')

        self.caixa_texto = Text(self.root)
        self.caixa_texto.place(relx=0.05, rely=0.01, width=700, height=600)  # Corrigido 'heigth' para 'height'

        self.envia_mensagem = Entry(self.root)
        self.envia_mensagem.place(relx=0.05, rely=0.8, width=500, height=20)  # Corrigido 'heigth' para 'height'

        self.btn_enviar = Button(self.root, text='Enviar', command=self.enviarMensagem)
        self.btn_enviar.place(relx=0.7, rely=0.8, width=100, height=20)  # Corrigido 'heigth' para 'height'
        self.root.protocol("WM_DELETE_WINDOW", self.fechar)  # Corrigido a vírgula fora do método

        self.root.mainloop()

    def fechar(self):
        self.root.destroy()
        self.client.close()

    def conecta(self):  # Corrigido a indentação
        while True:
            recebido = self.client.recv(1024)  # Corrigido 'rev' para 'recv'
            if recebido == b'SALA':
                self.client.send(self.sala.encode())
                self.client.send(self.nome.encode())
            else:
                try:
                    self.caixa_texto.insert('end', recebido.decode())
                except:
                    pass

    def enviarMensagem(self):
        mensagem = self.envia_mensagem.get()
        self.client.send(mensagem.encode())

chat = chat()
