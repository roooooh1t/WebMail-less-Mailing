import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 12000))
print("UDP server is ready to receive...")

while True:
    data, client_addr = server_socket.recvfrom(1024)
    print("Received from client:", data.decode())
    modified_data = data.decode().upper()
    server_socket.sendto(modified_data.encode(), client_addr)