import socket
from colorama import Fore, Back
from colorama import init

init(autoreset=True)

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

#USER Input Data
client_nickname = None

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))



def ClientStart():
	global client_nickname
	print(Fore.BLUE + "-=====| WELCOME TO FINNDER CHAT! |=====-")

	client_nickname = input("Enter A Nickname: ")
	while True:
		send_user_message()

def send_user_message():
	user_message = input(f"=> ")
	send(f"{client_nickname}: " + user_message)


ClientStart()