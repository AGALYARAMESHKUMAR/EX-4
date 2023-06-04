# EX-4 IMPLEMENTATION OF ADDRESS RESOLUTION PROTOCOL (ARP)

# EXP: 4
# DATE:29-03-2023
# AIM:
To write a python program for implementing Address Resolution Protocol(ARP).

# ALGORITHM:
# Client:
Start the program
Using socket connection is established between client and server.
Get the IP address to be converted into MAC address.
Send this IP address to server.
Server returns the MAC address to client.
# Server:
Start the program
Accept the socket which is created by the client.
Server maintains the table in which IP and corresponding MAC addresses are stored.
Read the IP address which is send by the client.
Map the IP address with its MAC address and return the MAC address to client.
# PROGRAM:
# CLIENT:
```
import socket
s=socket.socket()
s.bind(('localhost',8000))
s.listen(5)
c,addr=s.accept()
address={"165.165.80.80":"6A:08:AA:C2","165.165.79.1":"8A:BC:E3:FA"};
while True:
  ip=c.recv(1024).decode()
try:
  c.send(address[ip].encode())
except KeyError:
  c.send("Not Found".encode())
  ```
# SERVER:
```
import socket
s=socket.socket()
s.connect(('localhost',8000))
while True:
   ip=input("Enter logical Address : ")
   s.send(ip.encode())
   print("MAC Address",s.recv(1024).decode())
   ```
# CLIENT OUTPUT :
![image](https://github.com/sujathamohankumar/EX-4/assets/119394395/37466a05-e044-4783-855d-8d2853cce73b)


# SERVER OUTPUT :
![image](https://github.com/sujathamohankumar/EX-4/assets/119394395/dfbf9617-0415-4976-b161-b6763609bbf9)


# RESULT:
Thus, the python program for simulating ARP protocols using TCP was successfully executed.
