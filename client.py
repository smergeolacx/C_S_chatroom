import socket

host = "192.168.0.190"              #"203.191.62.198"
port = 5050
ADDR = (host,port)
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect(ADDR)

message = input("=> ")

while message != 'QUIT':
        client.send(message.encode())
        data = client.recv(1024).decode()
        print ('Received from server: ' + data)
        message = input("=> ")
         
client.close()