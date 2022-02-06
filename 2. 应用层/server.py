#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from socket import *

# servername = "127.0.0.1"
serverport = 9999
clientsocket = socket(AF_INET, SOCK_DGRAM)
clientsocket.bind(('',serverport))
print("The server is ready to send")
while True:
    data, address = clientsocket.recvfrom(2048)
    data1 = data.decode().upper()
    clientsocket.sendto(data1.encode(),address)
