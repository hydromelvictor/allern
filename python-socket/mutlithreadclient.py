import socket


multithreadclient = socket.socket()

host = '127.0.0.1'
port = 1233


try:
    multithreadclient.connect((host, port))
except socket.error as e:
    print(str(e))

resp = multithreadclient.recv(2048)
print(resp.decode('utf-8'))

while True:
    Input = input("Say something")
    multithreadclient.send(str.encode(Input))
    resp = multithreadclient.recv(1024)
    print(resp.decode('utf-8'))

multithreadclient.close()
