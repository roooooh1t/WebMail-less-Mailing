from socket import *
import threading

# SERVER DETAILS
my_server_ip = '172.24.244.183'
my_server_port = 7777

# CREATE SOCKET AND BIND TO SERVER ADDRESS
my_server_socket = socket(AF_INET, SOCK_DGRAM)
my_server_address = (my_server_ip, my_server_port)
my_server_socket.bind(my_server_address)

# FUNCTION TO RECEIVE MESSAGES FROM CLIENT
def receive_messages(server_socket):
    while True:
        # RECEIVE MESSAGE AND DECODE
        message, client_addr = server_socket.recvfrom(1024)
        decoded_message = message.decode()
        print(f"Received message from {client_addr}: {decoded_message}")

# FUNCTION TO SEND MESSAGES TO CLIENT
def send_messages(server_socket, client_address):
    while True:
        # GET USER INPUT AND ENCODE MESSAGE
        user_input = input("Enter message to send: ")
        encoded_message = user_input.encode()
        server_socket.sendto(encoded_message, client_address)

# PRINTING SERVER DETAILS
print(f"My server is listening on IP: {my_server_ip} and Port: {my_server_port}")

# GET CLIENT DETAILS FROM USER
client_ip = input("Enter client's IP address: ")
client_port = int(input("Enter client's port: "))
client_address = (client_ip, client_port)

# CREATE THREADS FOR RECEIVING AND SENDING MESSAGES
receive_thread = threading.Thread(target=receive_messages, args=(my_server_socket,), daemon=True)
send_thread = threading.Thread(target=send_messages, args=(my_server_socket, client_address), daemon=True)

# START THE THREADS
receive_thread.start()
send_thread.start()

# CLOSE THE SERVER SOCKET
my_server_socket.close()
