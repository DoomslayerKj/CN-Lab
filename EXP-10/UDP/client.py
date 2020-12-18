import socket

HOST= '127.0.0.1'
PORT = 12000
filename=input("Enter File Name: ")
with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as client:
    client.sendto(filename.encode(),(HOST,PORT))
    reply=client.recvfrom(1024)

print("reply: ",reply)
