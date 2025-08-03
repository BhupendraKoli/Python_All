# Section A: Theory (10 Questions)
'''
# 1-What are Python datatypes? Explain some common datatypes with examples.
#Ans:

Python Data types are the classification or categorization of data items. 
It represents the kind of value that tells what operations can be performed on a particular data.
 Since everything is an object in Python programming, Python data types are classes and variables are instances 
 (objects) of these classes. The following are the standard or built-in data types in Python:

Numeric - int, float, complex
Sequence Type - string, list, tuple
Mapping Type - dict
Boolean - bool
Set Type - set, frozenset
1.Numeric Data Types in Python
The numeric data type in Python represents the data that has a numeric value. A numeric value can be an integer, a floating number, or even a complex number. These values are defined as Python int, Python float and Python complex classes in Python.

Integers - This value is represented by int class. It contains positive or negative whole numbers (without fractions or decimals). In Python, there is no limit to how long an integer value can be.
Float - This value is represented by the float class. It is a real number with a floating-point representation. It is specified by a decimal point. Optionally, the character e or E followed by a positive or negative integer may be appended to specify scientific notation.
Complex Numbers - A complex number is represented by a complex class. It is specified as (real part) + (imaginary part)j . For example - 2+3j

2.Sequence Data Types in Python
The sequence Data Type in Python is the ordered collection of similar or different Python data types. Sequences allow storing of multiple values in an organized and efficient fashion. There are several sequence data types of Python:

Python String
Python List
Python Tuple

# 2-Explain the difference between mutable and immutable datatypes in Python.
#Ans:

 	Mutable                                                                          	Immutable
Definition	Data type whose values can be changed after creation.	Data types whose values can’t be changed or altered.
Memory Location	Retains the same memory location even after the
 content is modified.	                                            Any modification results in a new object and new memory location
Example	List, Dictionaries, Set	Strings, Types, Integer
Performance	It is memory-efficient, as no new objects are 
created for frequent changes.	                                    It might be faster in some scenarios as there’s no need to track changes.
Thread-Safety	Not inherently thread-safe.
 Concurrent modification can lead to unpredictable results.        	They are inherently thread-safe due to their unchangeable nature.
Use-cases	When you need to modify, add, or remove
 existing data frequently.	                                        When you want to ensure data remains consistent and unaltered.

# 3-What is the difference between a list and a tuple in Python? Give examples.
#Ans:
List:

list is a collection hetrogeneous data 
list is indexed and ordered
list is sequence data type that cantion all data types 
list is mutable (changeing modify the list )
allow duplicatis value 
list are created using square brackets [] or the list() function 
ex:
a = [10, 20, "GfG", 40, True]

print(a)

Tuple:
tuple :- sequence data type 
it is ordered and unchangeable.
tuple is collection of hetrogeneous data 
tuple is enclosed in round brackets ()
tuple is immutable means it cannot be changed after it is created.  

allow duplicats 
immutable 
Ex:
tup = (10, 20, 30) 

print(tup)
print(type(tup))

# 4-What is difference between Index and Find in String?
#Ans:

Both methods are used to locate the position of a substring within a string but the major difference between 
find() and index() methods in Python is how they handle cases when the substring is not found.
The find() method returns -1 in such cases, while index() method raises a ValueError.

# 5-What is the purpose of the break and continue statements in Python? Provide examples.
#Ans:
Break Statement in Python
The break statement in Python is used to exit or “break” out of a loop (either a for or while loop) prematurely, 
before the loop has iterated through all its items or reached its condition. When the break statement is executed, 
the program immediately exits the loop, and the control moves to the next line of code after the loop.
Ex:

for i in range(1,6):
    if i==3:
        break
    print(i,end=" ")
    
Continue Statement in Python
Python Continue statement is a loop control statement that forces to execute the next iteration of the loop while 
skipping the rest of the code inside the loop for the current iteration only, i.e. when the continue statement is executed in the loop, the code inside the loop following
the continue statement will be skipped for the current iteration and the next iteration of the loop will begin.
Ex:
for i in range(1,6):
    if i==4:
         continue
         print(i,end=" ")
# 6-What is the use of the in operator in Python? Explain with an example.
#Ans:
Operators: Special symbols use to perform some operations.
 a + b : + operator ; a,b operands; (a+b) operation.
Types:
1- Arithmetic Operators  (+,-,*,/,%,//,**)

2- Assignments Operators (=,+=,-=,*=,/=,%=,//=,**=)

3- Comparsion Operators  (<,>,<=,>=,==,!=)

4- Logical Operators     (and , or , not)

5- Membership Operators  (in , not in)

6- Identity Operators    (is, is not)

7- Bitwise Operators      (&,|,~,^,<<,>>)

# 7-Define loops in Python. What is the difference between for loop and while loop?
#Ans:
# loops are used to execute a block of code repeatedly for a specified number of times
# there are two types of loops in python
# 1. for loop
# 2. while loop
# for loop is used to iterate over a sequence (such as a list, tuple, dictionary,
#  set, etc.) and execute a block of code for each item in the sequence

# 8-What is Deep copy and Shallow copy? Brief it.
#Ans:
Shallow Copy:
Copies the object's structure but not the data within nested objects. 
Nested objects in the copy point to the same memory locations as the original. 
Changes to nested objects in either the original or the copy will affect the other. 
Generally faster and uses less memory than deep copy. 

Deep Copy:
Creates a completely independent copy of the object and all nested objects. 
Each nested object in the copy has its own memory location, separate from the original. 
Changes to nested objects in the copy will not affect the original object. 
More time-consuming and memory-intensive than shallow copy

# 9-How can you use an else clause with loops in Python? Provide an example.
#Ans:
n Python, an else clause can be used with both for and while loops. The key characteristic of this else clause is that it executes only if the loop completes all its iterations without encountering a break statement.
Example with a for loop:
Python

#  1: Loop completes normally
for i in range(5):
    print(i)
else:
    print("Loop finished without a break.")

print("-" * 20)

#  2: Loop is terminated by a break
for i in range(5):
    if i == 3:
        print("Breaking the loop at 3.")
        break
    print(i)
else:
    print("This message will not be printed because of the break.")

# 10-What is the importance of indentation in Python for conditional statements and loops?
#Ans:
dentation is a fundamental concept in Python programming language. It is the consistent use of whitespace (spaces or tabs) to define the scope and structure of code blocks. In Python, indentation plays a crucial role in determining the logical grouping of statements, unlike other programming languages where curly braces or keywords are used to define code blocks.

The Importance of Indentation
Indentation in Python serves several important purposes:

Code Readability: Proper indentation makes the code more readable and easier to understand, as it visually represents the hierarchical structure of the program.

Logical Grouping: Indentation is used to group related statements together, such as the body of a function, a loop, or a conditional statement.

Scope Definition: The level of indentation determines the scope of variables, functions, and other program elements. Statements with the same level
of indentation belong to the same scope.

Syntax Enforcement: Python's syntax relies heavily on indentation, and improper indentation can lead to syntax errors. The interpreter uses indentation to determine the structure of the code
'''

