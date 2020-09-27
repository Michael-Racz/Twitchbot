import cfg
import socket

server = socket.socket()
server.connect((cfg.HOST,cfg.PORT))

server.send(bytes('PASS ' + cfg.PASS + '\r\n', 'utf-8'))
server.send(bytes('NICK ' + cfg.NICK + '\r\n', 'utf-8'))
server.send(bytes('JOIN ' + cfg.CHAN + '\r\n', 'utf-8'))


print(server)

while True:
    print(server.recv(2048).decode('utf-8'))