#Rock,Paper,Scissors Game
 import random
 import os
 import sys

 print("++++++++++++++++++++++++++++++++++++++++++")
 print("|   Welcome to Rock,Paper,Scissors Game  |")
 print("|         Each game is 10 rounds         |")
 print("++++++++++++++++++++++++++++++++++++++++++")

 choices=["rock","paper","scissors"]
 human_score=0
 computer_score=0

 for i in range(3):
     human_turn = input(str("It is your turn,enter your choice (rock,paper,scissors): "))

     computer_turn = random.choice(choices)
     if human_turn == "rock" and computer_turn == "rock":
         print("Computer Choice is:",computer_turn)
         print("Tie is reached!")


     elif human_turn == "rock" and computer_turn == "paper":
         print("Computer Choice is:", computer_turn)
         print("Computer Won!")
         computer_score+=1

     elif human_turn == "paper" and computer_turn == "rock":
         print("Computer Choice is:", computer_turn)
         print("You Won YaaY!")
         human_score+=1

     elif human_turn == "rock" and computer_turn == "scissors":
         print("Computer Choice is:", computer_turn)
         print("You Won YaaY!")
         human_score+=1

     elif human_turn == "scissors" and computer_turn == "rock":
         print("Computer Choice is:", computer_turn)
         print("Computer won!")
         computer_score+=1

     elif human_turn == "scissors" and computer_turn == "scissors":
         print("Computer Choice is:", computer_turn)
         print("Tie is reached!")

     elif human_turn == "scissors" and computer_turn == "paper":
         print("Computer Choice is:", computer_turn)
         print("You Won Yaay!")
         human_score+=1

     elif human_turn == "paper" and computer_turn == "scissors":
         print("Computer Choice is:", computer_turn)
         print("Computer Won!")
         computer_score+=1

     elif human_turn == "paper" and computer_turn == "paper":
         print("Computer Choice is:", computer_turn)
         print("Tie is reached!")

 print("++++++++++++++++ Result of the Game ++++++++++++++")
 print("Computer score is ",computer_score)

 print("Your score is ",human_score)

 if computer_score>human_score:
     print("Computer is winner of the game!")

 elif computer_score==human_score:
     print("Tie...No Winner!")

 else:
     print("You are winner of the game!")

 print("++++++++++++++++++++++++++++++++++++++++++++++++++")

 answer=input(str("Do you want to play again?(yes/no):"))

 if answer=="yes":
     mySystem=sys.executable
     x=os.path.abspath(__file__)
     os.execl(mySystem, x, *sys.argv)

 else:
     sys.exit()

#-----------------------------------------
#Write one function to retrieve all unique substrings that start and end with a vowel
#Write another function to retrieve all unique substrings that start and end with a consonant
#The result should be sorted array and has unique values
#The word itself is a substring

def vowel_substrings(string):

    vowels=['a','i','o','u','e']
    vowelSubStrings=[]

    allSubStrings=[]
    for i in range(len(string)):
        for j in range(i+1,len(string)+1):
            allSubStrings.append(string[i:j])

    for i in allSubStrings:

        if i in vowels:

            vowelSubStrings.append(i)

        elif len(i)>1:
            if i[0] in vowels and i[len(i)-1] in vowels:
                vowelSubStrings.append(i)

    vowelSubStrings.sort()

    print(vowelSubStrings)

def consonant_substrings(s):
    vowels = ['a', 'i', 'o', 'u', 'e']
    constantSubStrings = []

    allSubStrings = []
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            allSubStrings.append(s[i:j])

    for i in allSubStrings:

        if len(i)==1 and i not in vowels:

            constantSubStrings.append(i)

        elif len(i) > 1:
            if i[0] not in vowels and i[len(i) - 1] not in vowels:
                constantSubStrings.append(i)

    constantSubStrings.sort()
    print(constantSubStrings)

vowel_substrings("computer")
['e', 'o', 'ompu', 'ompute', 'u', 'ute']

vowel_substrings("apple")
 ["a", "apple", "e"]

vowel_substrings("bcdf")
 []

consonant_substrings("science")
['c', 'c', 'cien', 'cienc', 'n', 'nc', 's', 'sc', 'scien', 'scienc']

