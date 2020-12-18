import socket

HOST= '127.0.0.1'
PORT = 12000

with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as server:
    server.bind((HOST,PORT))
    print(f"UDP Server Started on: {HOST}:{PORT}")
    data,addr= server.recvfrom(1024)
    print(f"Received Datagram from {addr}")
    with open(data,'r') as filename:
        try:
            filedata=filename.read()
            server.sendto(filedata.encode(),addr)
        except:
            print("no Such file")
            exit()



