#Write a function that takes in a string and for each character, returns
#the distance to the nearest vowel. If the character is a vowel itself, return 0
#All input strings will contain at least one vowel.
#Strings will be lowercased.
#Vowels are: a, e, i, o, u

def distance_to_nearest_vowel(string):
    
    string=string.lower()
    
    vowels=[ 'a', 'e', 'i', 'o', 'u']
    a=[]
    v=[]
    
    #get the indices of vowels
    for inx, char in enumerate(string):
        if char in vowels:
            v.append(inx)

for i in range(len(string[:-1])):
    if string[i] in vowels:
        a.append(0)
        
        elif string[i] not in vowels and string[i-1] in vowels and string[i+1] not in vowels:
            a.append(1)
        
        elif string[i] not in vowels and string[i - 1] not in vowels and string[i + 1] in vowels :
            a.append(1)
        
        elif string[i] not in vowels:
            #a.append("not v")
            m1=abs(i-min(v))
            m2=abs(i-max(v))
            if m1<m2:
                a.append(m1)
            else:
                a.append(m2)

index_of_last=len(string)-1
    
    if string[-1:] in vowels:
        a.append(0)
    elif string[len(string)-1] not in vowels and string[len(string)-2] in vowels:
        a.append(1)
    elif string[len(string)-1] not in vowels:
        m=max(v)
        dif=abs(index_of_last - m)
        a.append(dif)

print(a) # print the result

distance_to_nearest_vowel("aaaaa") #➞ [0, 0, 0, 0, 0]
distance_to_nearest_vowel("babbb") #➞ [1, 0, 1, 2, 3]
distance_to_nearest_vowel("abcdabcd") #➞ [0, 1, 2, 1, 0, 1, 2, 3]
distance_to_nearest_vowel("shopper") #➞ [2, 1, 0, 1, 1, 0, 1]
distance_to_nearest_vowel("table") #➞ [1,0,1,1,0]
distance_to_nearest_vowel("wxyzobcdf") #➞ [4,3,2,1,0,1,2,3,4]

#--------------------------------------------------------------------------------------------------
#by having an integer N we want to print it's palindromic triangle
#for example if N=5 then it's palindromic tringle will be:
#1
#121
#12321
#1234321
#123454321

a=[]
b=[]
n=5

for i in range(1,n+1):
    a.append(i)
    b.append(i)

a=a[:-1]
a.reverse()
for i in a:
    b.append(i)

for i in b:
    print(i,end="")

#--------------------------------------------------------------------------------------------------
#pick only one element from each list ( we have k lists such that 1<= k <= 7 )
#then do this: ( add up square of each element) % M  where  1<=M<=1000
#note that we want the maximum result
#example:
#2 5 4
#3 7 8 9
#5 5 7 8 9 10
#we choose 5 from first list
#we choose 9 from second list
#we choose 10 from third list
#(25+81+100) % 1000 = 206 which is max value

N=[[2,5,4],[3,7,8,9],[5,5,7,8,9,10]]
arr=[]
for i in N:
    arr.append(max(i))
#print(arr)
x=[int(i)**2 for i in arr]
#print(x)
addd=sum(x)
M=1000
#print(addd%M)

#--------------------------------------------------------------------------------------------------
#Given a two list. Create a third list by picking an odd-index element from the first list
#and even index elements from second.

l1=[1,2,"A","B","C","W",0,7,8]
l2=["D","E",3,4,5,6,"G","N",40]

l3=[]
odd_list_one=[ i for i in l1 if l1.index(i)%2!=0]
even_list_two=[ i for i in l2 if l2.index(i)%2==0]
for i in odd_list_one:
    l3.append(i)
for i in even_list_two:
    l3.append(i)
#print(l3)

#--------------------------------------------------------------------------------------------------
#we have a function that has two arguments: a list and a number
#we add 2 to odd numbers in the list and we subtract 2 from even numbers in the list
#the number of the times that we do this is depend on number which was the second argument
#for example:
#([3, 4, 9], 3) means we add 2 three times to odd numbers i.e to 3 and 9 and we three times subtract 2 from 4
#result will be [9, -2, 15] and we output the result

def even_odd(myList,N):

    odds=[i for i in myList if i%2!=0]
    evens=[i for i in myList if i%2==0]

    l=[]

    for i in myList:
        if i in odds:
            for j in range(N):
                i=i+2
        else:
            for j in range(N):
                i=i-2
        l.append(i)
    print(l)

#even_odd([1,2,3],1)
#even_odd([3,4,9],3)
#even_odd([0,0,0],10)

#--------------------------------------------------------------------------------------------------
#In each input list, every number repeats at least once, except for two.
#Write a function that returns the two unique numbers.
#example:
#returnUnique([1, 9, 8, 8, 7, 6, 1, 6]) ➞ [9, 7]
#returnUnique([5, 5, 2, 4, 4, 4, 9, 9, 9, 1]) ➞ [2, 1]
#returnUnique([9, 5, 6, 8, 7, 7, 1, 1, 1, 1, 1, 9, 8]) ➞ [5, 6]

def returnUnique(myList):
    arr=[]
    for i in myList:
        if myList.count(i)==1:
            arr.append(i)

    print(arr)
    
#returnUnique([1, 9, 8, 8, 7, 6, 1, 6])
#returnUnique([5, 5, 2, 4, 4, 4, 9, 9, 9, 1])
#returnUnique([9, 5, 6, 8, 7, 7, 1, 1, 1, 1, 1, 9, 8])

#--------------------------------------------------------------------------------------------------
#Create a function that takes in a list and returns a list of the accumulating sum.
#example:
#accumulating_list([1, 2, 3, 4]) ➞ [1, 3, 6, 10]
#[1, 3, 6, 10] can be written as  [1, 1 + 2, 1 + 2 + 3, 1 + 2 + 3 + 4]
#accumulating_list([1, 5, 7]) ➞ [1, 6, 13]
#accumulating_list([1, 0, 1, 0, 1]) ➞ [1, 1, 2, 2, 3]
#accumulating_list([]) ➞ []

