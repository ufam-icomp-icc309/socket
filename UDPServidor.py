from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print('Servidor pronto para receber')
while 1:
    message, clientAddress = serverSocket.recvfrom(2048)
    print(message)
    print(clientAddress)
    modifiedMessage = message.upper()
    serverSocket.sendto(modifiedMessage, clientAddress)
