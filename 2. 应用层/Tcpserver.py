from socket import *

sewrverport = 9999
server = socket(AF_INET, SOCK_STREAM)
server.bind(('', sewrverport))
server.listen(50)
print("Ready to receive")
while True:
    connect, address = server.accept()
    sentence = connect.recv(1024).decode()
    get = sentence.upper()
    connect.send(get.encode())
    connect.close()
