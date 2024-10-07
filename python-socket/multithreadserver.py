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
        reply = f"Hello I'm Server {data.decode('utf-8')}"

        if not data:
            break
        connection.sendall(str.encode(reply))

    connection.close()


while True:
    client, addr = multithreadserver.accept()
    print(f"connected to {addr[0]}{addr[1]}")
    _thread.start_new_thread(clientThread, (client,))
    threadCount += 1
    print(f"TrheadNumber {threadCount}")

multithreadserver.close()
