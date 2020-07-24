import socket

#disconnect message
DISCONNECT_MESSAGE = "CONNECTION TERMINATED"
PORT = 8080
HEADER = 1024
#private IP not the public one. When deploy to cloud has to be harcoded.
SERVER = "127.0.0.1"
#address variable
ADDR = (SERVER, PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode('utf-8')
    msg_length = len(message)
    send_length = str(msg_length).encode('utf-8')
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode('utf-8'))

send("I am a client!")
send("Samara is a superhacker")
#send(DISCONNECT_MESSAGE)

