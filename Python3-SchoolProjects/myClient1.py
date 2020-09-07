import math
import socket
import sys
import operator

the_key=8

#we have 5 keys
key  = 'zyxwvutsrqponmlkjihgfedcba'
key2 = 'mjnkhoylgrfncdflmbwapolqpm'
key3 = 'nmbcxzvasdgfhkoiuyrewqaspo'
key4 = 'xcvbnmzaqwertyuioplkjhgfcd'
key5 = 'xvvnmlkhiuytredswqazxcvbgk'

myMessage = """Music!!! the one and only phenomena which many people are living with. Music is in every human's
    blood on the earth. You can see little babies automatically dance when music is playing...  It is 
    inseparable part of human’s life & Without music do you think can we express ourselves???  
    In 2016 many music workshops appeared around the world,  there are lots of musical genres, Hip Hop is one of them. 
    1th of all,Hip Hop is recently used to educate and socialize the young people & Hip Hop also is considered as a serious business $$$ ...!!!
    In the years 2015 and 2016 and 2017 hip hop dancing got popular among young people...   """

#substitution scheme
def encrypt(m, myPlaintext):
 
    output = ''
    for p in myPlaintext.lower():
        try:
            i = (key.index(p) + m) % 26
            output += key[i]
        except ValueError:
            output += p
    return output.lower()

#transposition scheme
def transpose(the_message, the_key):
   
    myCiphertext=['']*the_key
 
    for i in range(the_key):
        mypointer =i
            
        while mypointer < len(the_message):
            myCiphertext[i] += the_message[mypointer]
                  
            mypointer +=the_key
    #join it to see the result in form of string
    return ''.join(myCiphertext)

#count the number of frequencies of each charactor in plaintext
frequency={}
for j in myMessage:
   frequency[j]=frequency.setdefault(j, 0)+1

def sortDicbyVal():
 sortedBaseOnValue=sorted(frequency.items(),key=lambda t:t[1], reverse=True)
 print(sortedBaseOnValue) 

#Diffie Hellman Algorithm
#define two prime numbers
#p1 = 29
#p2 = 11

#mySecretKey = 8 #this is my secret number lets call it a
#yourSercertKey= 21 #this is your secret  number lets call it b

#print( " Prime p2 " , p1)
#print( " prime p2:  " , p2 )
# I Send you my public number which is M=p2^a mod p1
#M = (p2**mySecretKey) %p1
#print( "\n I send", M )

# You Send me your public number which is Y = p2^b mod p1
#Y = (p2** yourSercertKey) %p1
#print( "you send ", Y)
#print( " calculating shared key:" )
# I Compute: Y^a mod p1
#mySh_key = (Y ** mySecretKey) % p1
#print( " my Shared key: ", mySh_key )
# You Compute = M^b mod p1
#yourSh_key = (M**yourSercertKey) %p1
#print( " your Shared key: ", yourSh_key)

def main():
   
    print("My original message is: {}".format(myMessage))
    substitutedMessage = encrypt(5, myMessage)
    print("My substituted message is : {}".format(substitutedMessage))
    transposedMessage = transpose(substitutedMessage, the_key)
    print("Now we take our substituted message and transpose it so my transposed message is : {}".format(transposedMessage))
    #count the number of frequencies of each charactor in cipherText
    frequency2={}
    for j in transposedMessage:
     frequency2[j]=frequency2.setdefault(j, 0)+1

    def sortDicbyVal2():
     sortedBaseOnValue2=sorted(frequency2.items(),key=lambda t:t[1], reverse=True)
     print(sortedBaseOnValue2) 

    print('frequencies of charactors in descending order in plaintext is:')
    sortDicbyVal()
    print('frequencies of charactors in descending order in cipherText is:')
    sortDicbyVal2()
     
#create socket
    myClientSocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    myClientSocket.connect(('127.0.0.1',1234)) 

    #client encrypts the message by using substitution and then transposition schemes and send it to the sever
    #this data is encrypted first with substitution scheme and then transposition scheme
    data=bytes(transposedMessage,'utf-8')
  
    myClientSocket.send(data)
  
    message = myClientSocket.recv(1020)
    print (message.decode('ascii'))
    myClientSocket.close()

if __name__ == '__main__':
    main()
