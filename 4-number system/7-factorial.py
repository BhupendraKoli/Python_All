# factorial number
# The factorial of a number is the product of all positive integers from 1 up to n  that number.
# For example, the factorial of 5 is 5*4*3*2*1
# 5! = 5*4*3*2*1 = 120
# 6! = 6*5*4*3*2*1 = 720
num=int(input("enter the number "))
fact=1
for i in range(1,num+1):
    fact=fact*i
print("factorial of",num,"is",fact)

num=int(input("enter the number "))
fact=1
i=1
while i <= num:
    fact=fact*i
    i=i+1
print("factorial of",num,"is",fact)

# strong number
# A strong number is the number which is the sum of the cube of its digit is equal to
# the number itself. For example, 1634 is a strong number since 1*1 
# *1 + 6*6*6 + 3*3*3 + 4
# *4*4 = 1634
'''
a number in which sum of factorical of its digits is equal ti given number 
for example 145 is a strong number
1!+4!+5!=1+24+120=145
krishanmurthy,perterson,stong number is same 

'''
num=int(input("enter the number "))
sum=0
temp=num
while temp != 0 :
    digit = temp % 10
    fac=1
    for i in range(1,digit+1):
        fac=fac*i
    sum=sum+fac
    temp = temp // 10

if sum==num:
    print(num,"is a strong number")
else:
    print(num,"is not a strong number")


#spy number 
# A spy number is a number whose sum of digits is equal to the product of its digits
# For example, 123 is a spy number since 1+2+3 = 6
# and 1*2*3 = 6

num = int(input("Enter a number: "))
sum = 0
product = 1

temp = num
while temp > 0:
    digit = temp % 10 
    sum += digit
    product *= digit
    temp //= 10
if sum == product:
    print(num, "is a Spy Number.")
else:
    print(num, "is not a Spy Number.")
