import socket
s=socket.socket()
s.connect(("localhost", 8000))
while True:
    ip=input("Enter the logical address:")
     
    s.send(ip.encode())
    print("Mac Address",s.recv(1024).decode())