# Section B: Correct the Code (10 Questions)

# 1)
#    x = 10
# for i in range(x):
#        if i % 2 == 0:
#     continue
#        print(i)

#Ans:
x = 10
for i in range(x):
       if i % 2 == 0:
        continue
       print(i)

# 2)

# fruits = ["apple", "banana", "cherry"]
# print(fruits[3])

#Ans:

fruits = ["apple", "banana", "cherry"]
print(fruits[2])

# 3)
# a = 10
# b = 5
# if a > b:
#     print("a is greater than b")
# else:
#   print("b is greater than a")

#Ans:

a = 10
b = 5
if a > b:
    print("a is greater than b")
else:
  print("a is not grater than b")

# 4)
# a = [1, 2]
# b = [3, 4]
# a + b.append(5)
# print(a)

#Ans:

a = [1, 2]
b = [3, 4]
res=(a + b).append(5)
print(a)

# 5)
# for i in range(1, 6)
#          print(i)
        
#Ans:

for i in range(1, 6):
         print(i)


# 6)
# while True:
#     num = int(input("Enter a number (0 to stop): "))
#     if num == 0:
#         break
#    print(f"You entered: {num}")

#Ans:

while True:
    num = int(input("Enter a number : "))
    if num == 0:
        break
        print(f"You entered: {num}")



