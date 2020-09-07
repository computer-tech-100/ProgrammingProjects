#You are given an input list of strings
#Write a function that returns True if, for each pair of consecutive strings, the second string can be formed from the first by adding a single letter either at the beginning or end
#Return False a word is NOT formed by adding only one letter
#Return False if the letter is added to the middle of the previous word
#All words in array should be lowercase

def myFunction(arr):
    
    a=[] #array that contains lowercase words
    for i in arr:
        if i.isupper()==True:
            
            a.append(i.lower())
        else:
            a.append(i)

    counter=[]
    
    for i in range(1,len(a)):
        word1=a[i][1:]
        word2=a[i][:-1]
        if a[i-1]==word1 or a[i-1]==word2:
            counter.append(True)
        else:
            counter.append(False)

    if all(counter)==True:
       return True
    else:
       return False

print(myFunction(["A", "at", "ate", "LATE", "plate", "plates"])) #➞ True

print(myFunction(["a", "at", "ate", "late", "plate", "plater", "platter"])) #➞ False
#"platter" is formed by adding "t" in the middle of "plater"

print(myFunction(["it", "bit", "bite", "biters"]))#➞ False
#"biters" is formed by adding two letters - we can only add one

print(myFunction(["MEAN", "meany"])) #➞ True

#----------------------------------------------------
#We can assign a value to each character in a word, based on their position in the alphabet (a = 1, b = 2, ... , z = 26)
#A balanced word is one where the sum of values on the left-hand side of the word equals the sum of values on the right-hand side.
#For odd length words, the middle character (balance point) is ignored
#All words will be lowercase, and have a minimum of 2 characters
#Write a function that returns True if the word is balanced, and False if it's not

