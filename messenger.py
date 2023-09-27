import sys
import socket
import threading

def send_message(client_socket):
    try:
        while True:
            message = input()
            if not message:
                break
            client_socket.sendall(message.encode())
    except:
        pass
    finally:
        client_socket.shutdown(socket.SHUT_WR)

def receive_message(client_socket):
    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"\nReceived: {data.decode()}")
    except:
        pass
    finally:
        client_socket.close()
        sys.exit(0)

def server_mode(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', port))
    server_socket.listen(1)
    print("Server is listening...")
    client_socket, client_address = server_socket.accept()
    print(f"Connected with {client_address}")

    threading.Thread(target=send_message, args=(client_socket,)).start()
    receive_message(client_socket)

def client_mode(port, address='localhost'):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((address, port))
    print("Connected to the server.")

    threading.Thread(target=send_message, args=(client_socket,)).start()
    receive_message(client_socket)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python messenger.py [-l] <port number> [<server address>]")
        sys.exit(1)
    
    if sys.argv[1] == "-l":
        server_mode(int(sys.argv[2]))
    else:
        port = int(sys.argv[1])
        address = sys.argv[2] if len(sys.argv) > 2 else 'localhost'
        client_mode(port, address)
