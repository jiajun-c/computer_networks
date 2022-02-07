from socket import *
import time
serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
Min = 1.1
Max = 0.0
sum = 0
get = 0
for i in range(10):
    start = time.time()
    message = "Ping hello YL " + str(i) + str(start)
    # 设置超时 单位秒
    clientSocket.settimeout(1)
    clientSocket.sendto(message.encode(), (serverName, serverPort))
    try:
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        timeDiff = time.time() - start
        Max = max(Max,timeDiff)
        Min = min(Min,timeDiff)
        sum += timeDiff
        print(modifiedMessage.decode() + " RTT: " + str(timeDiff))
        get+=1
    except:
        print("lost " + str(i))

print("The package loss rate:{0}%".format((10-get)*10))
#print("The max:{}\n The min{}\n The average{}\n".format{Max,Min,float(sum/float(get))})
print("Max:{}\nMin:{}\nAverage{}".format(Max,Min,float(sum/float(get))))