consonant_substrings("dogs")
['d', 'dog', 'dogs', 'g', 'gs', 's']

consonant_substrings("table")
['b', 'bl', 'l', 't', 'tab', 'tabl']

#-----------------------------------------
#Given a string of digits, return the longest odd substring with alternating odd/even digits
#The minimum alternating substring size is 2

def odd_longest_substring(str):

    allSubStrings = []
    for i in range(len(str)):
        for j in range(i + 1, len(str) + 1):
            allSubStrings.append(str[i:j])
    a=[]


    for i in allSubStrings:
        if len(i)>=2:
            a.append(i)

    odd_even=[]
    odd_even2=[]
    odd_even3=[]

    for num in a:
        for inx in range(len(num)):
            if inx%2==0:
                if int(num[inx])%2!=0:
                    odd_even.append([num, True])
            elif inx%2!=0:
                 if int(num[inx]) % 2 == 0:
                    odd_even.append([num,True])
                 else:
                     odd_even.append([num ,False])

    for i in odd_even:
        if i[1]==True:

            odd_even2.append(i)

    for i in odd_even2:

        length=len(i[0])
        if odd_even2.count(i)==int(length):
            odd_even3.append(i[0])

    l=[]
    lengths=[]
    for i in odd_even3:
        l.append([i,len(i)])

    x=0

    for i in l:
        if i[1]>x:
            x=i[1]
            lengths.clear()
            lengths.append(i) #largest length

    print(lengths)
    print("all substrings with alternating odd/even digits: ", odd_even3)
    print("longest substring with alternating odd/even or even/odd digits:",lengths[0][0],"with length",lengths[0][1])

odd_longest_substring("225424272163254474441338664823") # 72163254 with length 8

odd_longest_substring("594127169973391692147228678476") # 16921472 with length 8

odd_longest_substring("721449827599186159274227324466") # 7214 with length 4

#-----------------------------------------
#Given a string of digits, return the longest even substring with alternating even/odd digits
#The minimum alternating substring size is 2

def even_longest_substring(str):
    allSubStrings = []
    for i in range(len(str)):
        for j in range(i + 1, len(str) + 1):
            allSubStrings.append(str[i:j])
    a = []
    
    for i in allSubStrings:
        if len(i) >= 2:
            a.append(i)

    even_odd = []
    even_odd2 = []
    even_odd3 = []

    for num in a:
        for inx in range(len(num)):
            if inx % 2 == 0:
                if int(num[inx]) % 2 == 0:
                    even_odd.append([num, True])
            elif inx % 2 != 0:
                if int(num[inx]) % 2 != 0:
                    even_odd.append([num, True])
                else:
                    even_odd.append([num, False])

    for i in even_odd:
        if i[1] == True:
            even_odd2.append(i)

    for i in even_odd2:

        length = len(i[0])
        if even_odd2.count(i) == int(length):
            even_odd3.append(i[0])

    l = []
    lengths = []
    for i in even_odd3:
        l.append([i, len(i)])

    x = 0

    for i in l:
        if i[1] > x:
            x = i[1]
            lengths.clear()
            lengths.append(i)  # largest length

    print(lengths)
    print("all substrings with alternating even/odd digits: ", even_odd3)
    print("longest substring with alternating odd/even or even/odd digits:", lengths[0][0], "with length",
          lengths[0][1])

even_longest_substring("225424272163254474441338664823") #272163254 with length 9

even_longest_substring("594127169973391692147228678476") #6921472 with length 7

even_longest_substring("721449827599186159274227324466") #214 with length 3

#-----------------------------------------
#Write a function that takes a number and see if the digits are in ascending order
#If the digits are in ascending order then return True otherwise return false

def in_ascending_order(number):
    number=str(number)

    n1=[i for i in number]
    n2=[i for i in number]
    n2.sort()
    if n1==n2:
        return True
    else:
        return False

print(in_ascending_order(2869451))
print(in_ascending_order(24589))

#-----------------------------------------
#We have m lists (not more than 5)
#We want highest value such that:
#We pick only one element from each list square that element and add squares of chosen elements
#Then on that sum perform modulo by number n --> this gives a value
#The function should return max value that is produced by this process

