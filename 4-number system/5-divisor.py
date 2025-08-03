
# num=int(input("enter the number"))
# for i in range(1,num):
#     if num%i==0:
#         print(i,end=" ")

 # prefect number 
# num1=int(input("Enter the Number "))
# sum=0
# for i in range(1,num1):
#     if num1 %i==0:
#       sum += i
# if sum==num1:
#     print(num1,"is prefect number")
# else:
#     print(num1," is not prefect ")    

# Abundant number 
# A number is said to be abundant if the sum of its proper divisors is greater than the number exculeding it self 
num=int(input("Enter the number"))
sum=0
for i in range(1,num):
    if num % i == 0:
        sum += i
if sum>num:
     print(num,"is abundant number")
elif sum==num:
     print(num,"is prefect number")
else:
     print(num,"is not abundantabd & prefect  number")

# Defficient number 
# A number is said to be deficient if the sum of its proper divisors is less than the number
num=int(input("Enter the number"))
sum=0
for i in range(1,num):
     if num % i == 0:
          sum += i
if sum<num:
     print(num,"is deficient number") 
if sum>num:
     print(num,"is abundant number")
elif sum==num:
     print(num,"is prefect number")
else:
     print(num,"is not deficient & prefect number")


