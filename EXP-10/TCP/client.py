
from socket import *
serverName = '127.0.0.1'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

sentence = input("Enter file name: ")
clientSocket.send(sentence.encode())
filecontents = clientSocket.recv(1024).decode()
print ('From Server:', filecontents)

clientSocket.close()

# HOST='127.0.0.1'
# PORT=1234
# filename='test.txt'
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
#     client.connect((HOST,PORT))
#     client.send(filename.encode())
#     data=client.recv(1024).decode()
#
# print(f'Recieved data from Server: {data}')