def balanced(str):
    a=[0,"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    str=str.lower()
    l=int(len(str)/2)
    
    s=[i for i in str]
    first_half=[]
    second_half=[]
    if len(s)%2==0:
        for i in range(l):
            first_half.append(s[i])
        for i in range(l,len(s)):
            second_half.append(s[i])

    else:
        middle_element=s[l]
        withOutMiddle=[i for i in s if i!=middle_element]
        for i in range(l):
            first_half.append(withOutMiddle[i])
        for i in range(l, len(withOutMiddle)):
            second_half.append(withOutMiddle[i])
    inx1=[]
    inx2=[]
    
    for i in first_half:
        inx1.append(a.index(i))

    for i in second_half:
        inx2.append(a.index(i))
    
    print(inx1)
    print(inx2)
    print(sum(inx1))
    print(sum(inx2))
    
    if sum(inx1)==sum(inx2):
        return True #balanced
    else:
        return False #not balanced


print(balanced("zips")) #➞ True
# "zips" = "zi|ps" = 26+9|16+19 = 35|35 = True

print(balanced("brake")) # ➞ False
# "brake" = "br|ke" = 2+18|11+5 = 20|16 = False

print(balanced("level")) # ➞ True
# "level" = "le|el" = 12+5|5+12 = 17|17 = True --> Palindrome is always balanced.

#----------------------------------------------------
#Sort the array creating your own algorithm. Do not use Sorted() function...
#Create a function that takes an array of integers as an argument and returns the same array in ascending order
#The arrays can contain either positive or negative elements
#The arrays will only contain integers
#The arrays does not contain duplicate numbers

def sortTheArray(arr):
    size=len(arr)
    my_sorted_array=[]
    
    for i in range(size):
        
        my_sorted_array.append(min(arr))
        arr.remove(min(arr))
    
    print(my_sorted_array)

sortTheArray([2, -5, 1, 4, 7, 8]) # [-5, 1, 2, 4, 7, 8]

sortTheArray([9, -10, 3, 0, -12]) # [-12,-10,0,3,9]

sortTheArray([23, 15, 34, 17, -28]) # [-28, 15, 17, 23, 34]

#----------------------------------------------------
#Create a function that returns the simplified version of a fraction
#input fraction should be string

def simplify_fraction(f):
    
    division=f.index("/")
    numerator=[f[i] for i in range(len(f)) if i <division]
    denominator = [f[i] for i in range(len(f)) if i > division]
    
    numerator=''.join(numerator)
    denominator=''.join(denominator)
    n=[]
    d=[]
    common=[]
    
    numerator=int(numerator)
    denominator=int(denominator)
    
    for i in range(1,numerator+1):
        if numerator%i==0:
            n.append(i)

    for i in range(1,denominator+1):
        if denominator % i == 0:
           d.append(i)
    
    
    for i in n:
        for j in d:
            if i==j:
                common.append(i)

    x=max(common)
    new_numerator=int(numerator/x)
    new_denominator=int(denominator/x)
    print(new_numerator,"/",new_denominator)

simplify_fraction("5/20") # "1/4"

simplify_fraction("4/6") # "2/3"

simplify_fraction("10/11") # "10/11"

simplify_fraction("100/400") # "1/4"

simplify_fraction("8/4") # "2"

#----------------------------------------------------
#A consecutive run is a list of adjacent, consecutive integers
#This list can be either increasing or decreasing
#Create a function that takes a list of numbers and returns the length of the longest consecutive-run
#return 0 if there is no consecutive run
#There is no duplicates in input array

def longest_consecutive_run(arr):
    
    arr.append("None") #to avoid range error
    
    #consecutive run increasing
    a=[]
    no_duplicates_incereasing=[]
    
    for inx,num in enumerate(arr[:-1]):
        if arr[inx]+1==arr[inx+1]:
            a.append(num)
            a.append(arr[inx+1])

    for i in a:
        if i not in no_duplicates_incereasing:
          no_duplicates_incereasing.append(i)

    #consecutive run decreasing
    b = []
    no_duplicates_decereasing = []

    for inx, num in enumerate(arr[:-1]):
        if arr[inx] - 1 == arr[inx + 1]:
           b.append(num)
           b.append(arr[inx + 1])

    for i in b:
        if i not in no_duplicates_decereasing:
           no_duplicates_decereasing.append(i)
     
    count_increasing=0
    first_half=[]
    first_half_no_duplicates=[]
    
    for i in range(len(no_duplicates_incereasing)):
        if no_duplicates_incereasing[i]+1==no_duplicates_incereasing[i+1]:
            first_half.append(no_duplicates_incereasing[i])
            first_half.append(no_duplicates_incereasing[i+1])
            count_increasing+=1
        else:
            break

    second_half=[]
    for i in first_half:
        if i not in first_half_no_duplicates:
            first_half_no_duplicates.append(i)

    for i in no_duplicates_incereasing:
       if i not in first_half_no_duplicates:
           second_half.append(i)


    l1=len(first_half_no_duplicates)
    l2=len(second_half)

    count_decreasing = 0
    first_half2 = []
    first_half_no_duplicates2 = []
    
    for i in range(len(no_duplicates_decereasing)):
        if no_duplicates_decereasing[i] - 1 == no_duplicates_decereasing[i + 1]:
            first_half2.append(no_duplicates_decereasing[i])
            first_half2.append(no_duplicates_decereasing[i + 1])
            count_decreasing += 1
        else:
            break

    second_half2 = []
    for i in first_half2:
        if i not in first_half_no_duplicates2:
            first_half_no_duplicates2.append(i)

    for i in no_duplicates_decereasing:
        if i not in first_half_no_duplicates2:
            second_half2.append(i)

    l11 = len(first_half_no_duplicates2)
    l22 = len(second_half2)

    if no_duplicates_incereasing==[] and no_duplicates_decereasing!=[]:
    
        return max(l11,l22)
    
    elif no_duplicates_decereasing==[] and no_duplicates_incereasing!=[]:
        
        return max(l1,l2)

    elif no_duplicates_decereasing==[] and no_duplicates_incereasing==[]:
        
        return 0

print(longest_consecutive_run([1, 2, 3, 5, 6, 7, 8, 9])) # 5
#Two consecutive runs: [1, 2, 3] and [5, 6, 7, 8, 9] (longest).

print(longest_consecutive_run([1, 2, 3, 10, 11, 15])) # 3
#Longest consecutive-run: [1, 2, 3].

print(longest_consecutive_run([5, 4, 2, 1])) # 2
#Longest consecutive-run: [5, 4] and [2, 1].

print(longest_consecutive_run([3, 5, 7, 10, 15])) # 0
#No consecutive runs, so we return 0.

#----------------------------------------------------
#Write a function that returns all sets of 3 elements that sum to 0
#The original list may contain duplicate numbers
#Return an empty list if no 3 elements sum to zero
#Return an empty list if there are fewer than 3 elements

def three_sum(arr):
    sumToZero=[]
    s=[]
    for i in arr:
        for j in arr:
            for k in arr:
                if i+j+k==0:
                    sumToZero.append([i,j,k])

    for i in sumToZero:
        i.sort()
    if i not in s:
        s.append(i)
print(s)

three_sum([ 1, -1, -1, 2,-6,-3,-3]) #[[-3, 1, 2], [-1, -1, 2]]

three_sum([0, 0, 0, 7, -7]) #[[0, 0, 0], [-7, 0, 7]]

three_sum([1, 2, 4]) #[]

three_sum([8]) #[]

#----------------------------------------------------
#Write a function that returns true if exactly one word in the array differs in length from the rest
#Return false in all other cases
#The length of the array will always have at least three or more words

def differ_in_length(arr):
    
    lengths=[]
    b=[]
    counts=[]
    for i in arr:
        lengths.append(len(i))
    
    for i in lengths:
        counts.append(lengths.count(i))

    for i in counts:
        if i==1 :
            if counts.count(i)==1:
                return True
            
            else:
                return False

    if 1 not in counts:
        return False


print(differ_in_length(["silly", "mom", "let", "the"])) #true

print(differ_in_length(["swanky", "rhino", "moment"])) #true

print(differ_in_length(["the", "them", "theme"])) #false

print(differ_in_length(["very", "to", "an", "some"])) #false

#----------------------------------------------------
#Create a function that takes in a two-dimensional array as an argument
#and returns a one-dimensional array with the values of the original two dimensional array that are arranged by spiralling through it

def spiral_traverse(arr):
    
    spiral=[]
    first=[i for i in arr[0]]
    b=[]
    for i in first:
        spiral.append(i)
    
    for i in range(1,len(arr)):
        last_el=arr[i][len(arr[i])-1]
        spiral.append(last_el)
    
    last=arr[len(arr)-1]
    for i in last[:-1]:
        b.append(i)
    b.reverse()
    for i in b:
        spiral.append(i)
    
    one_to_last=arr[len(arr)-2]

    if len(arr)>2:
       for i in one_to_last[:-1]:
         spiral.append(i)
    
    print(spiral)

spiral_traverse([
                 [7, 2],
                 [5, 0]
                 ])
#[7, 2, 0, 5]


spiral_traverse([
                 [1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]
                 
                 ])
#[1, 2, 3, 6, 9, 8, 7, 4, 5]


spiral_traverse([
                 [1, 1, 1, 7],
                 [4, 5, 2, 9],
                 [3, 3, 2, 8]
                 ])
#[1, 1, 1, 7, 9, 8, 2, 3, 3, 4, 5, 2]


spiral_traverse([
                 [8, 5, 3, 2, 1, 6],
                 [6, 2, 9, 1, 4, 5],
                 [8, 4, 1, 5, 0, 4]
                 
                 ])
#[8, 5, 3, 2, 1, 6, 5, 4, 0, 5, 1, 4, 8, 6, 2, 9, 1, 4]

#----------------------------------------------------
#Write a function to find the smallest integer greater than zero which factorial is exactly divided by the number.
#If the number is prime then this function should return the number itself

def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

def prime(num):
    
    if num<=1:
        return False
    
    elif num==2:
        return True
    
    elif num>2:
        for i in range(2,num):
            if num%i==0:
                return False
            else:
                return True

def factorial_divided_by_number(number):
    if prime(number):
        return number
    else:
        for i in range(1,number+1):
            x=factorial(i)
            if x%number==0:
                return i

print(factorial_divided_by_number(8)) # 4
#1! = 1 % 8 !=0
#2! = 2 % 8 !=0
#3! = 6 % 8 !=0
#4! = 24 % 8 == 0 so we return 4

print(factorial_divided_by_number(6)) # 3

#1! = 1 % 6 !=0 0
#2! = 2 % 6 != 0
#3! = 6 % 6 == 0

print(factorial_divided_by_number(10)) # 5

#1! = 1 % 10 != 0
#2! = 2 % 10 != 0
#3! = 6 % 10 != 0
#4! = 24 % 10 != 0
#5! = 120 % 10 == 0

print(factorial_divided_by_number(2)) # 2 (prime)
print(factorial_divided_by_number(5)) # 5 (prime)

#----------------------------------------------------
# Make a stack calculator base on following instructions:
# +: Pop the last 2 values from the stack, add them, and push the result onto the stack
# -: Pop the last 2 values from the stack, subtract the lower one from the topmost one, and push the result
# *: Pop the last 2 values, multiply, and push the result
# /: Pop the last 2 values, divide the topmost one by the lower one, and push the result
# DUP: Duplicate the top value on the stack
# DOUBLE: top value *2
# POP: Pop the last value from the stack and discard it
# Whenever a number appears as an instruction. Push the number to the stack
# Any other instruction  should result in the value "Invalid Instructions"

def stack_calculator(stack,instruction):
    
    last=stack[len(stack)-1]
    second_last=stack[len(stack)-2]
    
    if instruction=="+":
        
        x=last+second_last
        stack.pop(len(stack)-1)
        stack.pop(len(stack)-1)
        stack.append(x)
        print(stack)

    elif instruction == "-":
        
        x = second_last - last
        stack.pop(len(stack) - 1)
        stack.pop(len(stack) - 1)
        stack.append(x)
        print(stack)

    elif instruction == "*":
        x = last * second_last
        stack.pop(len(stack) - 1)
        stack.pop(len(stack) - 1)
        stack.append(x)
        print(stack)
    
    elif instruction == "/":
        x = last / second_last
        stack.pop(len(stack) - 1)
        stack.pop(len(stack) - 1)
        stack.append(x)
        print(stack)

   elif instruction=="DUP":
        s.append(last)
        print(stack)
    
   elif instruction=="DOUBLE":
        d=last*2
        stack.pop(len(stack)-1)
        stack.append(d)
        print(stack)

   elif instruction=="POP":
        stack.pop()
        print(stack)
    
   elif instruction >= 0  or instruction<0:
        stack.append(instruction)
        print(stack)

   else:
        print("Invalid Instructions")

s=[1,2,3,4,5,6]

#stack_calculator(s,"+") # [1, 2, 3, 4, 11]

#stack_calculator(s,"-")# [1, 2, 3, 4, -1]

#stack_calculator(s,"*") # [1, 2, 3, 4, 30]

#stack_calculator(s,"/") # [1, 2, 3, 4, 1.2]

#stack_calculator(s,"DUP") # [1, 2, 3, 4, 5, 6, 6]

#stack_calculator(s,"DOUBLE") # [1, 2, 3, 4, 5, 12]

#stack_calculator(s,"POP") #[1, 2, 3, 4, 5]

#stack_calculator(s,10) #[1, 2, 3, 4, 5, 6, 10]

#We can ask the user to ceate a stack and chooses any instructions
size=int(input("Enter the size of stack:"))
stack=[]

for i in range(size):
    
    element=int(input("Enter a number:"))
    stack.append(element)

print("The user's stack is :",stack)

instruction=str(input("Enter an instruction:"))
stack_calculator(stack,instruction)

#----------------------------------------------------
#Write a function to determine if two triangles can fit into each other
#First triangle should be smaller than the second one

def does_fit_into_eachOther(arr1 ,arr2):
    a=[]
    result=[]
    for i in arr1:
        for j in arr2:
            a.append([i,j])

    for i in a:
        if i[0]<i[1]:
           result.append(True)
            
        else:
            result.append(False)

    if all(result)==True:
        return True
    else:
        return False

print(does_fit_into_eachOther([3, 3, 3], [3, 3, 3]))#False

print(does_fit_into_eachOther([2, 2, 2], [3, 3, 3]))#True

print(does_fit_into_eachOther([2, 3, 4], [2, 3, 2]))#False

print(does_fit_into_eachOther([1, 6, 5], [11, 7, 8]))#True

#----------------------------------------------------
#Start with any positive number. Add the number with the number formed by reversing its digits
#If the sum is palindrome return True
#Otherwise repeat the process 2 more times
#If after 2 times the palindrome is achieved then return True and also print the results otherwise return False

def palindrome(n):
    n=str(n)
    original=[i for i in n]
    a=[i for i in n]
    
    a.reverse()
    reversed=''.join(a)
    original=''.join(original)
    
    if original==reversed:
        return True
    else:
        return False

def palindrome_sum(number):
    if number <0:
        print("Number should be positive")
    else:    
        n = str(number)
        original = [i for i in n]
        a = [i for i in n]
        
        a.reverse()
        reversed = ''.join(a)
        original = ''.join(original)
        
        original=int(original)
        reversed=int(reversed)
        
        sum=original+reversed
        if palindrome(sum)==True:
            
            print(original, "+", reversed, "=", sum)
            return True
        else:     
            s = str(sum)
            original_sum = [i for i in s]
            r = [i for i in s]
            
            r.reverse()
            re = ''.join(r)
            original_sum = ''.join(original_sum)
            
            original_sum = int(original_sum)
            re = int(re)
            
            result=original_sum+re
            
            if palindrome(result):
                print(original_sum, "+", re, "=", result)
            else:    
                result = str(result)
                original_result = [i for i in result]
                result_re = [i for i in result]
                
                result_re.reverse()
                result_re = ''.join(result_re)
                original_result = ''.join(original_result)
                
                original_result = int(original_result)
                result_re = int(result_re)
                
                result2 = original_result + result_re
                
                if palindrome(result2):
                    print(original_sum, "+",re, "=", result)
                    print(original_result,"+",result_re,"=",result2)
                    return True
                else:
                    return False

print(palindrome_sum(61))#True
#61 + 16 = 77

print(palindrome_sum(97))#Fasle

print(palindrome_sum(38))#True
#38 + 83 = 121

print(palindrome_sum(348)) # True
#348+843 =1191 --> 1191+1911 =3102 --> 3102+2013 = 5115

print(palindrome_sum(295))#False
