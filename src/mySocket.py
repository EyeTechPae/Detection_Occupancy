import socket

host = '127.0.0.1'
port = 5204
backlog = 5
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(backlog)
client, address = s.accept()#pilla 1 client
while 1:
    data = client.recv(size)#escolta al client
    if len(data) > 0:	#quan el client envia algo:
	print(data.decode())#mostra el missatge rebut pel client
        client.send(b"0011111111011111111111111111111111110111111\0")#envia string al client(HA  DE ACABAR EN \0)!!!




