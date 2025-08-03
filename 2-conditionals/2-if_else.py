'''
syntax 
if condition 
# code to be executed if condition is true
else:
# code to be executed if condition is false
'''
a=int(input("enter the number "))
if a%2==0:
    print("a is even")
else:
 print("a is odd")

# if given nummber is divisible by or not 
 number = int(input("Enter a number: "))

if number % 5 == 0:
  print(f"{number} is divisible by 5")
else:
  print(f"{number} is not divisible by 5")

number = int(input("Enter a number: "))
# chech the  given number is dividsible by 5 and 10 
if number % 5 == 0 and number %10==0:
  print(f"{number} is divisible by 5 and 10")
else:
  print(f"{number} is not divisible by 5 and 10 ")  