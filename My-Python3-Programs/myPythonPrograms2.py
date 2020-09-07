#characotor at index n is removed

def remove_char_at_index_n(str,n):
    front=str[:n] #from begining to n
    back=str[n+1:]# from n+1 to the end
    print(front+back)
remove_char_at_index_n("hello",0) #call the function

#another solution:
def remove_char(str,index):
    a=[i for i in str]
    a.pop(index)
    x=''.join(a)
    return x

print(remove_char("computer",2))

#----------------------------------------
#first and last char of a string is swapped

def swap_first_abd_last(str):
    my_first_cahr=str[:1]
    my_last_char=str[-1:]
    print(my_last_char+str[1:-1]+my_first_cahr)
swap_first_abd_last("Computer")

#----------------------------------------
#reverse the list (merhod1)
myList1=[1,2,3,4,5]
myList2=["a","b","c","d"]
myList1.reverse()
myList2.reverse()
print(myList1)
print(myList2)

#----------------------------------------
#seperate elements of a list by hash#

myArr=[ "banana","orange","cat"]
x="#".join(myArr)
print(x)

#----------------------------------------
# add an element to every list item

items = ["A","B", "C", "D"]
my_new_list = ["a" + i for i in items]
print(my_new_list)

#----------------------------------------
#multiply every element of array by a number

def my_multiply_Function(myArr,value):
    for i in myArr:
        print(i*value)

myArr=[1,2,3,4,5]
my_multiply_Function(myArr,2)

#----------------------------------------
# myArr * 3 gives three copies of myArr i.e [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
#----------------------------------------
#A letter of a string replaced by another letter

def replace_by_another_letter(str,letter1,letter2):
    str=str.replace(letter1,letter2)
    print(str)

replace_by_another_letter("hello","h","C")

#----------------------------------------
#given an index of a letter of a string , we want to replace that letter with another letter

def replace_by_index(str,index,letter):
    str=list(str)
    str[index]=letter
    str="".join(str)
    print(str)
replace_by_index("Hello",0,"E")

#another solution:
def replace_by_index(str,inx,l2):
    x= str[inx]
        return str.replace(x,l2)
print(replace_by_index("table",1,"m"))

#----------------------------------------
#remove odd numbers

myArr=[]
myArr2=[1,2,3,4,5,6,7,8,9,10]
for i in myArr2:
    if i%2==0:
        myArr.append(i)
print(myArr)

#----------------------------------------
#mean of numbers in array

myArray=[1,2,3,4,5,6]
add_up=sum(myArray)
mean=add_up/len(myArray)
print(mean)

#or we can write it in one line:
print(sum(myArray)/len(myArray))

#----------------------------------------
#median of list

def median(my_array):
    my_array.sort() # first we need to sort the array
    if len(my_array)%2!=0: # i.e when length of array is odd the middle element is median
        middle=int(len(my_array)/2)
        middle=my_array[middle]
        print(middle)
    else:
        middle1 = int(len(my_array) / 2)
        middle = my_array[middle1]
        before_middle=middle1-1
        before_middle=my_array[before_middle]
        print((before_middle+middle)/2)

arrw=[20,10,40,30,50]
arW=[5,2,3,1,6,4]
median(arrw) #call the function
median(arW) #call the function

#----------------------------------------
#find mode in array
#mode is an element that appeared more frequently than others

def mode(arr):
    a=[]
    c=[]
    for i in arr:
      x=arr.count(i)
      a.append([i,x])
    for i in a:
      c.append(i[1])
    frequent=max(c)

    for i in a:
      if i[1]==frequent:
        print("mode is",i[0])
        break

array=[20,20,20,10,40,30,50,50]
mode(array) # gives 20

#----------------------------------------
#funtion that removes duplicates

my_list=[]
def remove_duplicates(myList):
    for i in myList:
        if i not in my_list:
            my_list.append(i)
    print(my_list)

list1=[1,2,2,3,2,3,2,4,5,6,8,8,9,9,10,10,7,7]
remove_duplicates(list1)

#----------------------------------------
#product of elements of list together

def multiply_items(myArray1):
    x=1
    for i in myArray1:
        x=x*i
    print(x)
s=[1,2,3,4]
multiply_items(s)

#----------------------------------------
#reverse the string

def reverse_string(str):
    
    a=[i for i in str]
        a.reverse()
            print(''.join(a))

reverse_string("computer")

#another solution:
def my_reverse_string_function(str):
    letter = ""
    for l in str:
        x = l + letter
        letter = x
    print(letter)

my_reverse_string_function("computer")

#----------------------------------------
#a function that removes vowels

def anti_vowel_function(str):
    vowels=['a','e','u','i','o']
    str=str.lower()

    for i in str:
        for j in vowels:
            if i==j:
                str=str.replace(i,"")
    print(str)
anti_vowel_function("computer Science YaaY ")

#----------------------------------------
#create a list
#double the elements
#then at last we want the double numbers divisible by three

