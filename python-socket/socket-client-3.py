import socket


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 12345))

payload = "Hey Server"

try:
    while True:

        client.send(payload.encode('utf-8'))
        data = client.recv(1024)
        print(str(data))

        more = input("Want to more data to the server ?")
        if more.lower() == "y":
            payload = input("Enter payloa")
        else:
            break
except KeyboardInterrupt:
    print("Exited by User")

client.close()
