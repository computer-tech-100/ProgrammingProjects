#return true if number is prime otherwise return false
def is_prime(num):
    
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                
                return False
        else:
            return True
    else:
        return False

print(is_prime(2))#true
print(is_prime(25))#false

#---------------------
#find digits inside a number that divides that number for example consider 24 then 2 and 4 divides 24 so we return 2

def digit(N):
    
    if N in range(1,11):
        print("number of digits is 1")
    elif N>10:
        arr= [int(i) for i in str(N)] # split digits of an integer
        A=[x for x in arr if x != 0] # list arr without zeros in fact we remove 0 from arr since we dont want integer division

        arr2=[]
        for i in A:
            if N%i==0 :
                arr2.append(i)
        print("the number of digits=",len(arr2))

digit(10)
digit(24)
digit(36)
digit(300)
digit(16)

#another solution
n=36
x=str(n)
a=[i for i in x if i!='0']
arr=[]
for i in a:
    i=int(i)
    if n%i==0:
        arr.append(i)
print(len(arr))

#---------------------
#sort intergers in ascending order by the number of 1s in their binary representation
#[7,8,6,5] =[0111,1000,0110,0101] first group the items by number of binary equal to [ [1000] , [0101,0110] , [0111] ]
# the elements 1s now must be ordered : [0110,0101]=[6,5] then sort it [5,6]
#[1000,0101,0110,0111] =[8,5,6,7]

def rearrange(arr):
    aa=[]
    b=[]
    c=[]
    d=[]
    e=[]
    f=[]
    g=[]
    h=[]
    j=[]
    all_binaries=[]
    non_empty_array=[]
    z=[]
    r=[]
    r1=[]
    r2=[]
    r3=[]
    rr=[]
    r4=[]
    r5=[]
    r6=[]
    r7=[]
    all_numbers=[]

    for i in arr:
        int_to_binary = '{0:08b}'.format(i)  # binary representation of any integer i
        x=[k for k in int_to_binary if k=='1'] # consider the ones only  in each binary number

        if len(x)==0:
            l = '{0:08b}'.format(i)
            aa.append(l)
            rr.append(i)

        if len(x)==1:
            l='{0:08b}'.format(i)
            b.append(l)
            r.append(i)

        elif len(x)==2:
            l = '{0:08b}'.format(i)
            c.append(l)
            r1.append(i)

        elif len(x)==3:
            l = '{0:08b}'.format(i)
            d.append(l)
            r2.append(i)

        elif len(x) == 4:
            l = '{0:08b}'.format(i)

            e.append(l)
            r3.append(i)

        elif len(x) == 5:
            l = '{0:08b}'.format(i)

            f.append(l)
            r4.append(i)

        elif len(x) == 6:
            l = '{0:08b}'.format(i)

            g.append(l)
            r5.append(i)

        elif len(x) == 7:
            l = '{0:08b}'.format(i)

            h.append(l)
            r6.append(i)

        elif len(x) == 8:
            l = '{0:08b}'.format(i)

            j.append(l)
            r7.append(i)

    all_binaries.append([aa,b,c,d,e,f,g,h,j])
    all_numbers.append([rr,r,r1,r2,r3,r4,r5,r6,r7])

    for i in all_binaries:
        for j in i:
            if j!=[]:
                non_empty_array.append(j)
    print("this is array of binary numbers base on number of ones:",non_empty_array)
    a=[]
    for i in all_numbers:
        for j in i:
            if j!=[]:
                a.append(j)
    print("this is array of numbers corresponding to binary numbers :",a)

    for i in a:
        i=i.sort()

    print("sort the numbers inside each array",a)

    o=[]
    for i in a:
        for j in i:
          o.append(j)
    print("final result will be:",o)

#test
array=[7,8,6,5]
rearrange(array)

#---------------------
#if any letter in string s is uppercase make it lower and vise versa
#for example: AbCd ---> aBcD

def swap_case(s):
    ss=[i.lower() if i.isupper() else i.upper() for i in s]
    return ''.join(ss)

#another solution:
st="AbCdEfG"
arr=[]
for i in st:
    if i.islower()==True:
        x=i.upper()
        
        arr.append(x)
    if i.isupper()==True:
        y=i.lower()
        arr.append(y)
print(''.join(arr))

