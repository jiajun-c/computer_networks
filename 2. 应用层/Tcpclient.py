from socket import *

servername = "127.0.0.1"
serverport = 9999
client = socket(AF_INET, SOCK_STREAM)
client.connect((servername, serverport))
while True:
    message = input("Please input the sentence")
    client.send(message.encode())
    reply = client.recv(1024).decode()
    print("From server: ", reply)
  #  client.close()

