import socket
import threading

host = socket.gethostbyname(socket.gethostname())
port = 5050
ADDR = (host,port)
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind(ADDR)

server.listen(1)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    while True:
        msg_length = conn.recv(1000).decode()
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode()
            if msg == "QUIT":
                break

            print(f"[{addr}]: {msg}")
            conn.send("Msg received".encode())

    conn.close()
        
print("starting...")

while True:
    conn, addr = server.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()

