'''
Section A: Theory (10 Questions)

Q1. What is Python? What are the benefits of using Python.
A1. Python is a high-level, interpreted programming language that is widely used for various purposes such
as web development, scientific computing, data analysis, artificial intelligence, and more. The benefits of using
Python include its simplicity, readability, and ease of use, making it an ideal language for beginners and
experienced programmers alike.
Benefits:
Easy to learn and use
Open-source and free
Large standard library
Cross-platform support
Huge community and support
Suitable for web development, data science, AI, machine learning, etc.

Q2. Explain the concept of a list in Python. 
In Python, a list is a collection of items that can be of any data type
including strings, integers, floats, and other lists. Lists are denoted by square brackets
[ ] and are mutable, meaning they can be modified after creation.
A list in Python is an ordered collection of items that can hold elements of different data types like integers, strings, floats, etc. Lists are mutable, meaning their elements can be changed after creation. Lists are defined using square brackets [].

Q3. Write the 5 features of python list in details.
 The 5 features of Python lists are:
1. Ordered: Lists maintain the order in which elements were added.
2. Indexed: Lists are indexed, meaning each element has a specific position or index.   
3. Mutable: Lists can be modified after creation.
4. Heterogeneous: Lists can hold elements of different data types.
5. Dynamic: Lists can grow or shrink in size as elements are added or removed.


Q4. What is the use of Loops? Explain in brief.
Loops are used to execute a block of code repeatedly for a specified number of times. They ar
e used to iterate over a sequence (such as a list, tuple, or string) or to
execute a block of code until a certain condition is met.

for loop: Iterates over a sequence (like list, tuple).
while loop: Repeats as long as a condition is true.

Q5. List is mutable or im-mutable and how? Explain with example
List is mutable. It can be changed after creation.
my_list = [1, 2, 3]
my_list[0] = 100
print(my_list)  # Output: [100, 2, 3]



Q6. What is difference between append and extend?
append() function adds an element to the end of the list.
extend() function adds multiple elements to the end of the list.
append() adds one element at a time, while extend() adds multiple elements at once.



Q7. Explain the remove method in a list with a example.
The remove() method removes the first occurrence of the specified value.                                    
my_list = [1, 2, 3, 4, 5]
my_list.remove(3)
print(my_list)  # Output: [1, 2, 4, 5]



Q8. What is difference between static and dyanamic typed language.
Static typed language: The type of a variable is known at compile time.
Dynamic typed language: The type of a variable is known at runtime.
In static typed language, the type of a variable is known at compile time, whereas in dynamic typed
language, the type of a variable is known at runtime.
Static typed language: Variable types are defined at compile time (e.g., Java, C++).
Dynamic typed language: Variable types are determined at runtime (e.g., Python).
 
Q9. What is Interpreted language?
An interpreted language is a high-level language that is translated into machine code at runtime. The code is
not compiled beforehand, but rather interpreted line by line as it is executed. This means that the cod 
e is not converted into machine code until it is run, and the process is slower than compilation.
An interpreted language executes instructions line-by-line using an interpreter rather than compiling the whole code at once. Python is an interpreted language.

Q10. What is difference between del and clear?
del() function is used to delete a specific element from a list.
clear() function is used to delete all elements from a list.
del() deletes a specific element, while clear() deletes all elements.



'''
# Section B: Write Code For (10 Questions) 

# Q1. How do you append an element to a list in Python?
list1=[1,2,3,4,5]
list1.append(6)
print(list1)

# Q2. How do you find the length of a list in Python?
list1=[1,2,3,4,5]
s=0
for i in list1:
    s=s+1
print(s)
# Q3. How do you access the last element of a list in Python?
list1=[1,2,3,4,5]
print(list1[-1])

# Q4. How do you find the average of elements in a list in Python?
list1=[1,2,3,4,5]
avg=sum(list1)/len(list1)
print("the avrage is ",avg)

# Q5.Remove Duplicates from a list. l=[1,2,3,1,3,45,6,78,8,3,90,24]
l1=[1,2,3,1,3,45,6,78,8,3,90,24]
res=[]
for i in l1:
   if i not in res:
      res.append(i)
print(res)

# Q6. Write a program and check the number is Armstrong number or not?

num=int(input("entr the number"))

temp=num
s=0
power=len(str(num))
while temp !=0:
    digit=temp%10
    s=s+digit**power
    temp=temp//10   
if s==num:
    print(num,"is an armstrong number")
else:   
  print(num,"is not an armstrong number")

# Q7. Write a Python program that takes a positive integer as input and calculates the sum of its digits using a loop.
num = int(input("Enter a positive integer: "))
sum_digits = 0

while num > 0:
    digit = num % 10
    sum_digits += digit
    num = num // 10

print("Sum of digits:", sum_digits)

# Q8. Write a program and check the number is Palindrome or not?
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
   
# Q9. WAP and print the Factorial of any number.
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

# Q10.l=[1,2,3,4,5] Fetch all even indexed elements from the list.
l = [1, 2, 3, 4, 5]
even_indexed = l[::2]
print("Even indexed elements:", even_indexed)  # Output: [1, 3, 5]




# Section C: Correct the Code (10 Questions)

# Q1.

#    fruits = ["apple", "banana", "cherry"]
#    print(fruits[3])
fruits = ["apple", "banana", "cherry"]
print(fruits[2])  # Indexing starts at 0



# Q2.

#    number = 12
#    if number > 10
#    print("Greater than 10")
#    elif number == 10
#        print("Equal to 10")
#    else:
#        print("Less than 10")


number = 12
if number > 10:
    print("Greater than 10")
elif number == 10:
    print("Equal to 10")
else:
    print("Less than 10")


# Q3.
 
#  a = 5
#    b = 10
#    print(fSum of a and b is: {a + b}")

a = 5
b = 10
print(f"Sum of a and b is: {a + b}")


# Q4. 

# x = "10"
#    y = 5
#    print(x + y)
x="10"
y = 5
print(x + str(y))


# Q5.

#   colors = ["red", "green", "blue"]
#    colors[1] = "yellow"
#       print(colors)

colors = ["red", "green", "blue"]
colors[1] = "yellow"
print(colors)

# Q6.
#    fruits = ["apple", "banana", "cherry"]
#     print(fruits["banana"])

fruits = ["apple", "banana", "cherry"]
print(fruits[1])

# Q7.
 
# i=1
# while i<= 10:
#    print(i)

i = 1
while i <= 10:
    print(i)
    i += 1

# Q8.

# age = 25
# print("I am " + age + " years old.")
age=25
print("I am ", age , " years old.")

# Q9.

# print(message)
# message = "This is a test message."

message = "This is a test message."
print(message)

# Q10.

# data = [1, "banana", 3, "apple", 2]
# data.sort()  
# print(data)

data = [1,  3,  2]
data.sort()
print(data)
