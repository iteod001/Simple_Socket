import socket
import threading
import time

#DEFINING CONSTANTS

#HEADER OF THE MESSAGE - might need to be changed to bigger one
HEADER = 1024
#defining http port variable -> can be 5000, 8000 etc
PORT = 8080
#get ip automatically, or hardcode your public/internal IP
SERVER = socket.gethostbyname(socket.gethostname())
#address of the server
ADDR = (SERVER, PORT)
#disconnect message
DISCONNECT_MESSAGE = "CONNECTION TERMINATED"

#testingnext 2 lines
#print(SERVER)
#print(socket.gethostname())

#creating socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#binding with the socket tuple so everything will hit the socket
server.bind(ADDR)

#handling client

def handle_client(conn, addr):
    print(f"[INCOMING CONNECTION, NEW ASTEROID DISCOVERED! ADRESS:] {addr} connected.")

    connected = True
    while connected:
        #receiving message from teh client
        msg_length = conn.recv(HEADER).decode('utf-8')
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(HEADER).decode('utf-8')
            if msg == DISCONNECT_MESSAGE:
             connected = False
            # lookup what kind of message received
            print(f"[{addr}] {msg}")
            conn.send("Mesg received".encode('utf-8'))
    conn.close()


#method that starts the server
def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        #registering incoming connections
        conn, addr = server.accept()
        #starting thread for each connection and passing it with arguments to handle_client
        thread = threading.Thread(target = handle_client, args=(conn, addr))
        thread.start()
        #registering amount of connections
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1 }")


print ("Server is starting")

start()