import itertools
def highest_value(arrOfArr,n):

    a=[]
    s=[]
    all=[]
    squares=[]

    myArr= list(itertools.product(*arrOfArr))
    for i in myArr:
        x=[j*j for j in i]
        squares.append(x)


    for i in squares:
        s.append(sum(i))

    for i in s:
        all.append(i%n)

    #print(myArr)
    #print(squares)
    #print(s)
    #print(all)

    return max(all)

a=[ [5,6,4,2,7], [2,8,1,3,9] ,[3,8,1,0,2],[5,2,7,1,4] ]
print(highest_value(a,50))

#-----------------------------------------
#We want to find number of triple indices in an array such that the elements at those indices are in geometric progression for a given ratio
#Geometric progression : when a number is produced by multiplying the previous number by given ratio
#for example: 1 2 4 5 with given ratio 2 --> 2 at index 1 is result of multiplying 1 (which is at index 0) by given ratio 2
#or 4 is result of mutiplying 2( at index 1) by given ratio 2  hence the triple indices are (0,1,2) i.e number of triple indices is 1

def count_triple_indices(arr,ratio):

    a=[]
    inx=[]

    for i in range(len(arr)):
        for j in range(len(arr)):
            for k in range(len(arr)):
                if i<j<k and arr[i]*ratio==arr[j] and arr[j]*ratio==arr[k]:
                    a.append([arr[i],arr[j],arr[k]])
                    inx.append([i,j,k])

    print(a)
    print(len(a))
    print(inx)


count_triple_indices([1,4,16,64],4)  # (0,1,2) (1,2,3) i.e 2 triple indices

count_triple_indices([1, 2, 2, 4],2) # (0,1,3) (0,2,3) i.e 2 triple indices

count_triple_indices([1, 3, 9, 9,27,81],3) # (0,1,2)(0,1,3)(1,2,4)(1,3,4)(2,4,5)(3,4,5) i.e 6 triple indices

count_triple_indices([1,5, 5, 25,125],5) # (0,1,3)(0,2,3)(1,3,4)(2,3,4) i.e 4 triple indices

#-----------------------------------------
#Determine if two strings share a common substring
#For example, the words "car" and "cat" share the common substrings are c, ca, a
#The words "dog" and "apple" do not share a substring

def share_subString(str1,str2):

    subStrings1 = []
    subStrings2=[]
    shared=[]
    common_char=[]

    #common substrings (common substrings can be also a single character)
    for i in range(len(str1)):
        for j in range(i + 1, len(str1) + 1):
            subStrings1.append(str1[i:j])

    for i in range(len(str2)):
        for j in range(i+1,len(str2)+1):
            subStrings2.append(str2[i:j])

    for i in subStrings1:
        for j in subStrings2:
            if i==j:
                shared.append(i)

    #only common single chars
    for i in str1:
        for j in str2:
            if i==j:
                common_char.append(i)

    #print(subStrings1)
    #print(subStrings2)
    print("All substrings including single characters are:",shared)
    print("Common single characters are :",common_char)

share_subString("abcdefg","abc")
share_subString("car","cat")
share_subString("dog","apple")

#-----------------------------------------
#Create an empty array A
#There is an array Arr containing pairs... The element in Arr[i][0] is operation and Arr[i][1] is data
#When operation is 1 it means we insert data (which is at Arr[i][1]) into array A
#When operation is 2 it means we delete one occurrence of data (which is at Arr[i][1]) that is in array A
#when operation is 3 means it means we check if any integer is present in A whose frequency is exactly Arr[i][1]
#If yes print 1 otherwise print 0

def myFunction(Arr):
    A=[]
    for i in range(len(Arr)):

            if Arr[i][0]==1:
                A.append(Arr[i][1])
            elif Arr[i][0]==2:
                if Arr[i][1] in A:
                    A.remove(Arr[i][1])

            elif Arr[i][0]==3 :
                if A!=[]:
                    for j in A:
                        if A.count(j)==Arr[i][1]:
                            print(1)
                            break

                        else:
                            print(0)
                            break
                else:
                    print(0)

    print(A)

