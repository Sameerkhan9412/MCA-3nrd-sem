import socket

client_socket = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)

while True:
    msg = input("You:")
    client_socket.sendto(msg.encode() , ("localhost" , 12345))