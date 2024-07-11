import socket
import threading

HOST1 = '127.0.0.1'
PORT1 = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST1, PORT1))  # Corrigido para HOST1 e PORT1
server.listen()


salas = {}

def broadcast(sala, mensagem):
    for i in salas[sala]:
        if isinstance(mensagem, str):
            mensagem = mensagem.encode()
        i.send(mensagem)  # Corrigido a indentação

def enviarMensagem(nome, sala, client):
    while True:
        mensagem = client.recv(1024)
        mensagem = f"{nome}: {mensagem.decode()}\n"
        broadcast(sala, mensagem)

while True:
    client, addr = server.accept()
    client.send(b'SALA')
    sala = client.recv(1024).decode()
    nome = client.recv(1024).decode()
    if sala not in salas.keys():
        salas[sala] = []
    salas[sala].append(client)
    print(f'{nome} se conectou na sala {sala}! INFO {addr}')
    # Lógica para lidar com o cliente no Servidor 1 (adicionar conforme necessário)
    # client.close()
    broadcast(sala, f'{nome}: Entrou na sala!\n')
    thread = threading.Thread(target=enviarMensagem, args=(nome, sala, client))
    thread.start()