a=[(1,5),(1,6),(3,2),(1,10),(1,10),(1,6),(2,5),(3,2)] #output is 0 1
myFunction(a)
b=[(3,4),(2,1003),(1,16),(3,1)]#output is 0 1
myFunction(b)
c=[(1,3),(2,3),(3,2),(1,4),(1,5),(1,5),(1,4),(3,2),(2,4),(3,2)] #output is 0 1 1
myFunction(c)
d=[(1,1),(2,2),(3,2),(1,1),(1,1),(2,1),(3,2)] #output is 0 1
myFunction(d)

#-----------------------------------------
#Sort an array by swapping pair of numbers then print total number of swaps
#[2,4,1] --> perform 2 swaps to sort the array [1,2,4]
#[1,4,6,8] --> no swaps to sort array so print 0
#[2,1,3,1,2] --> total of 4 swaps to sort array i.e:
# 1 swap gives[1,2,3,1,2] --> 2 swaps gives[1,1,2,3,2] -->1 swap gives[1,1,2,2,3]

def sort_array(arr):

    count=0

    for i in range(len(arr)):
        for j in range(len(arr)):
            if i<j and arr[i]>arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                count+=1

    print("Total number of swaps is:",count)
    print("Sorted array is:", arr)

sort_array([2,4,1])# 2
sort_array([1,4,6,8])# 0
sort_array([2,1,3,1,2])# 4

#-----------------------------------------
#Jerry wants to maximize number of toys he buys with his money
#Given a list of prices and an amount to spend, what is the maximum number of toys Jerry can buy?
#prices=[1,2,3,4] if Jerry has 7 dollars to spend then he can buy [1,2,3] for 6 or [3,4] for 7
#Hence he chooses the group of three items

import itertools

def maximize_number_of_toys(prices, money):
    p = []
    toys = []
    s = []

    for i in range(len(prices) ):
        for j in itertools.combinations(prices, i+1):
            p.append(list(j))

    for i in p:
        if sum(i) == money:
            toys.append(i)
    for i in toys:
        s.append(len(i))

    print(toys)
    print(max(s))

maximize_number_of_toys([1,2,3,4],7)#3

maximize_number_of_toys([1,12,5,111,200,1000,10],28)#4

#-----------------------------------------
#String is valid if frequency of all chars are equal such as abc
#String is also valid if we remove only one char and remaining characters will occur the same number of times
#For example abcc is valid because if we remove c in index 3 then frequency of remaining characters remain the same

from collections import Counter
def valid_string(str):

    x=[i for i in str]
    new_str=''

    counter=[]
    counter2=[]
    for i in str:
        counter.append(str.count(i))

    if all(i == counter[0] for i in counter):
        return True
    else:
        for i in str:
            counter2.append([i,str.count(i)])

    for i in range(len(counter2)):
        for j in range(len(counter2)):
            if counter2[i][1]>counter2[j][1]:
                new_str = str[0:i] + str[i + 1:len(str)]
                break

    x=[new_str.count(i) for i in new_str]
    if all(i == x[0] for i in x):
        return True
    else:
        return False

print(valid_string("abc"))#True

print(valid_string("abccdd"))#False

print(valid_string("abcc"))#True

print(valid_string("aabbbbc"))#False

#-----------------------------------------
#child string can be formed from two parent strings
#The goal is to return max length of child string that can be formed from parent strings
#For example ABC with max length 3 is child string of "ARGDBKFC" and "WYAPLBTC"
#i.e common characters between parent strings while maintaining order

def lengthOfChidString(s1,s2):

    first_parent=[i for i in s1]
    second_parent=[i for i in s2]
    common=[]

    for i in first_parent:
        for j in second_parent:
            if i==j:
                common.append(i)

    child=[]
    c=[]

    for i in range(len(common)):
        for j in range(len(common)):
            if s1.index(common[i])<s1.index(common[j]) and s2.index(common[i])<s2.index(common[j]) and  common[i]:

                    child.append(common[i])
                    child.append(common[j])

    for i in child:
        if i not in c:
            c.append(i)

    print(len(c))


lengthOfChidString("Sally","Harry")# ay with length 2

lengthOfChidString("XX","YY")# 0

lengthOfChidString("WXYZ","WGBXOPYKZ")# WXYZ with length 4

lengthOfChidString("ABCDEF","FBDAMN")# BD with length 2

