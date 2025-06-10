import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    message = input("Enter a message (type 'exit' to quit): ")
    if message.lower() == 'exit':
        break
    client_socket.sendto(message.encode(), ('localhost', 12000))
    modified_message, _ = client_socket.recvfrom(1024)
    print("From server:", modified_message.decode())

client_socket.close()