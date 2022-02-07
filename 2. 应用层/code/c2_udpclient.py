# from email import message
# from http import client, server
# from pydoc import cli
# from socket import *
# import time
# servername = "127.0.0.1"
# serverport = 12000
# client = socket(AF_INET,SOCK_DGRAM)
# for i in range(10):
#     start = time.time()
#     message = "Ping hello YL " + str(i) + str(start)
#     client.settimeout(1)
#     client.sendto(message.encode(),(servername,serverport))
#     try:
#         reply,address = client.recv(2048)
#         t = time.time() - start
#         print(reply.decode() + "RTT:" + str(t))
#     except:
#         print("Package lose: " + str(i))
# UDPPingerClient.py
from socket import *
import time
serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
for i in range(10):
    start = time.time()
    message = "Ping hello YL " + str(i) + str(start)
    # 设置超时 单位秒
    clientSocket.settimeout(1)
    clientSocket.sendto(message.encode(), (serverName, serverPort))
    try:
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        timeDiff = time.time() - start
        print(modifiedMessage.decode() + " RTT: " + str(timeDiff))
    except:
        print("lost " + str(i))
