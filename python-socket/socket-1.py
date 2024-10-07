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