def accumulating_list(myList):
    a=0
    arr=[]
    for i in myList:
        a=a+i
        arr.append(a)

    print(arr)

#accumulating_list([1, 5, 7])
#accumulating_list([1, 2, 3, 4])
#accumulating_list([1, 0, 1, 0, 1])
#accumulating_list([])

#--------------------------------------------------------------------------------------------------
#Create a function that tests whether or not an integer is a perfect number.
#A perfect number is a number that can be written as the sum of its factors, excluding the number itself.
#For example, 6 is a perfect number, since 1 + 2 + 3 = 6, where 1, 2, and 3 are all factors of 6.
#Similarly, 28 is a perfect number, since 1 + 2 + 4 + 7 + 14 = 28.

def check_perfect(num):

    arr=[]
    for i in range(1,num):
        if num%i==0:
            arr.append(i)
    if sum(arr)==num:
        print(True) # i.e yes it is a perfect number
    else:
        print(False)

#check_perfect(6) # True
#check_perfect(28) # True
#check_perfect(496) # True
#check_perfect(12) # False
#check_perfect(97) # False

#--------------------------------------------------------------------------------------------------
#Suppose you have a dictionary guest list of students and the country they are from,
#stored as key-value pairs in a dictionary.
#Write a function that takes in a name and returns a name tag, that should read:
# "Hi! I'm [name], and I'm from [country]."
#If the name is not in the dictionary, return:
#"Hi! I'm a guest.

def greeting(name):

    GUEST_LIST = {

        "Randy": "Germany",
        "Karla": "France",
        "Wendy": "Japan",
        "Norman": "England",
        "Sam": "Argentina"
    }
    for i in GUEST_LIST.keys():
        if i==name:
            print("Hi! I am", name , "and I am from", GUEST_LIST[name] )

    if name not in GUEST_LIST.keys():
        print("Hi! I'm a guest.")

#greeting("Randy") # "Hi! I'm Randy, and I'm from Germany."
#greeting("Sam") # "Hi! I'm Sam, and I'm from Argentina."
#greeting("Monti") # "Hi! I'm a guest."

#--------------------------------------------------------------------------------------------------
#write a function that counts number of overlapping intervals with a given number
#It takes two arguements: first parameter is list of intervals , second parameter is the number
#example:
#count_overlapping([[1, 2], [2, 3], [1, 3], [4, 5], [0, 1]], 2) ➞ 3
# Since [1, 2], [2, 3] and [1, 3] all overlap with point 2

arr=[]
def count_overlapping(myList,number):
    for i in myList:
        if number in range(i[0],i[1]+1):
            arr.append(i)
    print(len(arr))

#count_overlapping([[1, 2], [2, 3], [3, 4]], 5)  #0
#count_overlapping([[1, 2], [5, 6], [5, 7]], 5) #2
#count_overlapping([[1, 2], [5, 8], [6, 9]], 7)  #2
#count_overlapping([[1, 2], [2, 3], [1, 3], [4, 5], [0, 1]], 2) #3

#---------------------------------------------------------------------------------------------------
#Create a function that takes an integer and outputs an n x n square solely consisting of the integer n
#example:
#square_patch(3) is:
#  [
#  [3, 3, 3],
#  [3, 3, 3],
#  [3, 3, 3]
#   ]

def square_patch(num):
    if num>0:
        a=num*(list([num]))
        x=[a for i in range(num)]
        for i in x:
            print(i)

    elif num==0:
        print("[]")
    else:
        print("number should be positive")

#square_patch(3)
#square_patch(5)

#---------------------------------------------------------------------------------------------------
#Write a function that takes in a string and replaces all 'a's with 4, 'e's with 3, 'i's with 1, 'o's with 0, and 's's with 5.

def change_string(myString):
    myString=myString.lower()

    for i in myString:
        if i=='a':
            myString=myString.replace(i,"4")
        elif i=='e':
            myString = myString.replace(i, "3")

        elif i=='i':
            myString = myString.replace(i, "1")

        elif i=='o':
            myString = myString.replace(i, "0")

        elif i=='s':
            myString = myString.replace(i, "5")

    print( myString)

#change_string("javascript is cool")  #"j4v45cr1pt 15 c00l"
#change_string("programming is fun") #"pr0gr4mm1ng 15 fun"
#change_string("become a coder")  #"b3c0m3 4 c0d3r"

#---------------------------------------------------------------------------------------------------
#Create a function that takes a string, checks if
#it has the same number of x's and o's and returns either true or false.
#It returns true if there aren't any x's or o's.
#Must be case insensitive.

def XO(string):

    x=[]
    o=[]

    for i in string:

        if i=="x" or i=="X":
            x.append(i)
        elif i=="o" or i=="O":
            o.append(i)


    if len(x)==len(o):
        print(True)
    else:
        print(False)

#XO("ooxx") # true
#XO("xooxx") #false

#case sensitive
#XO("ooxXm") # true

# Returns true if no x and o.
#XO("zpzpzpp") # true
#XO("zzoo") # false

#---------------------------------------------------------------------------------------------------
#Given a common phrase, return False if
#any individual word in the phrase contains duplicate letters. Return True otherwise.
#for example: keep has duplicate letter e

def no_duplicate_letters(myPhrase):
    duplicates=[]
    non_duplicates=[]
    words=myPhrase.split()
    for i in words:
        for j in i:
            if i.count(j)>1:
                duplicates.append(j)
    if duplicates!=[]:
        print(False)
    else:
        print(True)

#no_duplicate_letters("Fortune favours the bold.") # True
#no_duplicate_letters("You can lead a horse to water, but you can't make him drink.") # True
#no_duplicate_letters("Look before you leap.") # False
#Duplicate letters in "Look" and "before".
#no_duplicate_letters("An apple a day keeps the doctor away.") # False
# Duplicate letters in "apple", "keeps", "doctor", and "away".

#---------------------------------------------------------------------------------------------------
#You are given three inputs: a string, one letter, and a second letter.
#Write a function that returns True if every instance of the first
#letter occurs before every instance of the second letter.
#All strings will be in lower case.
#All strings will contain the first and second letters at least once.
#All strings will be in lower case.
#All strings will contain the first and second letters at least once.

