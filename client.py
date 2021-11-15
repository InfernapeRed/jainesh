import socket
HEADER=1024
FORMAT='utf-8'
DISCONNECT_MESSAGE='!DISCONNECT'
SERVER=input("Enter server IP:")
PORT=int(input("Enter port:"))
ADDR=(SERVER,PORT)

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)
print(client.recv(HEADER).decode(FORMAT))
def send(msg):
    message=msg.encode(FORMAT)
    client.send(message)
    return msg
connected=True

while connected:
    sent_msg=send(input("> "))
    if sent_msg:
        if sent_msg==DISCONNECT_MESSAGE:
            print("you are disconnecting...\n DISCONNECTED")
            connected=False
            break
        