#-----------------------------------------
#Find number of palindromic substrings of a string (single characters are counted as palindromic substrings)

def palindrome(str):
    s=[i for i in str]
    x=[i for i in str]
    x.reverse()
    if x==s:
        return True
    else:
        return False

def palindromic_substrings(string):

    subString=[]
    palindromee=[]

    for i in range(len(string)):
        for j in range(i+1,len(string)+1):
            subString.append(string[i:j])
    #print(subString)
    for i in subString:
        if palindrome(i):
            palindromee.append(i)
    print(palindromee)
    print(len(palindromee))

palindromic_substrings("aaaa")#10
palindromic_substrings("skdksks")#11
palindromic_substrings("xcxcd")#7

#-----------------------------------------
#We have array of numbers A
#We have integer k
#We should create sub arrays of length k
#Then from a sub array we choose max and min value --> unfairness =max(subarray) - min(subarray)
#Do this for each sub array
#Then print the minimum unfairness

import itertools
def min_result(arr,k):

    x=[]

    subArr=list(itertools.combinations(arr, k))
    for i in subArr:
        min_value=min(i)
        max_value=max(i)

        unfairness=max_value - min_value
        x.append(unfairness)

    print(min(x)) # minimum unfairness

min_result([1,4,7,2],2) #1 --> [1,2] --> 2 - 1 = 1
min_result([10,100,300,200,1000,20,30],3) # 20 ---> max(10,20,30) - min(10,20,30) = 30 -10 =20
min_result([1,2,3,4,10,20,30,40,100,200],4) #3 ---> max(1,2,3,4) - min(1,2,3,4) = 4 -1 =3

#------------------------------------------
#Ignore sections of array starting with 10 and ending with 11 and return the sum of remaining numbers in array

def sumArr(arr):
    if 10 in arr and 11 in arr:
        x=arr.index(10)
        y=arr.index(11)
        new_arr=arr[x:y+1]
        a=[]
        for i in arr:
            if i not in new_arr:
                a.append(i)
        return sum(a)

    else:
        return sum(arr)

print(sumArr([1, 2, 2])) # 5
print(sumArr([1, 2, 2, 10, 99, 99, 11])) # 5
print(sumArr([1, 1, 10, 11, 2])) # 4
#------------------------------------------
#Find longest consecutive character for example: AABCDDBBBEA --> longest consecutive character is BBB i.e {'B': 3}

def longest_consecutive_character(string):
    a=[]
    x=[i for i in string]
    x.append("0")

    for i in range(len(x[:-1])):
        if x[i]==x[i+1]:
            a.append(x[i])

        elif x[i]==x[i-1] and x[i]!=x[i+1]:
            a.append(x[i])

    counter={}
    final_result={}
    for char in a:
        counter[char]=a.count(char)

    for v in counter.values():
        if v==max(counter.values()):
            final_result[char]=v

    print(final_result)

longest_consecutive_character("AABCDDBBBEA") # {'B': 3}

longest_consecutive_character("XXYUMMMM") # {'M': 4}

longest_consecutive_character("TTGGGGGVA")# {'G': 5}

#------------------------------------------
#Determine the number of times that the string "code" appears anywhere in the given string
#Except we accept any letter for the 'd', for example  "cope" and "cooe" are acceptable

def count_code(s):
    x=[]
    for i in range(len(s)):
        for j in range(len(s)):
            for k in range(len(s)):
                for r in range(len(s)):
                    if i+1==j and j+1==k and k+1==r and s[i]=="c" and s[j]=="o" and s[r]=="e":
                        x.append([s[i],s[j],s[k],s[r]])
    print(x)
    print(len(x))

count_code('aaacodebbb') # 1
count_code('codexxcode') # 2
count_code('cozexxcope') # 2
count_code('codexxcooexxxcoze') #3
count_code('oAcodeBcoleccoreDD')#3

#------------------------------------------
#Given a string return a new string where all the characters are duplicated

def duplicated_chars(string):
    x=[i+i for i in string]
    new_string=''.join(x)
    return new_string

print(duplicated_chars("ABCD!"))#AABBCCDD!!
print(duplicated_chars("cat_dog."))#ccaatt__ddoogg..