# 7)
# x = 10
# if x > 5:
#     print("x is greater than 5")
# elif x == 5:
#     print("x is equal to 5")
# else:
#     print("x is less than 5")

#Ans:

x = 10
if x < 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")


# 8)
# items = ["pen", "pencil", "eraser"]
# items.remove(2)
# print(items)

# #Ans

items = ["pen", "pencil", "eraser"]
s=items.remove("eraser")
print(items)

# 9)
# tup = (10, 20, 30)
# tup[1] = 25
# print(tup)

#Ans:

tup = (10, 20, 30)
tup = 25
print(tup)


# 10)
# x = [2, 4, 6]
# for i in x:
#     if i == 4:
#         continue
#              print(i)
        
# #Ans:
                                                                  
for i in range(2,4,6):
    if i == 4:
        continue
        print(i)


# Section C: Write Code For (10 Questions) 

# 1- Write a Python program to demonstrate the use of different datatypes (int, float, list, tuple, etc.).

# Integer (int): Whole numbers
my_integer = 10
print(f"Integer: {my_integer}, Type: {type(my_integer)}")

# Float (float): Numbers with a decimal point
my_float = 3.14
print(f"Float: {my_float}, Type: {type(my_float)}")

# List (list): Ordered, mutable collection of items
my_list = [1, 2, "three", 4.0]
print(f"List: {my_list}, Type: {type(my_list)}")
my_list.append("five") 
print(f"List after append: {my_list}")

# Tuple (tuple): Ordered, immutable collection of items
my_tuple = (10, 20, "thirty")
print(f"Tuple: {my_tuple}, Type: {type(my_tuple)}")

# 2- WAP to print the count  all even  items from the list.

l=[10,20,30,40,50,60]

count=len(l)
print(count)

# 3- Write a Python program that finds the largest of three numbers using if-elif-else.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
if num1 > num2 and num1 > num3:
    print(F"{num1}is gretaer than nmu2 and num3")
elif num2 > num3:
    print(F"{num2}is gretaer than nmu1 and num3")
else:
 print(F"{num3}is gretaer than nmu1 and num2")

# 4- WAP print all the Palindrome number from the list.

num=int(input("enter the number "))
temp=num
rev=0
while temp !=0:
    rem=temp%10
    rev=rev*10+rem
    temp=temp//10
if num==rev:
    print(num,"is a palindrome number")
else:
   print(num,"is not a palindrome number")

# 5- Create a dictionary from two lists.

list1=[1,2,3,4,5]
list2=["jeh","virat","lina","komal","mariya"]

d={}
for i in range(len(list1)):
    d[list1[i]]=list2[i]
print(d)

# 6-Write a Python program that asks the user to enter a number, and keep entering numbers until they enter 0.

while True:
    num = int(input("Enter a number : "))
    if num == 0:
        break
        print(f"You entered: {num}")

# 7-Write a Python program to combine two dictionary by adding values for common keys.

d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}
combined_dict = {}
for key, value in d1.items():
    combined_dict[key] = value
for key, value in d2.items():
    if key in combined_dict:
        combined_dict[key] += value
    else:
        combined_dict[key] = value

print("Combined dictionary with added values for common keys:", combined_dict)


# 8-Write a Python program that calculates the factorial of a number using a loop.

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

# 9-Write a Python program to find all the unique words and count the frequency of occurrence from a given list of strings. 

text="apple"
# I want this in a output:
d={"a":1,"p":2,"l":1,"e":1}


text="apple"
d={}
for i in text: #a #p #p
    if i in d: #a #p
        d[i]=d[i]+1  #d[p]=1+1
    else:
        d[i]=1   #"a":1, #"p":1
print(d)

# 10-Write a Python program to check if a given value is present in a set or not.

set1={3,5,7,9}
print(7 in set1)