my_list1=[x for x in range(1,11)] # list from 1 to 10
my_list2=[2*x for x in range(1,11)] # double the elements
print(my_list2)

myArray1=[] # will contain the numbers divisible by 3
for i in my_list2:
    if i%3==0:
        myArray1.append(i)
print (myArray1)

#another solution:
l=[1,2,3,4]
a=[2*i for i in l ]
x=[i for i in a if i%3==0]
print(x)

#----------------------------------------
#create list of square of even numbers that are between 1 and 11

x=[x for x in range(1,12)]
print(x)
y=[]

for i in x:
    if i%2==0:
        y.append(i)

square_of_even_numbers=[k**2 for k in y]
print(square_of_even_numbers)

#another solution
a=[i**2 for i in range(1,12)]
b=[i for i in a if i%2==0]
print(b)

#----------------------------------------
#create a list called cubes by four that have cubes of numbers 1 through 10 only if the cube is divisible by 4

x=[i **3 for i in range(1,11)]
cubes_by_four =[]
for j in x:
    if j%4==0:
        cubes_by_four.append(j)
print(cubes_by_four)

#another solution
a=[i**3 for i in range(1,11)]
b=[i for i in a if i%4==0]
print(b)

#----------------------------------------
# remove an element from an array at given index

def remove_element(arrr,index):
    arrr[index]=""
    print(arrr)
a=[1,2,3,4,5]
remove_element(a,1)
b=["a","b","c"]
remove_element(b,2)

#----------------------------------------
#remove a letter from string at given index

def remove_letter(str,letter):
    str=str.replace(letter,"")
    print(str)
remove_letter("Hello","H")

#another solution
def remove_ele(str,n):
    str=list(str)
    str[n]=''
    str=''.join(str)
    return str
remove_ele("computer",0)

#----------------------------------------
#print every number that are in second distance of each other(jump two distance each time)

arr=[1,2,3,4,5,6,7,8,9,10]
print(arr[::2])

#----------------------------------------
#factorial

def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
n=3
print("factorial for",n,"is",factorial(n))
print("1! is",factorial(1))

#----------------------------------------
#array of numbers between 1 and 10 , square them, find out if those squares are between 30 and 70

z=[x**2 for x in range(1,11)]

for i in z:
    if i in range(30,71):
        print(i)

#another solution
a=[]
for i in range(1,11):
    a.append(i)
b=[j**2 for j in a]
c=[k for k in b if k in range(30,71)]
print(c)

#----------------------------------------
#binary Search iterative

def myBinarySearchFunction(my_array,  searchValue):

    arr.sort() # first we need to sort the array
    firstIndex=0 # this is lowest index
    lastIndex=len(arr)-1 # this is highest index which is one less than length of the array

    # we will stop whenever firstIndex becomes bigger than lastIndex
    while firstIndex <= lastIndex:

        middleIndex =(lastIndex + firstIndex) / 2 # this is middle index

        middleIndex=int(middleIndex) # we dont want decimal number

       # if search value is located at middle index we return the middle index
        if my_array[middleIndex] == searchValue:
            return middleIndex

            # when search value is bigger than middle value then we need to update first index (i.e first index comes after middle index)
        elif my_array[middleIndex] < searchValue:
                firstIndex = middleIndex + 1

            # when search value is less than middle value then we update the last index (i.e last index comes before middle value)
        elif my_array[middleIndex] > searchValue:
            lastIndex = middleIndex - 1

    # we return false if we could not find the search value
    return False

my_list=[8,5,9,13,100,46] # this array need to be sorted and will be sorted inside our function
mySearchValue=100

if myBinarySearchFunction(my_list, mySearchValue):
    print ("The search value is at index: ", myBinarySearchFunction(my_list, mySearchValue) )
else:
    print("The search value is not found.")

#----------------------------------------
#meal Cost

def mealCost(mealCost,tip,tax):
    tip= mealCost*(tip/100)
    tax=mealCost*(tax/100)
    print(round(mealCost+tip+tax))
mealCost(12,20,8)

#----------------------------------------
#age Class

class Person:
    def __init__(self,initial_age):
        self.initial_age=initial_age

        if initial_age<0:
            self.age=0
            print("age is not valid, setting age to 0")
        else:
            self.age=initial_age

    def yearsPasses(self):
        self.age=self.age+1
        print(self.age)
    def amIold(self):
        if self.age < 13:
             print("you are young")
        elif self.age >= 13 and self.age<18:
             print("you are teenager")
        else:
            print("you are old")

object1=Person(11)
object1.yearsPasses()
object1.amIold()

object1=Person(-2)
object1.yearsPasses()
object1.amIold()

object1=Person(20)
object1.yearsPasses()
object1.amIold()

object1=Person(14)
object1.yearsPasses()
object1.amIold()

#----------------------------------------
#input n and output = n*i where 1<=i<=10

