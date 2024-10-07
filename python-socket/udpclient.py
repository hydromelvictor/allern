import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
msg = "Hello UDP server"
client.sendto(msg.encode('utf-8'), ('127.0.0.1', 12345))

data, addr = client.recvfrom(4096)
print("Server Says")
print(str(data))
client.close()