def first_before_second(mySentence, firstLetter, secondletter):

    mySentence=mySentence.lower()
    arr=[]
    x=[i for i, letter in enumerate(mySentence) if letter == firstLetter]
    w = [i for i, letter in enumerate(mySentence) if letter == secondletter]

    a=[]
    b=[]
    for i in x:
        for j in w:
            a.append(([i,j]))

    c=[i[0] <i[1] for i in a]

    if all(c)==True:
        print(True)
    else:
        print(False)

#first_before_second("a rabbit jumps joyfully", "a", "j") # True
#Every instance of "a" occurs before every instance of "j".

#first_before_second("knaves knew about waterfalls", "k", "w") # True

#first_before_second("happy birthday", "a", "y") # False
# The "a" in "birthday" occurs after the "y" in "happy".

#first_before_second("precarious kangaroos", "k", "a") # False

#---------------------------------------------------------------------------------------------------
#Creata a function that flips a horizontal list into a vertical list, and a vertical list into a horizontal list

def flip_list(myList):

    arr=[]
    for i in myList:
        for j in i:
            arr.append(j)

    print(arr)

def flip_listt(myList):

    arr=[]
    for i in myList:
        arr.append([i])

    print(arr)

#flip_listt([1, 2, 3, 4]) #--> [[1], [2], [3], [4]]
# Take a horizontal list and flip it vertical.

#flip_list([[5], [6], [9]]) #--> [5, 6, 9]
# Take a vertical list and flip it horizontal.

#flip_list([]) #--> []

#--------------------------------------------------------------------------------------------------
#Create a function that returns True if two lines rhyme and False otherwise.
#For the purposes of this exercise, two lines rhyme if the last word from each sentence contains the same vowels.
#Case insensitive.
#Here we are disregarding cases like "thyme" and "lime".
#We are also disregarding cases like:
#"away" and "today" (which technically rhyme, even though they contain different vowels).

def does_rhyme(mySentence1,mySentence2):
    a=mySentence1.split()
    b=mySentence2.split()
    last1=a[len(a)-1]

    last2=b[len(b)-1]

    vowels=["a","o","e","u","i","A","O","E","U","I"]
    arr1=[]
    arr2=[]
    for i in last1:
        i=i.lower()
        if i in vowels:
            arr1.append(i)

    for i in last2:
        i=i.lower()
        if i in vowels:
            arr2.append(i)

    if arr1==arr2:
        print(True)
    else:
        print(False)

#does_rhyme("Sam I am!" ,"Green eggs and ham.") # True

#does_rhyme("Sam I am!","Green eggs and HAM.") # True
#Capitalization and punctuation should not matter.

#does_rhyme("You are off to the races", "a splendid day.") # False
#does_rhyme("and frequently do?", "you gotta move.")# False

#--------------------------------------------------------------------------------------------------
#Create a function that takes in n, a, b
#and returns the number of values raised to the nth power lie in the range [a, b], inclusive.
# Remember that the range is inclusive.
# a < b will always be true.
def power_ranger(n,a,b):
    arr=[]
    for i in range(1,100):
        if i**n in range(a,b+1):
            arr.append(i)
    print(len(arr))

#power_ranger(2, 49, 65) #➞ 2
# 2 squares (n^2) lie between 48 and 65, 49 (7^2) and 64 (8^2)

#power_ranger(3, 1, 27) #➞ 3
# 3 cubes (n^3) lie between 1 and 27, 1 (1^3), 8 (2^3) and 27 (3^3)

#power_ranger(10, 1, 5)# ➞ 1
# 1 value raised to the 10th power lies between 1 and 5, 1 (1^10)

#power_ranger(5, 31, 33) #➞ 1

#power_ranger(4, 250, 1300) #➞ 3

#--------------------------------------------------------------------------------------------------
#Write a function that pairs the first number in an array with the last, the second number with the second to last, etc.
#If the list has an odd length, repeat the middle element twice for the last pair.
#Return an empty list if the input is an empty list

def pairs(myArray):
    arr=[]
    arr2=[]

    if len(myArray)%2==0: # when length of array is even
        while myArray !=[]:
            first=myArray[0]
            l=len(myArray)-1
            last=myArray[l]
            arr.append([first,last])
            myArray.pop(0)
            myArray.pop()
        print(arr)
    else:
        middle_element_index=int(len(myArray)/2)
        middle_element=myArray[middle_element_index]

        myArray.pop(middle_element_index)

        while myArray!=[]:

            firstt = myArray[0]
            ll = len(myArray) - 1
            lastt = myArray[ll]

            arr2.append([firstt,lastt])

            myArray.pop(0)
            myArray.pop()
        arr2.append([middle_element,middle_element])
        print(arr2)

#pairs([1, 2, 3, 4, 5, 6, 7]) #➞ [[1, 7], [2, 6], [3, 5], [4, 4]]
#pairs([1, 2, 3, 4, 5, 6]) #➞ [[1, 6], [2, 5], [3, 4]]
#pairs([5, 9, 8, 1, 2]) #➞ [[5, 2], [9, 1], [8, 8]]
#pairs([]) #➞ []

#--------------------------------------------------------------------------------------------------
#Write a function that moves all the zeroes to the end of a list.
#Do this without returning a copy of the input list.
#Keep the relative order of the non-zero elements the same.

def zeroes_to_end(myList):
    arr=[]
    x=[i for i in myList if i!=0]
    for i in myList:
        if i==0:
            arr.append(i)
    for i in arr:
        x.append(i)

    print(x)

#zeroes_to_end([1, 2, 0, 0, 4, 0, 5]) #➞ [1, 2, 4, 5, 0, 0, 0]
#zeroes_to_end([0, 0, 2, 0, 5])# ➞ [2, 5, 0, 0, 0]
#zeroes_to_end([4, 4, 5]) #➞ [4, 4, 5]
#zeroes_to_end([0, 0]) #➞ [0, 0]

#--------------------------------------------------------------------------------------------------
#Create a function that finds how many prime numbers there are, up to the given integer.

