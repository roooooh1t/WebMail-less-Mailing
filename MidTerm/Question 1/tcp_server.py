import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12000))
server_socket.listen(1)
print("TCP server is ready to receive...")

conn, addr = server_socket.accept()
print(f"Connected by {addr}")

while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    print("Received from client:", data)
    modified_data = data.upper()
    conn.send(modified_data.encode())

conn.close()