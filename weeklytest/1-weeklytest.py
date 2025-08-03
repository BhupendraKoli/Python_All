
# Q1. What is Python? What are the benefits of using Python.
'''
1 Python  has simple and clear synstax
2 python is an interprete lang 
   Python is called an interpreted language because it executes code logic directly, line by line, without the need for a separate compilation step
3 python is dynamically typed lang
    In Python, "dynamically typed" refers to the fact that the type of a variable is determined at runtime, not when the code is compiled or written
4 python is open source 
5 python is object oriende lang
   class and object 
6 python has rich eco system and lib      
7 python is high level lang
    easy to read and write
8 python is garbage collection lang
     Garbage collection is Python's way of automatically managing memory, ensuring that your applications runs smoothly by freeing up memory that is no longer in use.
9 python is platfrom independetd lang 
     In Python, a platform-independent programming language means that the same Python code can be executed on different operating systems (like Windows, macOS, and Linux) without requiring any changes or recompilation            
 Benefits of Python:
Easy to learn and use
Large standard library
Cross-platform compatibility
Strong community support
Wide range of applications (web, data science, AI, etc.)
'''
# Q2. What is difference between == and is? 
'''
== checks value equality (whether two variables have the same value).
is checks identity (whether two variables point to the same object in memory)
'''
# Q3. Write the 5 features of python in details.
'''
1. Simple and clear syntax
Python's syntax is designed to be easy to read and write, making it a great language for
beginners and experienced programmers alike.
2. Interpreted language
Python code is executed line by line, without the need for a separate compilation step.
3. Dynamically typed language
Python is dynamically typed, which means that the type of a variable is determined at runtime, not wh
en the code is compiled or written.
4. Open source language
Python is open source, which means that it is free to use, modify, and distribute.
5. Object-oriented language
Python is an object-oriented language, which means that it organizes code using objects and classes.
'''
#Q4. "==" is which type of operator?
'''
== is a comparison (relational) operator.
It checks if two values are equal.
'''
#Q5. What is logical operators?
'''
and: Returns True if both conditions are True
or: Returns True if at least one condition is True
not: Reverses the result (True becomes False, and vice versa)
'''
#Q6. What is Conditional statement?
'''
If-else statement is used to execute different blocks of code based on a condition.
The condition is a boolean expression that can be either true or false.
Conditional statements allow the program to make decisions and execute certain parts of code based on conditions.
'''
# Q7. Describe if,elif and else statement.
'''
if: Used to execute a block of code if a condition is true.
elif: Used to execute a block of code if the initial condition is false and the next condition is
true.
else: Used to execute a block of code if all conditions are false.
'''


#Q8. What is Membership operators?
'''
in: Returns True if a value is found in a sequence (like a list, tuple, or string).
not in: Returns True if a value is not found in a sequence.
'''

 
#Q9. What are variables in Python.
'''
Variables are used to store values in Python. They are essentially labels that we assign to a value so
that we can refer to that value later in the code.
'''

#Q10. What is the purpose of f-string?
'''
f-strings (formatted string literals) make string formatting easier and more readable.
The purpose of f-string is to insert the value of a variable into a string. It is a
formatted string literal that allows you to embed expressions inside string literals.
'''
# CODE FOR THE GIVEN QUESTIONS 

# Q1 WAP and Take 10 input from user and print average.
num1=int(input("enter the number1 :-"))
num2=int(input("enter the number2:-"))
num3=int(input("enter the number3:-"))
num4=int(input("enter the number4:-"))
num5=int(input("enter the number5:-"))
num6=int(input("enter the number6:-"))
num7=int(input("enter the number7:-"))
num8=int(input("enter the number8:-"))
num9=int(input("enter the number9:-")) 
num10=int(input("enter the number10:-"))
average=(num1+num2+num3+num4+num5+num6+num7+num8+num9+num10)
print("the averge is ",average/10)
# Q2 Bmi cal
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))
# Calculate BMI
bmi = weight / (height ** 2)
# Print BMI
print(f"Your BMI is: {bmi:.2f}")
# Determine weight status
if bmi < 18.5:
    print("Weight Status: Underweight")
