import cv2
import socket
import pickle
import struct
import sys

SERVER_IP = '127.0.0.1'  # localhost, since running on the same machine
PORT = 9999

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print(f"Connecting to server {SERVER_IP}:{PORT} ...")
    try:
        client_socket.connect((SERVER_IP, PORT))
    except Exception as e:
        print(f"Failed to connect: {e}")
        sys.exit(1)
    print("Connected to server!")

    data = b""
    payload_size = struct.calcsize("Q")
    print(f"Expected header size: {payload_size} bytes")

    try:
        while True:
            # Retrieve message size (header)
            while len(data) < payload_size:
                packet = client_socket.recv(4 * 1024)  # 4KB chunks
                if not packet:
                    print("Connection closed by server")
                    sys.exit(0)
                data += packet

            packed_msg_size = data[:payload_size]
            data = data[payload_size:]
            msg_size = struct.unpack("Q", packed_msg_size)[0]

            # Retrieve all data based on message size
            while len(data) < msg_size:
                data += client_socket.recv(4 * 1024)

            frame_data = data[:msg_size]
            data = data[msg_size:]

            # Deserialize frame
            frame = pickle.loads(frame_data)

            # Show frame in window
            cv2.imshow("🎥 Live Stream - Press 'q' to quit", frame)

            # Exit on pressing 'q'
            if cv2.waitKey(1) & 0xFF == ord('q'):
                print("Exiting...")
                break

    except Exception as e:
        print(f"Error: {e}")

    finally:
        client_socket.close()
        cv2.destroyAllWindows()
        print("Client closed")

if __name__ == "__main__":
    main()