#---------------------
#Read a given string, change the character at a given index and then print the modified string.

def change_string(string, position, character):
    a=[i for i in string]
    a[position]=character
    a=''.join(a)
    return a

#another solution:
def change_str(string,pos,c):
    x=string[pos]
    s=string.replace(x,c)
    print(s)

#---------------------
#we give score 2 to a word if we have even number of vowels in that word
#we give score of 1 to a word if we have odd number of vowels in that word
#example programming is awesome has score of 4 since:
#programing has score of 1 (we have 3 vowels oai) ... is has score of 1 ...awesome has score of 2  --> 1+1+2=4

def count_score(str):
    vowels=['a','i','e','o','u']
    arr=[]
    total=[]
    s=str.split()
    a=[]
    for i in s:
        for j in i:
            if j not in vowels:
                i=i.replace(j,"")
        a.append(len(i))
    for i in a:
        if i%2!=0:
            total.append(1)
        else:
            total.append(2)
    print(sum(total))

count_score("computer science is intersting") #4

#---------------------
#replace every number with it's number of occurences
#for example : 1222211 ---> (1,1)(4,2)(2,1)
#we need to use groupby so we need to import it

n=input("enter number:")
from itertools import groupby
print(*[(len(list(num_of_ocurrence_of_i)),int(i) )for i, num_of_ocurrence_of_i in groupby(n)])

#---------------------
#we want to sort string s such that:
#All sorted lowercase letters are ahead of uppercase letters.
#All sorted uppercase letters are ahead of digits.
#All sorted odd digits are ahead of sorted even digits.
#example: Sorting1234  -->  ginortS1324

s=input('Enter:')
upperL=[]
lowerL=[]
odd=[]
even=[]
for i in s:
    if i.isupper():
        upperL.append(i)
    
    elif i.islower():
        lowerL.append(i)

    elif i.isdigit():
        i=int(i)
        if i%2!=0:
            odd.append(i)
        else:
            even.append(i)

upperL.sort()
lowerL.sort()
odd.sort()
even.sort()

sorted_upperCase_letters=''.join(upperL)
sorted_LowerCase_letters=''.join(lowerL)
sorted_odd_numbers=''.join(map(str, odd))
sorted_even_numbers=''.join(map(str, even))

print(sorted_LowerCase_letters+sorted_upperCase_letters+sorted_odd_numbers+sorted_even_numbers)

#---------------------
#we have string of length n
#we have integer k that divides n
#each divided substring might have duplicate charactors
#drop duplicates in each substring and print that substring on new line
#example: AABCAAADA  , k=3
#output:
#AB
#CA
#AD

from  more_itertools import unique_everseen
def split_my_string(str,k):
    
    if len(str)%k==0:
        x=[i for i in str]
        number_of_substrings=int(len(str)/k)
        x=[[]*i for i in range(1,number_of_substrings+1)] #number of empty arrays=number of substrings
        for i in x:
            i=str[:len(x)]
                
            #drop duplicates while you preserve order of elements in list , you should import unique_everseen
            d=list(unique_everseen(i))
            a=''.join(d) # convert from array to string
            print(a)
            str=str.replace(i,'')
    else:
        print('string can not be divided by k')

split_my_string('ASSDFDkkj',3)
split_my_string('AABCAAADA',3)

#---------------------
#given a string we need to print out most common three letters along with their occurance count on separate line
#sort output in descending order of occurrence count.
#If the occurrence count is the same, sort the characters (or letters) in alphabetical order.
#example: aabbbccde
#output:
#b 3
#a 2
#c 2

from collections import Counter
def count_3_comon_chars(string):
    s=[i for i in sorted(string)]
    a=[]
    c=Counter(s)
    top_three=c.most_common(3)
    print(*[str(i[0]) + ' ' + str(i[1]) for i in c.most_common(3)], sep="\n")

count_3_comon_chars("ccbbbaade")

# output for ccbbbaade will be:
# b 3
# a 2
# c 2
# here a and c have same ocuurance 2 then we need to sort them i.e a then c since a comes sooner than c in alphabet

# another example: dddyyyyaaaf
#y 4
#a 3
#d 3
# a and d occurence are the same hence sort them i.e a comes sooner than d

