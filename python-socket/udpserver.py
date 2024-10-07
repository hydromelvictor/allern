import socket


server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('127.0.0.1', 12345))

while True:
    data, addr = server.recvfrom(4096)
    print(str(data))

    message = "Hello I'm UDP Server".encode('utf-8')
    server.sendto(message, addr)