def primeNumbers(num):
    arr=[]

    for i in range(2,num):
        isPrime=True
        for j in range(2,i):
            if i%j==0:
                isPrime=False
        if isPrime:
            arr.append(i)

    print(len(arr))

#primeNumbers(10) #➞ 4
#// 2, 3, 5 and 7

#primeNumbers(20) #➞ 8
#// 2, 3, 5, 7, 11, 13, 17 and 19

#primeNumbers(30) #➞ 10
#// 2, 3, 5, 7, 11, 13, 17, 19, 23 and 29

#--------------------------------------------------------------------------------------------------
#Write a function to replace all instances of character x with character y and vice versa.

def doubleSwap(myString,x,y):

    if x in myString and y in myString:
        s1 = myString.replace(x, "1")
        s2 = s1.replace(y, x)
        s3 = s2.replace("1", y)

        print(s3)

#doubleSwap( "aabbccc", "a", "b")# ➞ "bbaaccc"

#doubleSwap("random w#rds writt&n h&r&", "#", "&")
#"random w&rds writt#n h#r#"

#doubleSwap("128 895 556 788 999", "8", "9")
#"129 985 556 799 888"

#--------------------------------------------------------------------------------------------------
#Create a function that takes a string as an argument and returns True if each letter in the string is surrounded by a plus sign.
#Return False otherwise.

def plus_sign(myString):
    arr=[]
    a=[]
    if myString[0]!="+":
        print(False)
    else:
        for i in myString:
            if i.isalpha() == True:
                a.append(i)
                index_of_letter = myString.index(i)
                pre = index_of_letter - 1
                after = index_of_letter + 1
                if myString[pre]=="+" and myString[after]=="+":

                    arr.append(i)
        if arr==a:
            print(True)
        else:
            print(False)

#plus_sign("+f+d+c+#+f+") # True
#plus_sign("+d+=3=+s+") # True
#plus_sign("f++d+g+8+") # False
#plus_sign("+s+7+fg+r+8+") # False
#plus_sign("+w+u+x+1+2=k+")#False
#plus_sign("+s+7=w")

#--------------------------------------------------------------------------------------------------
#Create a function that takes in two words as input and returns a list of three elements, in the following order:
#Shared letters between two words.
#Letters unique to word 1.
#Letters unique to word 2.
#Each element should have unique letters, and have each letter be alphabetically sorted.
#Both words will be in lower case.
#You do not have to worry about punctuation, all words only have letters from [a-z].
#If an element contains no letters, return an empty string (see last example).

def letters(first,second):
    first=first.lower()
    second=second.lower()
    arr1=[]
    for i in first:
        for j in second:
            if i==j:
                arr1.append(i)
    arr=[]
    for i in arr1:
        if i not in arr:
            arr.append(i)

    common=sorted(arr)
    C=''.join(common) #common letters between two words

    first_letters=[i for i in first]
    second_letters=[i for i in second]
    f=[]
    s=[]
    for i in first_letters:
        if i not in second_letters:
            f.append(i)
    ff=[]
    for i in f:
        if i not in ff:
            ff.append(i)
    for j in second_letters:
        if j not in first_letters:
            s.append(j)
    ss=[]
    for i in s:
        if i not in ss:
            ss.append(i)


    f_s=sorted(ff)
    s_s=sorted(ss)
    F=''.join(f_s)
    S=''.join(s_s)

    myArr=[]
    myArr.append([C,F,S])
    print(str(myArr)[1:-1])

#letters("sharp", "soap") #➞ ["aps", "hr", "o"]
#letters("board", "bored") #➞ ["bdor", "a", "e"]
#letters("happiness", "envelope") #➞ ["enp", "ahis", "lov"]
#letters("kerfuffle", "fluffy") #➞ ["flu", "ekr", "y"]
# Even with multiple matching letters (e.g. 3 f's), there should
# only exist a single "f" in your first element.

#letters("match", "ham") #➞ ["ahm", "ct", ""]
#"ham" does not contain any letters that are not found already
#in "match".

#-------------------------------------------------------------------------------------------------
#Write a function that sorts the positive numbers in ascending order,
#and keeps the negative numbers untouched

def sort_pos(lst):
    sorted_pos = sorted([n for n in lst if n > 0])
    new_list = []
    for n in lst:
        if n > 0:

             new_list.append(sorted_pos.pop(0)) # remove one by one from beginning

        else:
             new_list.append(n)
    print(list(new_list))


#sort_pos([6, 3, -2, 5, -8, 2, -2]) #➞ [2, 3, -2, 5, -8, 6, -2]
#sort_pos([6, 5, 4, -1, 3, 2, -1, 1]) #➞ [1, 2, 3, -1, 4, 5, -1, 6]
#sort_pos([-5, -5, -5, -5, 7, -5]) #➞ [-5, -5, -5, -5, 7, -5]
#sort_pos([])# ➞ []

#-------------------------------------------------------------------------------------------------
#A 1 is unhappy if the digit to its left and the digit to its right are both 0s. A 0 is unhappy if the digit to its left and the digit to its right are both 1s.
#If a number has only one neighbor, it is unhappy if its only neighbor is different. Otherwise, a number is happy.
#Write a function that takes in a list of 0s and 1s and outputs the percentage of numbers which are happy.
#The total percentage of numbers which are happy can be represented as:
# % of happy 0s = (# happy 0s + # unhappy 0s) / # total 0s
#% of happy 1s = (# happy 1s + # unhappy 1s) / # total 1s
# %percentage of happy numbers = (% of happy 0s + % of happy 1s) / 2
#[0, 1, 0, 0, 0, 1, 1, 1, 0, 1]
#The first element, a 0, and the last element, a 1 are both unhappy.
#The second element, a 1 is unhappy.
#The second-to-last element, a 0 is unhappy.
#All other numbers in this list are happy.

