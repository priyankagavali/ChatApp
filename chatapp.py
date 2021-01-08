import socket 
import threading
print('\n\t\t\t...Welcome To Chat Application...\t\t\t\n')

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip=input("enter your ip: ")
port=1234
s.bind((ip,port))
server_ip=input("enter server ip: ")
server_port=9094
 
def send():
 while True:
     data=input("enter msg:")
     s.sendto(data.encode(),(server_ip,server_port))
     print("\n\t\t\t\t\t\t\tSent : " ,data)
     if data == "exit":
            os._exit(1)



def receive():
 while True: 
   data=s.recvfrom(1024)
   if data.decode() == "exit":
            os._exit(1)

   print('\n\t\t\t\t\t\t\tReceived : ' + data[0].decode())


thread1 = threading.Thread(target=send)
thread2 = threading.Thread(target=receive)
thread1.start()
thread2.start()









