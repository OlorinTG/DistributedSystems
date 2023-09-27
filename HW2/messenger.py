import sys
import socket
import threading


run_as_server = False
server_address = ('localhost', 0)
conn = None
#check if command line arg was given
if len(sys.argv) >=2:
    arg1 = sys.argv[1]
    #check if arg is -l (run server mode)
    if arg1 == '-l':
        run_as_server = True
        if len(sys.argv) >=3:
            try:
                port_number = int(sys.argv[2])
                server_address = ('', port_number)
            except ValueError:
                print("Invalid port number. <port number> ")
                sys.exit(1)
    else:
        try:
            port_number = int (sys.argv[1])
            if len(sys.argv) >= 3:
                server_address = (sys.argv[2], port_number)
        except ValueError:
            print("Invalid port number. <port number> ")
            sys.exit(1)
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    if run_as_server:
        sock.bind(server_address)
        sock.listen(5)
        print(f"Listening on port {server_address[1]}...")
        conn, addr = sock.accept()
        print(f"Connection established with {addr}")
    else:
        sock.connect(server_address)
        print(f"Connected to {server_address[0]}:{server_address[1]}")

    def receive_messages():
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(data.decode('utf-8'))

    # Start a thread to receive messages from the other end
    receive_thread = threading.Thread(target=receive_messages)
    receive_thread.start()

    while True:
        message = input()
        conn.send(message.encode('utf-8'))

except KeyboardInterrupt:
    pass
finally:
    if conn is not None:
        conn.close()
    else:
        sock.close()