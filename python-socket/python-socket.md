# Python Socket

Un socket est une interface de communication utilisée pour permettre l'échange de données entre deux programmes sur un réseau. Plus précisément, il sert à établir une connexion entre un client et un serveur, permettant à ces deux entités d'envoyer et de recevoir des informations.

## Définition

Socket : C'est un point d'extrémité pour une communication entre deux machines. Un socket se compose d'une adresse IP et d'un port, qui ensemble permettent d'identifier le destinataire ou l'expéditeur d'un flux de données.

## But

Échange de données : Les sockets permettent la communication bidirectionnelle entre deux processus via un réseau (comme l'Internet ou un réseau local).
Abstraction du réseau : Ils fournissent une interface standardisée, abstraite, qui simplifie l'utilisation des protocoles sous-jacents (comme TCP ou UDP).
Interopérabilité : Ils permettent à des applications différentes, tournant sur des systèmes différents, de communiquer entre elles en utilisant des protocoles réseaux.

### TCP

```python

# client.py

import socket
import sys


try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as e:
    print("Failed to create a socket")
    print("Reason " + str(e))
    sys.exit()

print("socket created")

host = input("enter the host name to connect: ")
port = input("enter the port: ")

try:
    sock.connect((host, int(port)))
    print(f"socket connected to {host}:{port}")
    sock.shutdown(2)
except socket.error as e:
    print(f"Failed to connected to {host}:{port}")
    print("Reason " + str(e))
    sys.exit()


# server.py

import socket


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 8001))
# nbre de connection possible
server.listen(5)

white True:
    print("server waiting...")
    cleint, addr = server.accept()
    print("client connected from", addr)
    
    while True:
        data = client.recv(1024)
        if not data or data.decode("utf-8") == "END":
            break

        print("received from client" + data.decode("utf-8"))

        try:
            client.send(bytes("Hey client", "utf-8"))
        except Exception as e:
            print("exit by user")

    client.close()

server.close()
```

### UDP

```python

# server

import socket


server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('127.0.0.1', 12345))

while True:
    data, addr = server.recvfrom(4096)
    print(str(data))
    message = bytes("Hello I'm UDP Server").encode('utf-8')
    server.sendto(message, addr)


# client

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
msg = "Hello UDP server"
client.sendto(msg.encode('utf-8'), ('127.0.0.1', 12345))

data, addr = client.recvfrom(4096)
print("Server Says")
print(str(data))
client.close()
```

### Mutti Thread

```python

# server
import socket
import _thread


multithreadserver = socket.socket()

host = '127.0.0.1'
port = 1233
threadCount = 0

try:
    multithreadserver.bind((host, port))
except socket.error as e:
    print(str(e))

print("waiting for connection")
multithreadserver.listen(5)


def clientThread(connection):
    connection.send(str.encode("welcome to the server"))

    while True:
        data = connection.recv(2048)
        reply = f"Hello I'm Server {data.encode('utf-8')}"

        if not data:
            break
        connection.sendall(str.encode(reply))

    connection.close()


while True:
    client, addr = multithreadserver.accept()
    print(f"connected to {addr[0]}{addr[1]}")
    _thread.start_new_thread((clientThread, (client,)))
    threadCount += 1
    print(f"TrheadNumber {threadCount}")

multithreadserver.close()


# client

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
```