def percentage_happy(myArr):
    happy_zero=[]
    happy_one=[]
    sad_zero=[]
    sad_one=[]

    if myArr[0]==0:
        if myArr[1]==1:
           sad_zero.append(True)
        else:
            happy_zero.append(True)

    last=len(arr)-1
    if myArr[last]==0:
        if myArr[last-1]==0:
            happy_zero.append(True)
        else:
            sad_zero.append(True)

    if myArr[0] == 1:
       if myArr[1] == 1:
           happy_one.append(True)
       else:
            sad_one.append(True)

    last = len(arr) - 1
    if myArr[last] == 1:
        if myArr[last - 1] == 1:
            happy_one.append(True)
        else:
            sad_one.append(True)

    ArrOfNexts=[]
    ArrOfPre=[]

    for index, value in enumerate(myArr[:-1]):

        preVal = myArr[index - 1]

        ArrOfPre.append([value,preVal])

        nextt = myArr[index + 1]

        ArrOfNexts.append([value,nextt])

    ArrOfNexts.pop(0)
    ArrOfPre.pop(0)

    for i in range(len(ArrOfNexts)):
        if ArrOfNexts[i][0] ==ArrOfPre[i][0]== ArrOfNexts[i][1] == ArrOfPre[i][1] == 1:
            happy_one.append(True)

        elif ArrOfNexts[i][0] ==ArrOfPre[i][0]== ArrOfNexts[i][1] == ArrOfPre[i][1] == 0:
            happy_zero.append(True)

        elif (ArrOfNexts[i][0] == ArrOfPre[i][0] == 0) and (ArrOfNexts[i][1] == ArrOfPre[i][1]==1):
            sad_zero.append(True)

        elif (ArrOfNexts[i][0] == ArrOfPre[i][0] == 1) and (ArrOfNexts[i][1] == ArrOfPre[i][1] == 0):
            sad_one.append(True)

        elif (ArrOfNexts[i][0] == ArrOfPre[i][0] == 1) and ArrOfNexts[i][1] == 1 and  ArrOfPre[i][1] == 0:

            sad_one.append(True)

        elif (ArrOfNexts[i][0] == ArrOfPre[i][0] == 1) and ArrOfNexts[i][1] == 0 and ArrOfPre[i][1] == 1:

            sad_one.append(True)

        elif (ArrOfNexts[i][0] == ArrOfPre[i][0] == 0) and ArrOfNexts[i][1] == 1 and ArrOfPre[i][1] == 0:

            sad_zero.append(True)

        elif (ArrOfNexts[i][0] == ArrOfPre[i][0] == 0) and ArrOfNexts[i][1] == 0 and ArrOfPre[i][1] == 1:

            sad_zero.append(True)

    #print("happy Zero",happy_zero)
    #print("hapy one",happy_one)
    #print("sad one",sad_one)
    #print("sad zero",sad_zero)
    # % of happy 0s = (# happy 0s + # unhappy 0s) / # total 0s
    total_zero=[i for i in myArr if i==0]
    total_one=[i for i in myArr if i==1]
    number_of_happy_zero=len(happy_zero)
    number_of_happy_one = len(happy_one)
    number_of_sad_zero = len(sad_zero)
    number_of_sad_one = len(sad_one)
    #print("h1",number_of_happy_one)
    #print("s1:",number_of_sad_one)
    #print("h0",number_of_happy_zero)
    #print("s0",number_of_sad_zero)
    total_zeroo=len(total_zero)
    total_onee=len(total_one)
    #print("t1",total_onee)
    #print("t0",total_zeroo)

    happy_zero_Percentage=(number_of_happy_zero+number_of_sad_zero)/total_zeroo
    #print(happy_zero_Percentage)
    # % ofhappy1s = (  # happy 1s + # unhappy 1s) / # total 1s
    happy_one_Percentage = (number_of_happy_one + number_of_sad_one )/ total_onee
    #print(happy_one_Percentage)
    #% percentageofhappynumbers = (% of happy 0s + % of happy 1s) / 2
    percentage_of_happynumbers = (happy_zero_Percentage + happy_one_Percentage) / 2
    #print(percentage_of_happynumbers)

#call the functions
#percentage_happy([0, 1, 0, 1, 0])# ➞ 0
#percentage_happy([0, 1, 1, 0]) #➞ 0.5
#percentage_happy([0, 0, 0, 1, 1]) #➞ 1
#percentage_happy([1, 0, 0, 1, 1])# ➞ 0.8
#percentage_happy([1, 0, 1,0,0])

#--------------------------------------------------------------------------------------------------
#Create a function that determines whether each seat can "see" the front-stage. A number can "see" the front-stage if
#it is strictly greater than the number before it.
#Everyone can see the front-stage in the example below

#   FRONT STAGE
#  [[1, 2, 3, 2, 1, 1],
#  [2, 4, 4, 3, 2, 2],
#  [5, 5, 5, 5, 4, 4],
#  [6, 6, 7, 6, 5, 5]]

# Starting from the left, the 6 > 5 > 2 > 1, so all numbers can see.
# 6 > 5 > 4 > 2 - so all numbers can see, etc.

# Not everyone can see the front-stage in the example below:

# FRONT STAGE
# [[1, 2, 3, 2, 1, 1],
#  [2, 4, 4, 3, 2, 2],
# [5, 5, 5, 10, 4, 4],
# [6, 6, 7, 6, 5, 5]]

# The 10 is directly in front of the 6 and blocking its view.
#The function should return True if every number can see the front-stage, and False if even a single number cannot.

def can_see_stage(arr):

    arr=reversed(arr)
    
    #works for arrays of size 3
    f, s,t = zip(*arr)
    x=list([f,s,t])
    #print(x)

    c=[]

    for i in x:
        if i[0]>i[1]>i[2]:
            c.append(True)

        else:
            c.append(False)

    if all(c)==True:
        print(True)
    else:
        print(False)

#can_see_stage([[1, 2, 3],[4, 5, 6],[7, 8, 9]]) #➞ True
#can_see_stage([[0, 0, 0],[1, 1, 1],[2, 2, 2]]) #➞ True
#can_see_stage([[2, 0, 0],[1, 1, 1],[2, 2, 2]])# ➞ False
#can_see_stage([[1, 0, 0],[1, 1, 1],[2, 2, 2]]) #➞ False
#can_see_stage( [[1, 2, 2],[2, 4 , 3],[5, 5 , 10],[6, 6, 6]])#-> False

