# nesteed conditional 
'''
nested if statment is when we create on if statement inside another 

if the first if block is true than the second if block is run 
if the first if block is false than the second if block is not run


'''
# example of nested if statement
# find the greatest number of  3 no using nested if else
num1 = int(input("enter the first number "))
num2 = int(input("enter the second number "))
num3 = int(input("enter the third number "))

if num1 > num2:
    if num1 > num3:
        print(f"{num1}is the greatest number")
    else:
         print(f"{num3}is the greatest number")
else:
     if num2 >num3:
      print(f"{num2}is the greatest number")
     else:
       print(f"{num3}is the greatest number")
# find the small  number of  3 no using nested if else
if num1 < num2:
    if num1 < num3:
        print(f"{num1}is the small number")
    else:
         print(f"{num3}is the small number")
else:
     if num2 <num3:
      print(f"{num2}is the small number")
     else:
       print(f"{num3}is the small number")

#wap and check if student is pass or not 
# #if pass check he is in class topper list 
# Define the pass mark
pass_mark = 40
name = input("Enter student name: ")
marks = int(input("Enter student's marks: "))

topper_list = ["Mansi", "Rohini", "Prathamesh","aadity","ganesh", "mahendra50"
]

if marks >= pass_mark: 
    print(f"{name} has passed the exam.")
    if name in topper_list:
        print(f"{name} is also in the class topper list.")
    else:
        print(f"{name} is not in the class topper list.")
else:
    print(f"{name} has failed the exam.")

#find the middle number of three number 
a=int(input("enter the number"))
b=int(input("enter the number"))
c=int(input("enter the number"))
if a>b:
    if a>c:
        print(f"{a}is the middle number")
    elif b>c:
        print(f"{b}is the middle number")
    else:
        print(f"{c}is the middle number")
else:
  if a>c:
    print(f"the {a}is middle ")
  elif b<c:
    print(f"the {b}is middle ")
  else:
    print(f"the {c}is middle ")

  #leap year 
  # if year is divisible by 4 then it is leap year
  # but year is not divisible by 100 then it is a leap year
  # except year is divisible by 400 then it is a leap year
  
year=int(input("enter the year"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
    else:
        print(f"{year} is a leap year")
else:
 print(f"{year} is not a leap year")

# Q1) Check the temprature given by user is for which season
    #  (spring(15-30 °C), summer(30+ °C), autumn(0-10 °C), and winter( 10–15 °C))

temperature = float(input("Enter the temperature in °C: "))

if 15 < temperature <= 30:
    print("Season: Spring")
elif temperature > 30:
    print("Season: Summer")
elif 0 <= temperature <= 10:
    print("Season: Autumn")
elif 10 < temperature <= 15:
    print("Season: Winter")
else:
    print("Invalid temperature or out of range.")

# Q2) Wap to Take values of length and breadth of a rectangle from user and check if it is square or not.
length = float(input("Enter the length : "))
breadth = float(input("Enter the breadth : "))
if length == breadth:
    print("It is a square.")
else:
 print("It is rectangle.")
#Q3) Alice is trying to find a no which is non negative and even and divisible by 3 given by Alice .
# Alice is trying to find a number which is non-negative, even, and divisible by 3

number = int(input("Alice, enter a number: "))

if number >= 0:
    if number % 2 == 0:
        if number % 3 == 0:
            print("The number is non-negative, even, and divisible by 3.")
        else:
            print("The number is non-negative and even but not divisible by 3.")
    else:
        print("The number is non-negative but not even.")
else:
    print("The number is negative.")


#Q4) Write a program to print Yes if no which is odd and between 10 to 15 and divisible by 4 given by user
number = int(input("Enter a number: "))

if 10 < number < 15:
    if number % 2 != 0 :
     
     if number % 4 == 0:
       print("Yes")
     else:
      print("No")
       
else:
    print("No")

#Q5) Write a program to check the input nos. given by Jeff and Bob are same or not for same "Won" else "Lost"

jeff = input("Enter the result of Jeff: ")
bob = input("Enter the result of Bob: ")
if jeff == bob:
   print("Won")
else:
    print("Lost")

# Q6) Create a program using nested if-else where the player chooses between "tea" or "coffee," 
    #  and then chooses "hot" or "cold" to get a final drink suggestion.

drink = input("Do you want tea or coffee? ")
temperature = input("Do you want it hot or cold? ")
if drink == "tea":
   if temperature == "hot":
      print("You should have a hot tea.")
   elif temperature == "cold":
     print("You should have a cold tea.")
else:
  if temperature == "hot":
   print("You should have a hot coffee.")
  elif temperature == "cold":
     print("You should have a cold coffee.")

   