#---------------------
#we have array of numbers ,call this array W
#we have array A and array B
#happiness initially is zero
#if any i from W is in A then we add 1 to happiness
#if any i from W is in B we subtract 1 from happiness
#at last we return result of happiness
#example: W=[1,5,3] , A=[1,3], B=[5,7] so output is amount of happiness i.e 1

def happiness(W,A,B):
    happy=0
    for i in W:
        if i in A:
            happy+=1
        elif i in B:
            happy-=1
    return happy
W=[1,5,3]
A=[1,3]
B=[5,7]
happiness(W,A,B)

#---------------------
#input is bunch of words
#we want to drop duplicates then count the distinct words
#first output is the number of distinct words
#second output is number of occurance of each word base on their order in the original input
#example: suppose input is-->  dog,dog,cat,cat,fish,horse
#drop duplicates--> dog,cat,fish,horse
#when you drop duplicates then count the words which is 4 this is your first output
#second output is 2 2 1 1 because we have two dogs,two cats, 1 fish ,and 1 horse in original input
#another example: hello,hello,hello,bye,yay,yay
#first output: 3
#second output: 3 1 2

from collections import Counter

n=input("Howmany words do you like to enter?")
n=int(n)
arr=[]
ar=[]#remove duplicates
a=[]
v=[]

for i in range(n):
    c=input("Enter a word:")
    arr.append(c)

for i in arr:
    if i not in ar:
        ar.append(i)
print(len(ar))

x=Counter(arr)
s=list(x.values())
c=str(list(x.values()))
c=c.replace(',','') #remove commas
print(c.strip("[]"))#remove brackets

#---------------------
#input is a space-separated lowercase English letters, denoting the elements of the list
#for example a a c d where a is at index 0 and second a is at index 1 then c is at index 2 and d is a at index 3
# we have integer k which specifies size of tuples that contain index of english letters
#for example if k=2 then we have tuples of size two containg indexes: 0123
#(0,1),(0,2),(0,3)(1,2),(1,3)(2,3)
#i.e given an array of size n, we want all possible combinations of r elements in array.
#so we need to use combination
#now we want to figure out the probabilty of having a where a has index 0 and index 1
#so the probabilty will be 5/6 since we have 5 tuples containg a i.e indexes 0 and 1
#so the output is a number which is probabilty of tuples containg a , here it is 5/6

from itertools import combinations
def find_prob(k,n):
    all_index=[]
    n=n.lower()
    arr=list(n)
    print(arr)
    q=[index for index in enumerate(arr)]

    index_of_a=[i[0] for i in q if i[1]=='a']
    print("\n")
    print("a is at index:",index_of_a)
    print("\n")
    for i in q:
        all_index.append(i[0])
    tuples_containing_a=[]
    print("all indices of all elements:",all_index)
    print("\n")
    all_combinations_of_all_index=list(combinations(all_index, k))
    tuples_having__index_of_a=[j for i in index_of_a for j in all_combinations_of_all_index if (j[0]==i or j[1]==i)]
    print("combination of all indices:",all_combinations_of_all_index)

    remove_dup=[]
    for i in tuples_having__index_of_a:
        if i not in remove_dup:
            remove_dup.append(i)

    total=len(all_combinations_of_all_index)
    print(total)
    print("\n")
    print("tuples containg a:",remove_dup)
    le=len(remove_dup)
    print(le)
    probability=le/total

    print("\n")
    print(probability)

find_prob(2,'aacd')

#---------------------
#we want to filter out invalid email addresses
#output will be list of valid email addresses in exicographical order. If the list is empty, just output an empty list, []
#Valid email addresses must follow these rules:
#It must have the username@websitename.extension format type.
#The username can only contain letters, digits, dashes and underscores.
#The website name can only have letters and digits.
#The maximum length of the extension is 3

import re
def valid_emails(email):
    a = re.match(r'[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$',email)
    extension=email.split(".")[1] #this only gets the extension part of an email
    e=email.split("@")[-1]
    website=e.split(".")[0] #this only takes the website part an email
    my_username=email.split("@")[0] # this only gets the username part of an email
    #print("the username is:",my_username)
    #print("the website is:",website)
    #print("the extension is:",extension)
    condition1=False
    for i in my_username:
        if i.isalpha() or i.isdigit() or i=='_'or i=='-':
            condition1=True
        else:
            condition1=False

    condition2=False
    for i in website:
        if i.isalpha() or i.isdigit():
            condition2=True
        else:
            condition2=False

    condition3=False
    if 0<len(extension)<4 :
        condition3=True
    
    condition4=False
    
    if a:
        condition4=True
    else:
        condition4=False

   #print("username:", condition1)
   #print( "website:",condition2)
   #print("extension:",condition3)
   #print("format:",condition4)

    valid= all([condition1,condition2,condition3,condition4])
    #print(valid)
    return valid

