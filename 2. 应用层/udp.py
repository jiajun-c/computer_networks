#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from socket import *

servername = "127.0.0.1"
serverport = 9999
clientsocket = socket(AF_INET, SOCK_DGRAM)

while True:
    message = input("What do you wants to say\n")
    clientsocket.sendto(message.encode(), (servername, serverport))
    modify, address = clientsocket.recvfrom(2048)
    print(modify.decode())