def m(num):
    for i in range(1,11):
        print(num,"x",i,"=",num*i,"\n")

m(2)

#----------------------------------------
#even index Space odd index

def even_odd(str):
    even=[]
    odd=[]
    for i in str:
        if str.index(i)%2==0:
            even.append(i)
        else:
            odd.append(i)
    print(''.join(even),' ',''.join(odd))

even_odd("computer")
even_odd("science")

#----------------------------------------
#reverse the array and separate by a space

def my_list(value):

    a=[]
    for i in range(1,value+1):
        a.append(i)
    a.reverse()
    print(*a, sep=' ')


#x=int(input("enter a number greater than 1:"))
#my_list(x)

#another solution:
a=["a","b","c","d"]
a.reverse()
for i in a:
    print(i,' ',end='') # output will be: d  c  b  a
    
#----------------------------------------
#int to binary then count the number of consecutive 1s

def counting1s(n):

    int_to_binary='{0:08b}'.format(n) #binary representation of any integer n

    print("binary representation is:",int_to_binary)
    x=map(len,int_to_binary.split('0'))
    print( max(x)) #maximum number of consecutive 1s

counting1s(5)
counting1s(13)

#----------------------------------------
#person student class

class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)

class Student(Person):
    #Class Constructor
     def __init__(self,firstName,lastName,idNumber,scores):

         Person.__init__(self, firstName, lastName, idNumber)
         self.scores = scores
    
     #Parameters:
     #firstName - A string denoting the Person's first name.
     #lastName - A string denoting the Person's last name.
     #id - An integer denoting the Person's ID number.
     #scores - An array of integers denoting the Person's test scores.
     def calculate(self,scores):

            a=sum(scores)
            average=a/len(scores)

            if average < 40:
                return 'T'
            elif average < 55:
                return 'D'
            elif average < 70:
                return 'P'
            elif average < 80:
                return 'A'
            elif average < 90:
                return 'E'
            else:
                return 'O'

scores=[90,80,70,60]
tommy=Student("tommy","T",12345,[90,80,70,60])
tommy.printPerson()
print(tommy.calculate(scores))

#----------------------------------------
#a class that computes maximum difference between any 2 elements of an array

class computeDifference:
    def __init__(self, array):
        self.array=array
        min_element=min(array)
        max_element=max(array)
        print(abs(max_element-min_element))
a=[1,2,5]
object=computeDifference(a)

#----------------------------------------
#calculator class that takes in two numbers
#first number power of second number

class Calculator:
    def __init__(self,n,m):
        self.n=n
        self.m=m

    def calculate(self,n,m):
        if self.n<0 or self.m<0:
            raise Exception(" numbers should be non negative")
        else:
            print( self.n**self.m)

c=Calculator(2,3)
c.calculate(2,3)

#----------------------------------------
#stack

class Stack:
    def __init__(self):
        self.items = [] # create an empty list

    # add item to stack (append to end of list)
    def push(self, item):
        self.items.append(item)

    # remove from stack
    def pop(self):
        return self.items.pop()

    # if stack is empty returns true otherwise false
    def is_empty(self):
        return self.items == []

    # returns top most element of the stack
    def peek(self):
        if not self.is_empty():
            return self.items[-1] # or print(self.items[len(self.items)-1]) --> i.e the last element of list
    def get_stack(self):

        print(self.items)

s=Stack()
s.push("A")
s.push("B")
s.push("C")
s.get_stack()
s.pop()
s.get_stack()
print(s.is_empty())
print(s.peek())

#----------------------------------------
#queue

itemss=["A","B"]

def view():
    for i in range(len(itemss)):
         print(itemss[i])

#appends item at end of queue
def push(i):

    itemss.append(i)

#always pop out first item of list i.e Q[0]
def pop():
    item=itemss.pop(0)
    print("you popped out ",item)

push("R")
push("T")
pop()
view()

#----------------------------------------
#palindrome

def myPalindrome():
    a=str(input("enter a word:"))
    a.lower()

     def my_reverse_string_function(a):
         letter = ""
         for l in a:
             x = l + letter
             letter = x
         return letter
     letter=my_reverse_string_function(a)
     if letter==(a):
         print("it is palindrome")
     else:
         print("not a palindrome")

 myPalindrome()

#another solution
def isPalindrome(str):
    string=[i for i in str]#original string
    s=[i for i in str]
    s.reverse()
    r=[ i for i in s] #reverse the string
    if string==r:
        print("Palindrome")
    else:
        print("Not Palindrome")

isPalindrome("level")#Palindrome
isPalindrome("refer")#Palindrome
isPalindrome("table")#Not Palindrome

#----------------------------------------
#sum of divisors of a number

def sumOfDivisors(n):
    arr=[]
    for i in range(1,n+1):
        if n%i==0:
            arr.append(i)
    print( "sum of the divisors of the number is",sum(arr))
sumOfDivisors(6)
