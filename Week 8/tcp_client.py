
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("localhost", 12345))

with open("test.txt", "rb") as f:
    data = f.read(1024)
    while data:
        client_socket.send(data)
        data = f.read(1024)

print("File sent successfully.")
client_socket.close()