s=input("Howmany email address do you like to enter?")
arr=[]

for i in range(int(s)):
    x=input("Enter your email: ")
    arr.append(x)

print("this is list of all email addresses:",arr) # this array contains all of the email addresses

my_arr=[] #will only contain valid emails

# without using filter we want to have sorted valid email addresses
for i in arr:
    valid_emails(i)
    valid=valid_emails(i)
    if valid:
        my_arr.append(i)

x=[i.lower() for i in my_arr] # in order to sort properly we need to have lower case letters

print("\n")
print("This is list of sorted valid emails without using filter:",sorted(x)) # this is without using filter

# But if we want to use filter it is easier and code is shorter , we filter out invalid emails
valid_only=list(filter(valid_emails,arr)) # we apply function to every element in the list

w=[i.lower() for i in valid_only]
print("\n")
print("This is list of sorted valid emails using filter:",sorted(w))

#---------------------
#even 2 means we want to print first two positive even numbers i.e 2 and 4
#odd 3 means we want first three odd numbers i.e 1,3,5
#note that numbers that we print is greater than 0

def play_even_odd(even_or_odd, num):
    if even_or_odd=='odd':
        for i in range(1,num+num+1):
            if i%2!=0:
                print(i)


    elif even_or_odd=='even':
        for i in range(1,num+num+1):
            if i%2==0:
                print(i)

#play_even_odd('odd',6)
#play_even_odd('odd',2)
#play_even_odd('even',3)
#play_even_odd('odd',5)
#play_even_odd('even',7)

#---------------------
#determine if a credit card number is valid or not:
#valid credit card has:
#It must start with a 4 ,5  or 6 (con1)
#It must contain exactly 16 digits.(con2)
#It must only consist of digits (0-9). (con3)
#It must NOT have 4 or more consecutive repeated digits.(con4)
#It must NOT use any other separator like ' ' , '_', etc.(con5)(con4)
#It may have digits in groups of 4 separated by one hyphen "-".(con5)

import re
def valid(cardNumber):
    con1=False
    
    arr=[int(i) for i in str(cardNumber) if i!='-' and i.isdigit()]
    if arr[0]==4 or arr[0]==5 or arr[0]==6:
        con1=True
    else:
        con1=False

    con2=False
    w=[i for i in cardNumber if i!='-' and i.isdigit()]
    if len(w)==16:
        con2=True
    else:
        con2=False
    con3=False
    w=[int(i) for i in str(cardNumber) if i!='-' and i.isdigit()]
    for i in w:
        if 0<=i<=9 :
            con3=True
        else:
            con3=False

    con4=False

    no_four_consecutive= r"((\d)-?(?!(-?\2){3})){16}"#  NOT have 4 or more consecutive repeated digits

    formatt=re.match(no_four_consecutive,cardNumber)

    if formatt:
        con4=True
    else:
        con4=False
    con5=False
    
    form=re.match(r"(-?\d{4}){4}$",cardNumber) #goup of 4 digits sep by "-"

    if form:
        con5=True
    else:
        con5=False
    valid=all([con1,con2,con3,con4,con5])
    if valid:
        print("this is a valid credit card number")
    else:
        print("this is not a valid credit card number")
    return valid

valid('4253625879615786')#valid
valid('6676-3456-8912-3450')#valid
valid('5122-2368-7954 - 3214') #not valid because separators other than '-' are used

#---------------------
# we want to replace part of string with another substring
# we can use re.sub()
import re
s = "hello there is a cat && there is a dog || we can say there is a mouse"
s = re.sub(r" \&\&(?= )", " and", s)  #replacing && with and
s = re.sub(r" \|\|(?= )", " or", s)  #replacing || with or
s=re.sub("mouse", 'bird', s) #replacing mouse with bird
print(s)
