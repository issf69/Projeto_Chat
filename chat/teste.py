import socket

HOST1 = '127.0.0.1'
PORT1 = 55555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST1, PORT1))

mensagem = client.recv(1024)

if mensagem == b'SALA':
    client.send(b'games')
    client.send(b'Irene')

# Lógica para lidar com o cliente no Servidor 2 (adicionar conforme necessário)
# client.close()

#rodar servidor=

#cd chat
#python3 servidor.py

#cd chat
#python3 cliente.py
