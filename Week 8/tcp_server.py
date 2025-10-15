
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 12345))
server_socket.listen(1)

print("TCP server ready to receive file.")
conn, addr = server_socket.accept()
print(f"Connected by {addr}")

with open("received_file.txt", "wb") as f:
    while True:
        data = conn.recv(1024)
        if not data:
            break
        f.write(data)

print("File received successfully.")
conn.close()