#-------------------------------------------------------------------------------------------------
#Start your counter at 0, and increment by 1 each time you encounter a new character.
#Identical characters should share the same number.

def character_mapping(string):
    counter=0
    arr=[0]

    for i in range(len(string[:-1])):

        if string[i]!=string[i+1]:

            counter+=1
            arr.append(counter)

        elif string[i]==string[i+1]:

            arr.append(counter)

        else:
            arr.append(counter)

    print(arr)

#character_mapping("abcd") #➞ [0, 1, 2, 3]
#character_mapping("abb") #➞ [0, 1, 1]
#character_mapping("hmmmmm")# ➞ [0, 1, 1, 1, 1, 1]

#-------------------------------------------------------------------------------------------------
#Create a function that returns a list containing the prime factors of whatever integer is passed to it.

from math import sqrt; from itertools import count, islice
from functools import reduce

def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

def prime_factors(num):

    arr=[]
    the_primes=[]

    for i in range(2, num+1):
        if num % i == 0:
            arr.append(i)

    z=[]

    for i in arr:
        if isPrime(i):
            the_primes.append(i)

    a=reduce(lambda x, y: x * y, the_primes)
    s=num/a
    s=int(s)

    if isPrime(s):
        the_primes.append(s)
    else:
        for i in range(2,s+1):
            if isPrime(i) and s%i==0:
                the_primes.append(i)
    print(sorted(the_primes))

#prime_factors(20) #➞ [2, 2, 5]
#prime_factors(100) #➞ [2, 2, 5, 5]
#prime_factors(8912234)# ➞ [2, 47, 94811]

#--------------------------------------------------------------------------------------------------
#Create a function that takes a string and replaces every letter with the letter following it in the alphabet
#i.e "c" becomes "d", "z" becomes "a", "b" becomes "c", etc
#Then capitalize every vowel (a, e, i, o, u) and return the new modified string.
#If a letter is already uppercase, return it as uppercase (regardless of being a vowel).

def replace_with_next(myString):
    
    alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a"]
    alphabet2=[i.upper() for i in alphabet]
    vowels=["a","o","u","e","i"]
    a=[]
    for i in myString:
        if  i.isalpha() and i.islower():
            index_of_i=alphabet.index(i)
            index_of_following_letter=index_of_i+1
            
            myString=myString.replace(i,alphabet[index_of_following_letter])
    
        if i.isalpha() and i .isupper():
            index_of_i=alphabet2.index(i)
            index_of_following_letter=index_of_i+1
            
            myString=myString.replace(i,alphabet2[index_of_following_letter])

    for i in myString:
        if i in vowels:
            myString=myString.replace(i,i.upper())
    
    print(myString)

replace_with_next("fun times!") #➞ "gvO Ujnft!"
replace_with_next("eGG")# ➞ "FHH"
replace_with_next("OMega") #➞ "PNfhb"

#--------------------------------------------------------------------------------------------------
#Create a function that takes a list of numbers or strings and returns a list with the items from the original list stored into sublists.
#Items of the same value should be in the same sublist.

def advanced_sort(arr):
    x=[]
    for i in arr:
        for j in arr:
            if i==j  and arr.count(i)>1:
                x.append([i,j])
            elif arr.count(i)==1:
                x.append([i])
    z=[]
    for i in x:
        if i not in z:
            z.append(i)
    print(z)

#advanced_sort([2, 1, 2, 1]) #➞ [[2, 2], [1, 1]]
#advanced_sort(["b", "a", "b", "a", "c"]) #➞ [["b", "b"], ["a", "a"], ["c"]]

#--------------------------------------------------------------------------------------------------
#Write two functions:
#One that returns the maximum product of three numbers in a list.
#One that returns the minimum product of three numbers in a list.

def max_product(arr):
    s=[]
    for i in arr:
        for j in arr:

            for k in arr:
                if i!=j and i!=k and j!=k:
                    s.append(i*k*j)
    print(max(s))

def min_product(arr):
    s=[]
    for i in arr:
        for j in arr:

            for k in arr:
                if i!=j and i!=k and j!=k:
                    s.append(i*k*j)
    print(min(s))

#max_product([-8, -9, 1, 2, 7]) #➞ 504
#max_product([-8, 1, 2, 7, 9]) #➞ 126
#min_product([-5, -3, -1, 0, -4]) #➞ -60
#min_product([-5, -3, -1, 0, 4]) #➞ -15

#--------------------------------------------------------------------------------------------------
#Sexy primes are primes that differ by 6.
#For example, (5, 11) comprise a sexy prime pair, while (5, 11, 17) comprise a set of sexy prime triplets.
#Create a function that takes two numbers as argument, the set length n (2 for pairs, 3 for triplets), and
#the limit. Return a list of sorted tuples of sexy primes up to (but excluding) the limit.

from math import sqrt; from itertools import count, islice
from functools import reduce

def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

def sexy_primes(count,limit):
    arr=[]

    for i in range(2,limit):
        if isPrime(i):
            arr.append(i)

    result = tuple(arr[x:x + count] for x in range(0, len(arr), count))

    print(result)

#sexy_primes(2, 100) #➞ [(5, 11), (7, 13), (11, 17), (13, 19), (17, 23), (23, 29), (31, 37), (37, 43), (41, 47), (47, 53), (53, 59), (61, 67), (67, 73), (73, 79), (83, 89)]
#sexy_primes(3, 100) #➞ [(5, 11, 17), (7, 13, 19), (11, 17, 23), (17, 23, 29), (31, 37, 43), (41, 47, 53), (47, 53, 59), (61, 67, 73), (67, 73, 79)]
#sexy_primes(3, 250) #➞ [(5, 11, 17), (7, 13, 19), (11, 17, 23), (17, 23, 29), (31, 37, 43), (41, 47, 53), (47, 53, 59), (61, 67, 73), (67, 73, 79), (97, 103, 109), (101, 107, 113), (151, 157, 163), (167, 173, 179), (227, 233, 239)]

