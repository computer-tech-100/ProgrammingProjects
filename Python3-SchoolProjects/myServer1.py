#this is server that recieves encrypted message from client
#we should run server first then we run client afterwards

import socket
import sys
import math

the_key=8
key  = 'zyxwvutsrqponmlkjihgfedcba'

def decrypt(n, ciphertext):
    result = ''
    for l in ciphertext:
        try:
            i = (key.index(l) - n) % 26
            result += key[i]
        except ValueError:
            result += l
    return result

def decryptMessage(k, m):

    col = math.ceil(len(m) / k)
    myRows = k
    cells = (col* myRows) - len(m)
    backTo_original = [''] * col
    j = 0
    row = 0
    for i in m:
        backTo_original[j] += i
        j += 1
        if (j == col) or (j == col - 1 and row >= myRows - cells):
            j= 0
            row += 1
    return decrypt(5, ''.join(backTo_original))

host='127.0.0.1'
port=1234
server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)#we create socket
server_socket.bind((host,port)) #then we bind socket to ip address and port
server_socket.listen(10)
client,address=server_socket.accept()
print("connection from %s" % str(address))

while True:

  data = client.recv(2048) #buffer size
  msg = data.decode('UTF-8') # convert to string
  print( msg)
  decrypteMyMessage = decryptMessage(the_key,msg)
  print("The decrypted message is : {}".format(decrypteMyMessage))
  server_socket.close() #close the socket
