# Recurrsion:
'''
When a function call itself till certain condition.

'''
# Factorial:
'''
5!=1*2*3*4*5=120

4!=1*2*3*4=24

'''

# num=int(input("Enter a number: "))

# fac=1

# for i in range(1,num+1):
#     fac=fac*i
# print(fac)    #120

# # Will perform by recurrsion function:

# def fac(n):
#     if n==1:
#         return 1
#     else:
#         return n*fac(n-1)
    
# print(fac(5))   #120

'''
n=5

5* fac(5-1)

5*4 fac(4-1)

5*4*3 fac(3-1)

5*4*3*2 fac(2-1)

5*4*3*2*1======120

'''

# WAP of sum of digits of a number by using recurrsion.

# def sum_of_digit(num):
#     if num==0:
#         return 0
#     else:
#         digit=num%10
#         return digit + sum_of_digit(num//10)
    
# print(sum_of_digit(123))
    
# '''
# num       digit        sum_of_digit(num//10)

# 123        3            3+ sum_of_digit(123//10)
# 12         2            3+2+ sum_of_digit(12//10)
# 1          1            3+2+1 sum_of_digit(1//10)
# 0          0             6

# '''

# # You need to print the reverse of a number by using recurrsion.

# def reverse(num,rev=0):
#     if num==0:
#         return rev
#     else:
#         digit=num%10
#         rev=rev*10+digit
#         return reverse(num//10,rev)
# print(reverse(12345))
# #54321
# #  
# '''
# num      digit    rev                  updated
# 121       1       rev=1                 121//10=12
# 12        2       rev=1*10+2            reverse(12//10,12)
# 1         1       rev=12*10+1=121       reverse(1//10,121)

# '''
# l=[[1,2,1,4],[4,5,6]]

# # You have to flatten a list.
# output=[1,2,1,4,4,5,6]

# l=[[1,2,1,4],[4,5,6]]

# flatten=[]

# for i in l:
#     for item in i:
#         flatten.append(item)
# print(flatten)

# # [1, 2, 1, 4, 4, 5, 6]      

# # l=[12,3,4,5,[3,5,6],6,7,[2,6,7,[7,8,9],8]]

# l=[12,3,4,5,[3,5,6],6,7,[2,6,7,[7,8,9],8]]

# def flatten(l):
#     res=[]

#     for i in l:
#         if isinstance(i,list):
#             res.extend(flatten(i))
#         else:
#             res.append(i)
    
#     return res
# print(flatten(l))

# output: [12, 3, 4, 5, 3, 5, 6, 6, 7, 2, 6, 7, 7, 8, 9, 8]

#####  TASK   ######

# 1. WAP print all the palindrone items from a list.
# Without function

# list1=[121,785,990,545,131,654,161]

# res=[]
# for i in list1:
#     num=i
#     temp=num
   
#     rev=0

#     while temp!=0:
#         digit=temp%10
#         rev=rev*10+digit
#         temp=temp//10

#     if rev==num:
#         res.append(num)

# print(res)
# output: [121, 545, 131, 161]

# WAP to print all the sum of palindrone items from list:

l=[121,784,900,343,99,11,190]

def check_palindrone(num):
    temp=num
    rev=0

    while temp !=0:
        digit=temp%10
        rev=rev*10+digit
        temp=temp//10
    if rev==num:
        return True
    
def sum_palindrone(l):
    res=[]
    for i in l:
        if check_palindrone(i):
            res.append(i)
    return sum(res)
print(sum_palindrone(l))

# output: 121+343+99+11=574

# WAP print all the prime items from the list:

list1=[1,4,5,67,98,77,97,7,11]

def is_prime(num):
    if num <=1:
        return False
    max_div=(int(num**0.5))+1
    for i in range(2,max_div):
        if num % i==0:
            return False
    return True

def get_prime(list1):
    res=[]
    for j in list1:
       if  is_prime(j):
           res.append(j)
    
    return res

list1=[1,4,5,67,98,77,97,7,11]
print(get_prime(list1))
# output: [5, 67, 97, 7, 11]

# WAP print all the sum of prime items from the list.

list1=[1,4,5,67,98,77,97,7,11]

def is_prime(num):
    if num <=1:
        return False
    max_div=(int(num**0.5))+1
    for i in range(2,max_div):
        if num % i==0:
            return False
        return True
    
def sum_of_prime(list1):
    res=[]
    for j in list1:
        if is_prime(j):
            res.append(j)
    return sum(res)

list1=[1,4,5,67,98,77,97,7,11]
print(sum_of_prime(list1))
# output: 5+67+97+7+11=264

# WAP print all the armstrong items from a list.
l=[4,67,98,7,11,153,370]

def armstrong(num):
    temp=num
    sum=0
    power=len(str(num))
   
    while temp!=0:
        digit=temp%10
        sum=sum+digit**power
        temp=temp//10
    return sum==num
print("Armstrong numbers in the list:")
for num in l:
    if armstrong(num):
        print(num,end=" ")

# output: Armstrong numbers in the list: 4 7 153 370 

# WAP to print all the sum of Armstrong items from the list.

l=[4,67,98,7,11,153,370]

def armstrong(num):
    temp=num
    sum=0
    power=len(str(num))
   
    while temp!=0:
        digit=temp%10
        sum=sum+digit**power
        temp=temp//10
    return sum==num
print("Sum of Armstrong numbers in the list:")

def sum_armstrong(l):
    res=[]
    for j in l:
        if armstrong(j):
            res.append(j)
    return sum(res)

l=[4,67,98,7,11,153,370]
print(sum_armstrong(l))
    
# output: Sum of Armstrong numbers in the list: 4+7+153+370= 534

# WAP print the count of palindrone items from the list.

l=[121,784,900,343,99,11,190]

def check_palindrone(num):
    temp=num
    rev=0

    while temp !=0:
        digit=temp%10
        rev=rev*10+digit
        temp=temp//10

    return num==rev
    
def count_palindrone(l):
    res=[]
    for i in l:
        if check_palindrone(i):
            res.append(i)
    return len(res)

print("Count of palindrone numbers: ",count_palindrone(l))
# output:Count of palindrone numbers:  4

# WAP to print count of prime items from the list.

list1=[1,4,5,67,98,77,97,7,11]

def is_prime(num):
    if num <=1:
        return False
    max_div=(int(num**0.5))+1
    for i in range(2,max_div):
        if num % i==0:
            return False
        return True
    
def count_prime(list1):
    res=[]
    for i in list1:
        if is_prime(i):
            res.append(i)
    return len(res)

print("Count of prime numbers: ",count_prime(list1))
# output:Count of prime numbers: 6

# WAP print the count of Armstrong items from the list

l=[4,67,98,7,11,153,370]

def armstrong(num):
    temp=num
    sum=0
    power=len(str(num))
   
    while temp!=0:
        digit=temp%10
        sum=sum+digit**power
        temp=temp//10
    return sum==num

def count_armstrong(l):
    res=[]
    for i in l:
        if armstrong(i):
            res.append(i)
    return len(res)

print("Count of armstrong numbers: ",count_armstrong(l))
# output:Count of armstrong numbers: 4

# WAP to count how many even digits are present
# in a given number using a while loop
num=45678

def count_even_digits(num):
    count=0
    temp=num

    while temp > 0:
        digit=temp%10
        if digit%2==0:
            count=count+1
        temp=temp//10
    return count
print("count of all even numbers is: ",count_even_digits(num))
# output: count of all even numbers is: 3




    