#--------------------------------------------------------------------------------------------------
#Write a function that repeats the shorter string until it is equal to the length of the longer string.
#Both strings will differ in length.
#Both strings will contain at least one character.

def lengthen(s1,s2):

    s11=[i for i in s1]
    s22=[i for i in s2]
    if len(s11)<len(s22):
        for i in s11:
            s11.append(i)
            if len(s11)==len(s22):
                print(''.join(s11))
                break
    else:
        for i in s22:
            s22.append(i)
            if len(s22)==len(s11):
                print(''.join(s22))
                break

#lengthen("abcdefg", "ab") #➞ "abababa"
#lengthen("ingenius", "forest") #➞ "forestfo"
#lengthen("clap", "skipping") #➞ "clapclap"

#---------------------------------------------------------------------------------------------------
#An emirp  = is a prime number that when we reverse its digits it is also prime  13 is a prime, and so is 31. Both are therefore emirps.
#A bemirp is a prime which is an emirp but additionally, makes another prime when flipped upside down i.e 9 is upside down of 6 and 6 is upside down of 9
#So Bemirps consist only of digits 0, 1, 6, 8, and 9. it is emirp and upside dwon
#For example: 11061811, reversed = 11816011, upside-down = 11091811, upside-down reversed = 11819011. All four are primes.
#Create a function that takes a number and returns :
#"B" if it’s a bemirp,
#"E" if it's  emirp,
#"P" if it's a  prime, and is not bemirp and is not emirp
#"C" if it is not a prime

from math import sqrt; from itertools import count, islice
from functools import reduce

def isPrime(n):
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

def recognize_prime(num):
    num=str(num)
    re=num[::-1]
    reversee=int(re)

    x = ['0', '1', '6', '8', '9']

    emirp=isPrime(int(num)) and isPrime(int(reversee))
    if emirp:
        print("E : it is  emirp")
    arr=[]
    nineToSix=[]
    sixtoNine=[]
    w=[]
    for i in range(len(num)):
        if num[i] in x:
            arr.append(True)
        else:
            arr.append(False)
    for i in num:
        if i=='9':
            num=num.replace(i,'6')
            if isPrime(int(num)):
                nineToSix.append(True)
            else:
                nineToSix.append(False)

        elif i=='6':
            num=num.replace(i,'9')
            if isPrime(int(num)):
                sixtoNine.append(True)
            else:
                sixtoNine.append(False)
    w.append(nineToSix)
    w.append(sixtoNine)

    a=[]
    for i in w:
        if all(i)==True:
            a.append(True)

    #all elements of num are in x
    Bimirp= len(arr)==len(num) and all(arr)==True and emirp and a!=[]
    if Bimirp:
        print("B: bimirp")

    primee= isPrime(int(num))

    if primee:
        print("p: it is prime")
    if not primee and not Bimirp and not emirp:
        print("c: it is not prime")

#recognize_prime(13)
#recognize_prime(101) #➞ "P"
#recognize_prime(1011) #➞ "C"
#recognize_prime(1069) #➞ "E"
#recognize_prime(1061) #➞ "B"

#--------------------------------------------------------------------------------------------------
#Given an array of strings and an original string,
#write a function to output an array of boolean values - True if the word can be formed from the original word by swapping two letters only once and False otherwise.
#Original string will consist of unique characters.

from itertools import permutations

def validate(element,string):

    aa=[]
    w=element #element

    w=list(w)
    s=string #string

    for k in range(len(w)):
        for j in range(len(w)):

            w=element
            w = list(w)
            w[j],w[k]=w[k],w[j]
            z=''.join(w)
            aa.append(z)

    x=[]

    for i in aa:
        if i not in x:
            x.append(i)

    m=[]
    if s in x:
        m.append('True')
    else:
        m.append('False')

    return m

def validate_swaps(arr,string):
    a=[]
    for i in arr:

        m=validate(i,string)
        a.append(m)
    s=[''.join(i) for i in a]

    print(s)

#validate_swaps(["BACDE", "EBCDA", "BCDEA", "ACBED"], "ABCDE")
#➞ [True, True, False, False]

# Swap "A" and "B" from "ABCDE" to get "BACDE".
# Swap "A" and "E" from "ABCDE" to get "EBCDA".
# Both "BCDEA" and "ACBED" cannot be formed from "ABCDE" using only a single swap.

#validate_swaps(["32145", "12354", "15342", "12543"], "12345")
#➞ [True, True, True, True]

#validate_swaps(["9786", "9788", "97865", "7689"], "9768")
#➞ [True, False, False, False]

#--------------------------------------------------------------------------------------------------
#We can assign a value to each character in a word, based on their position in the alphabet (a = 1, b = 2, ... , z = 26). A
#balanced word is one where the sum of values on the left-hand side of the word equals the sum of values on the right-hand side.
#For odd length words, the middle character (balance point) is ignored.
#Write a function that returns True if the word is balanced, and False if it's not.
#All words will be lowercase, and have a minimum of 2 characters

