#this is server that recieves encrypted message from client and decrypts it
#we should run server first then we run client afterwards

import socket
import sys

def vernamDecrypt(myBinary):

 #convert binary to Ascii then to string
 n=int(myBinary, 2)
 a=(n.bit_length() + 7) // 8
 toBytes=n.to_bytes(a,'big')
 decrpytedMessage=toBytes.decode()
 return decrpytedMessage


# def vernamDecrypt(myBinary, encoding='utf-8', errors='surrogatepass'):
#     n = int(myBinary, 2)
#     return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'


host='127.0.0.1'
port=1234
server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)#we create socket
server_socket.bind((host,port)) #then we bind socket to ip address and port
server_socket.listen(10)
client,address=server_socket.accept()
print("connection from %s" % str(address))

while True:

  data = client.recv(8048) #buffer size 2048
  msg = data.decode('UTF-8') # convert to string
  print( msg)
  decryptedBinary=vernamDecrypt(msg)
  print("The decrypted message is:", decryptedBinary)
  server_socket.close() 
