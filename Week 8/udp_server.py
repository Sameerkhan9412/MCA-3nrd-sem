import socket

server_socket = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
server_socket.bind(("localhost" , 12345))

print("Server started to receive messages")

while True:
    message , address = server_socket.recvfrom(1024)
    print(f"Received from {address} : {message.decode()}")