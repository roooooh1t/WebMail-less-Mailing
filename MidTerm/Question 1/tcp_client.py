import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12000))

while True:
    message = input("Enter a message (type 'exit' to quit): ")
    if message.lower() == 'exit':
        break
    client_socket.send(message.encode())
    modified_message = client_socket.recv(1024).decode()
    print("From server:", modified_message)

client_socket.close()