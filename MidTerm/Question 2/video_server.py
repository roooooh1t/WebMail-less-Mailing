import cv2
import socket
import pickle
import struct

HOST = '0.0.0.0'  
PORT = 9999

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)
print(f"Server listening on {HOST}:{PORT}")

conn, addr = server_socket.accept()
print(f"Client connected from: {addr}")

cam = cv2.VideoCapture(0)

try:
    while cam.isOpened():
        ret, frame = cam.read()
        if not ret:
            print("Failed to grab frame")
            break

        data = pickle.dumps(frame)
        message = struct.pack("Q", len(data)) + data
        conn.sendall(message)

except Exception as e:
    print(f"Server error: {e}")

finally:
    cam.release()
    conn.close()
    server_socket.close()
    print("Server closed")