elif 18.5 <= bmi < 25:
    print("Weight Status: Normal weight")
elif 25 <= bmi < 30:
    print("Weight Status: Overweight")
else:
    print("Weight Status: Obese")

# Q3  Leap Year Checker
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# Q5 arothomatic op
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print("Addition of the Two Number Is ",num1+num2)
print("Subtraction of the Two Number Is ",num1-num2)
print("Multiplication of the Two Number Is ",num1*num2)
print("Division of the Two Number Is ",num1/num2)
print("Division of the Two Number Is ",num1%num2)
print("Division of the Two Number Is ",num1//num2)
# Q6  insurance of people
age=int(input("Enter the Age of the person "))
status=str(input("enter the married status "))
if status == "married" and age > 30:
    print("the person is married and above 30 is eligible for the insurance")
else:
    print("the person is not eligible for the insurance")

# Q7 Write a Python program that declares two variables, x and y, and swaps their values using a third variable.
x = 4
y = 8
print("Value of x Befor swapping: ", x)
print("Value of y Befor  swapping: ", y)
temp = x
x = y
y = temp
print("Value of x after swapping: ", x)
print("Value of y after swapping: ", y)

# Q8 Write a Python program to determine if a given number is positive, negative, or zero.
num = int(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
elif num == 0:
    print("The number is zero.")
else:
    print("The number is negative.")

#Q9. Write a program to take two integer inputs from user and print sum and product of them.
num1=int(input("enter the firts number "))
num2=int(input("enter the second number "))
print("Sum of the two number is ",num1+num2)
print("Product of the two number is ",num1*num2)

#Q10.Find the largest number of three numbers using conditionals statements.
num1=int(input("enter the first number "))
num2=int(input("enter the second number "))
num3=int(input("enter the third number "))
if num1> num2 and num1 > num3:
    print(num1,"is the largest number")
elif num2 > num1 and num2 > num3 :
    print(num2,"is the largest number")
else:
  print(num3,"is the largest number")


# ERROR CHECKED QUPESTIONS AND ANSWER 

'''
Q1.

a = 10  
b = 3  
result = a ***/ b  
print(result)


Q2.

   number = 12
   if number > 10
   print("Greater than 10")
   elif number == 10
       print("Equal to 10")
   else:
       print("Less than 10")


Q3.
 
 a = 5
   b = 10
   print(fSum of a and b is: {a + b}")


Q4. 

x = "10"
   y = 5
   print(x + y)


Q5.

name = "Alice"  
age = 25  
print(f"Hello, my name is {name and I am {age} years old.")


Q6.

age = 18  
if age >= 18:  
print("You are eligible to vote.")  


Q7.

num = 10  
if num > 10:  
    print("Greater than 10")  
elif num < 10:  
    print("Less than 10")  
else num == 10:  
    print("Equal to 10")


Q8.

age = 25
print("I am " + age + " years old.")


Q9.

print(message)
message = "This is a test message."


Q10.

num = 10  
if num = 10:  
    print("Number is ten.")





'''
#Q 1
a = 10  
b = 3  
result = a ** b  
print(result)
# Q2
number = 12
if number > 10 :
    print("Greater than 10")
elif number == 10:
       print("Equal to 10")
else:
       print("Less than 10")

# Q3
a = 5
b = 10
print ((f"Sum of a and b is: {a + b}"))
# Q4
x = 10
y = 5
print(x+y)
# Q5
name = "Alice"  
age = 25  
print(f"Hello, my name is {name} and I am {age} years old.")
# Q6
age = 18  
if age >= 18:  
 print("You are eligible to vote.") 
else:
     print("You are not eligible to vote.")
#Q7
num = 10  
if num > 10:  
    print("Greater than 10")  
elif num < 10:  
    print("Less than 10")  
else:  
    print("Equal to 10")
#Q8
age = 25
print(f"I am  {age} years old.")
#Q9
message = "This is a test message."
print(message)
#Q10
num = 10  
if num == 10:  
    print("Number is ten.")
  

