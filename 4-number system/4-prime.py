# prime number 
#A prime number is a number greater than 1 that has no divisors other than 1 and itself.

num = int(input("Enter a number: "))
flag = 0  # Assume number is prime (no divisors found yet)

if num <= 1:
    flag = 1  # Not prime if 1 or below
else:
    for i in range(2, num):
        if num % i == 0:
            flag = 1  # Found a divisor, so not prime
            break

# Final result based on flag
if flag == 0:
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")






num=int(input("enter the number "))
flag=True
i=2

if num <= 1:
    flag=False
while i< num :
    if num % i == 0 :
        flag=False
    i=i+1

if flag:
    print("the number is prime number ")
else:
    print("the number is not prime number ")

# find the prime number in spefice range 
start=int(input("enter the number"))
end=int(input("enter the number "))  
while start<=end:
    flag=True
    i=2

    if start<=1:
        flag=False
    while i < start :
        if start % i== 0:
            flag=False
        i=i+1
    if flag:
        print(start,end=" ")  
    start=start+1             

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
print(f"Prime numbers between {start} and {end} are:")
while start <= end:
    if start > 1:  # Prime numbers are greater than 1
        i = 2
        is_prime = True
        while i * i <= start:
            if start % i == 0:
                is_prime = False
                break
            i += 1
        if is_prime:
            print(start, end=" ")
    start += 1
