# print all palindrome items from list 

l = [121, 785, 990, 131, 654, 161]
res=[]
for n in l:
    original = n
    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n = n // 10
    if original == reversed_num:
        print(original,end="  ")    # 121  131  161  
         
l=[121,785,990,131,654,161]
def palindrome(n):
    original = n
    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10
    return original == reversed_num
for num in l:
    if palindrome(num):
        print(num,end=" ")     # 121 131 161


# print all sum of pllindrome items from list 

l=[121,784,900,343,99,11,190]
def check_palindrome(num):
    temp=num
    rev=0
    while temp !=0:
        digit=temp%10
        rev=rev*10+digit
        temp=temp//10
    if rev==num:
        return True
def sum_palindrome(l) :
    res=[]
    for i in l :
        if check_palindrome(i):
            res.append(i)
    return sum(res)
print(sum_palindrome(l))    # 574 = 121+343+99+11

# print all prime num items from list 

l=[1,4,5,67,98,77,97,7,11]
def check_prime(n):
    if n<2:
        return False 
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
print("Prime numbers :")
for num in l:
    if check_prime(num):
        print(num,end=" ")    # Prime numbers : 5 67 97 7 11

l=[1,4,5,67,98,77,97,7,11]
def is_prime(num):
    if num<=1:
        return False
    sq_root=int(num**0.5)+1
    for i in range (2,sq_root):
        if num % i ==0:
            return False 
    return True
def get_prime(l):
    res=[]
    for i in l :
        if is_prime(i):
            res.append(i)      
    return res
print(get_prime(l))    # [5, 67, 97, 7, 11]

# print all sum of prime items from list 

l=[1,4,5,67,98,77,97,7,11]
def check_prime(num):
    if num<=1:
        return False
    sq_root=int(num**0.5)+1
    for i in range (2,sq_root):
        if num % i ==0:
            return False 
    return True
def sum_prime(l):
    prime_sum = 0
    for num in l:
        if check_prime(num):  
            prime_sum += num
    print("Sum of prime numbers :", prime_sum)
(sum_prime(l) )   # Sum of prime numbers : 187

# print all armstrong items from list

l = [4, 67, 98 , 97, 7, 11, 153, 370]
def is_armstrong(num):
    s = 0
    temp = num
    power = len(str(num))
    while temp != 0:
        digit = temp % 10
        s += digit ** power
        temp = temp // 10
    return s == num
print("Armstrong numbers in the list:")
for num in l:
    if is_armstrong(num):
        print(num,end=" ")    # Armstrong numbers in the list: 4 7 153 370

# print sum of armstrong items from list 
l = [4, 67, 98 , 97, 7, 11, 153, 370]
def is_armstrong(num):
    s = 0
    temp = num
    power = len(str(num))
    while temp != 0:
        digit = temp % 10
        s += digit ** power
        temp = temp // 10
    return s == num
def sum_armstrong (l):
    res=[]
    for i in l :
        if is_armstrong(i):
            res.append(i)
    return sum(res)
print("Sum of Armstrong numbers : ",sum_armstrong(l))     # Sum of Armstrong numbers : 534

# print count of palindrome items from list 
l=[121,785,990,131,654,161]
def palindrome(n):
    original = n
    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10
    return original == reversed_num
def count_palindrome(l):
    c = 0
    for i in l:
        if palindrome(i):
            c += 1
    return c
print("Count of palindrome numbers:", count_palindrome(l))    # Count of palindrome numbers: 3

# print count prime items from list 
l=[1,4,5,67,98,77,97,7,11]
def is_prime(num):
    if num<=1:
        return False
    sq_root=int(num**0.5)+1
    for i in range (2,sq_root):
        if num % i ==0:
            return False 
    return True
def count_prime(l):
    c = 0
    for i in l:
        if is_prime(i):
            c += 1
    return c
print("Count of prime numbers:", count_prime(l))   # Count of prime numbers: 5

# print count of armstrong items from list
l = [4, 67, 98 , 97, 7, 11, 153, 370]
def is_armstrong(num):
    s = 0
    temp = num
    power = len(str(num))
    while temp != 0:
        digit = temp % 10
        s += digit ** power
        temp = temp // 10
    return s == num
def count_armstrong(l):
    c = 0
    for i in l:
        if is_armstrong(i):
            c += 1
    return c
print("Count of armstrong numbers:", count_armstrong(l))    # Count of armstrong numbers: 4

# wap to count how many even digits are present in number using while loop

num = 45678
def count_even_digits(num):
    count = 0
    temp = num
    while temp > 0:
        digit = temp % 10    #digit = temp % 10 = 8 (last digit)
        if digit % 2 == 0:
            count += 1
        temp = temp // 10    # temp = temp // 10 = 4567 (drops the 8)
    return count
print("Count of even digits:", count_even_digits(num))    # Count of even digits: 3
 