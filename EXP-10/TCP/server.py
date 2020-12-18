from socket import *
import socket

HOST= '127.0.0.1'
PORT = 12000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f'Server Listening on {HOST}:{PORT}')
    conn, addr = s.accept()
    with conn:
        print('Connected by: ', addr)
        while True:
            data = conn.recv(1024).decode()
            if not data:
                break
            with open(data,'r') as filename:
                filedata=filename.read()
                print(filedata)
            conn.sendall(filedata.encode())
