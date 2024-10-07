import socket


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 12345))
# nbre de connection possible
server.listen(5)

while True:
    print("server waiting...")
    client, addr = server.accept()
    print("client connected from", addr)

    while True:
        data = client.recv(1024)
        if not data or data.decode("utf-8") == "END":
            break

        print("received from client" + data.decode("utf-8"))

        try:
            client.send(bytes("Hey client", "utf-8"))
        except Exception:
            print("exit by user")

    client.close()

server.close()
