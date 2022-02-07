# import socket module
from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)
# Prepare a sever socket
# Fill in start
serverSocket.bind(("", 81))
serverSocket.listen(1)
# Fill in end
while True:
    # Establish the connection
    print("Ready to serve...")
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(2048)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        # Fill in start #Fill in end
        # Send one HTTP header line into socket
        # Fill in start
        outputdata = 'HTTP/1.1 200 OK\r\n connection: close \r\n\r\n' + outputdata
        # Fill in end
        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.close()
    except IOError:
        # Send response message for file not found
        # Fill in start
        outputdata = 'HTTP/1.1 404 Not Found\r\n\r\n'
        # Fill in end
        # Close client socket
        # Fill in start
        connectionSocket.send(outputdata.encode())
        break
    # Fill in end
serverSocket.close()
