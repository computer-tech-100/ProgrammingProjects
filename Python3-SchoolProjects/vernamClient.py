import socket
import sys
import operator

def vernamEncrypt(message):

#convert string to Ascii then to binary
 encoding= message.encode()
 w=int.from_bytes( encoding , 'big')
 encryptedMessage=bin(w)
 return encryptedMessage

myMessage = """Music!!! the one and only phenomena which many people living with.    Music is in every human's
    blood on the earth.   You can see little babies automatically dance when music is playing...  It is 
    inseparable part of human’s life & Without music do you think can we express ourselves???  
    In 2016 many music workshops appeared around the world,  there are lots of musical genres, Hip Hop is one of them. 
    1th of all,   Hip Hop is recently used to educate and socialize the young people & Hip Hop also is considered as a serious business $$$ ...!!!
    In the years 2015 and 2016 and 2017 hip hop dancing got popular among young people...   """
               
#frequency of charactors in plaintext
frequency={}
for j in myMessage:
   frequency[j]=frequency.setdefault(j, 0)+1

def sortDicbyVal():
 sortedBaseOnValue=sorted(frequency.items(),key=lambda t:t[1], reverse=True)
 print(sortedBaseOnValue) 
       
print('My original message is:'+myMessage)
print('Frequency of characters in descending order in plaintext is:')
sortDicbyVal()

data=vernamEncrypt(myMessage)
print('my encrypted message is:',data)

#frequency of charactors in plaintext
frequency2={}
for j in data:
   frequency2[j]=frequency2.setdefault(j, 0)+1

def sortDicbyVal2():
 sortedBaseOnValue2=sorted(frequency2.items(),key=lambda t:t[1], reverse=True)
 print(sortedBaseOnValue2) 

print('Frequency of characters in descending order in cipherText is:')
sortDicbyVal2()

#create socket 
myClientSocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
myClientSocket.connect(('127.0.0.1',1234)) 

data1=bytes(data,'utf-8')
myClientSocket.send(data1) 

message = myClientSocket.recv(1020)
print (message.decode('ascii'))
myClientSocket.close()