alphabet=['0','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def balanced(string):
    string=string.lower()

    string=list(string)
    arr=[]
    aa=[]
    b=[]
    first_half_of_even=[]
    second_half_of_even=[]

    if len(string)%2==0:

        a=int(len(string)/2)
        arr.append(string[:a])
        aa.append(string[a:])

        for i in (arr):
                for j in i:
                    first_half_of_even.append(alphabet.index(j))

        for i in (aa):
            for j in i:
                second_half_of_even.append(alphabet.index(j))

        x=sum(first_half_of_even)
        y=sum(second_half_of_even)
        if x==y:
            print(True)
        else:
            print(False)

    else:
        a = int(len(string) / 2)

        string=''.join(string)
        string=string.replace(string[a],'') #remove middle element

        arr.append(string[:a])
        aa.append(string[a:])

        for i in (arr):
            for j in i:
                first_half_of_even.append(alphabet.index(j))

        for i in (aa):
            for j in i:
                second_half_of_even.append(alphabet.index(j))

        x = sum(first_half_of_even)
        y = sum(second_half_of_even)
        if x == y:
            print(True)
        else:
            print(False)

#balanced("zips")
#balanced("brake")

#---------------------------------------------------------------------------------------------------
#Write a Python class to get all possible unique subsets from a set of distinct integers.
#Input : [4, 5, 6]
#Output : [[],[4], [5], [6], [5, 6], [4, 6], [4, 5], [4, 5, 6]]

from itertools import chain, combinations

class subset:
    def __init__(self,string):
        self.string=string

    def sub(self):

       return chain.from_iterable(combinations(list(self.string), i) for i in range(len(list(self.string)) + 1))

a="456"
s=subset(a)
x=list(s.sub())
#print(x)

#---------------------------------------------------------------------------------------------------
#Write a function to find a pair of elements (indices of the two numbers) from a given array whose sum equals a specific target number
#Input: numbers= [90,20,10,40,50,60,70], target=50
#Output: 2,3

def cal(arr,target):
    for i in arr:
        for j in arr:
            if i!=j:
                if i+j==target:
                    print(arr.index(i),arr.index(j))

numbers= [90,20,10,40,50,60,70]
target=50
#cal(numbers,target)

#---------------------------------------------------------------------------------------------------
#Create all possible strings by using 'a', 'e', 'i', 'o', 'u'.Use the charactors exactly once

import itertools
s=['a', 'e', 'i', 'o', 'u']
x=list(itertools.permutations(s))
#for i in x:
    #print(''.join(i))

#---------------------------------------------------------------------------------------------------
#Write a Python program to find common divisors between two numbers in a given pair

def find_divisor(arr):
    f=[]
    s=[]
    c=[]

    for i in range(1,arr[0]+1):
        if arr[0]%i==0:
            f.append(i)

    for i in range(1, arr[1] + 1):
        if arr[1] % i == 0:
            s.append(i)
    for i in f:
        if i in s:
            c.append(i)
    print(f,s,c)
    print("number of common divisors is:",len(c))

#find_divisor([2,4])
#find_divisor([2,8])
#find_divisor([12,24])

#-----------------------------------------------------------Dictionaries------------------------------------------------------
#Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
#sample Dictionary (n = 5) :
#expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

def dic(n):
    d={}
    for i in range(1,n+1):
        d[i]=i*i
    print(d)
#dic(5)

#--------------------------------------------
#Write a Python program to multiply all the values together in a dictionary

my_dict = {'data1':2,'data2':4,'data3':8}
x=1
for i in my_dict.values():
    x=x*i
#print(x)

#--------------------------------------------
#Write a Python program to map two lists into a dictionary.

keys = [1, 2, 3]
values = ['green','red', 'blue']
d={}
for i in keys:
    for j in values:
        d[i]=j
        values.remove(j)
        break
#print(d)

#-------------------------------------------
#Write a Python program to sort a dictionary by key.

d = {4: 10, 3: 20, 2: 30, 6: 40, 5: 50, 1: 60}
d=sorted(d.items())
x={x:y for x,y in d}
#print(x)

#-------------------------------------------
#Write a Python program to combine two dictionary adding values for common keys

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d={}
#Sample output: {'a': 400, 'b': 400, 'c': 300, 'd':400}
for i in d1.keys():
    for j in d1.values():
        for l in d2.keys():
            for k in d2.values():
                if i not in d2.keys():
                    d[i]=j
                    d[l]=k
                else:
                    x=d1[i]+d2[l]
                    d[i]=x

#print(d)

#---------------------------------------------
#Write a Python program to find the highest 3 values in a dictionary.

my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5873, 'f': 20}
arr=[]
keys_of_top_three=[]
w=[]
for i in my_dict.values():
    arr.append(i)
x=sorted(arr)

top_three=x[-3:]
x=[i for i in reversed(top_three)]
#print(x)

for i in x:
    for j in my_dict.keys():
        if my_dict[j]==i:
            keys_of_top_three.append(j)
for i in keys_of_top_three:
    if i not in w:
        w.append(i)
#print(w)

#--------------------------------------------
#Write a Python program to create a dictionary from a string.
#Note: Track the count of the letters from the string.
#string = "programming"
#Expected output: {'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 1, 'n': 1}

def makeDicFromStr(string):
    arr=[]
    for i in string:
        arr.append([i,string.count(i)])
    
    x = {x: y for x, y in arr}
    print(x)
#makeDicFromStr("programming")

#----------------------------------------------
#Write a Python program to sort in descending order by value.

my_dictionaryy={'Math':81, 'Physics':83, 'Chemistry':87}
#Expected data: [('Chemistry', 87), ('Physics', 83), ('Math', 81)]

arr=[]
for i in my_dictionaryy.values():
    arr.append(i)
arr=sorted(arr)
arr=reversed(arr)
w=[]
for i in arr:
    for j in my_dictionaryy.keys():
        if my_dictionaryy[j]==i:
            w.append([j,i])

#print(w)

#----------------------------------------------
#Write a Python program to replace dictionary values with their sum.

my_dict={'Math':2, 'Physics':3, 'Chemistry':1}

x=sum(my_dict.values())

for i in my_dict.keys():
    my_dict[i]=x
#print(my_dict)

#---------------------------------------------
#Write a Python function to check whether a number is perfect or not.
#a perfect number is a positive integer that is equal to the sum of its proper positive divisors,
#that is, the sum of its positive divisors excluding the number itself
#Equivalently, a perfect number is a number that is half the sum of all of its positive divisors (including itself).
#Example : The first perfect number is 6, because 1, 2, and 3 are its proper positive divisors, and 1 + 2 + 3 = 6.
#Equivalently, the number 6 is equal to half the sum of all its positive divisors: ( 1 + 2 + 3 + 6 ) / 2 = 6.
#The next perfect number is 28 = 1 + 2 + 4 + 7 + 14. This is followed by the perfect numbers 496 and 8128.

def perfect(num):
    arr=[]
    for i in range(1,num):
        if num%i==0 :
            arr.append(i)
    if sum(arr)==num:
        print(True)
    else:
        print(False)

#perfect(6)
#perfect(28)
#perfect(496)
