from audioop import add
from email import message
from http import client
from pydoc import cli
from socket import *
address = '127.0.0.1'
port = 83
client = socket(AF_INET,SOCK_STREAM)
client.connect((address,port))
message = "GET test.txt"
while True:
    client.send(message.encode())
    reply = client.recv(2048).decode()
    print(reply)
    client.close()
    break
# term