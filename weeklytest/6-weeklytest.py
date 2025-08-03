'''
Section A: Theory (10 Questions)

Q1. What is slicing in python? Brief it.
Slicing in Python means accessing a part of a sequence (like a list, tuple, or string) using a start, stop, and step index. It creates a new subsequence without modifying the original.

Q2. What is Keywords in python?
 Keywords are reserved words in Python that have special meaning and cannot be used as identifiers (variable names). For example: if, else, for, def, class, etc.


Q3. What is break, continue, pass in python?
break: exits the nearest enclosing loop completely.

continue: skips the rest of the current loop iteration and goes to the next one.

pass: does nothing, used as a placeholder



Q4. What is an iterator in Python?
An iterator is an object which implements the __iter__() and __next__() methods, allowing you to traverse through elements one at a time. Lists, tuples, sets, and dictionaries can all return iterators.


Q5. What is Dyanamically Typed language?
In dynamically typed languages like Python, variable data types are checked at runtime, not in advance. So you do not need to declare the data type explicitly.

Q6. When should you use lambda functions in Python?
Use lambda functions for short, simple, one-line anonymous functions where defining a full def function would be overkill. Often used with map(), filter(), or sorted().



Q7. What is negative indexes and why are they used?
Negative indexes allow you to access sequence elements from the end rather than the beginning

s = "python"
print(s[-1])  # Output: 'n' (last character)



Q8. What is string in python?
A string is an immutable sequence of Unicode characters. Strings in Python are enclosed in single quotes, double quotes, or triple quotes.


 
Q9. Explain difference between discard() and remove()?
Both are used to remove elements from a set:
remove(x) raises an error if x is not present.
discard(x) does not raise an error if x is not present.

s = {1,2,3}
s.discard(4)  # no error
s.remove(4)   # raises KeyError



Q10. What is Recurrsion function, Brief it with example.
A recursive function is a function that calls itself to solve a problem by breaking it down into smaller sub-problems.

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))  # Output: 120


'''


# Section B: Correct the Code (10 Questions)

# Q1.

my_tuple = (10, 20, 30)
my_tuple=25
print(my_tuple)


# Q2. What will be the output of this code?
   
x = 10
for i in range(x):
    if i % 2 == 0:
        continue
    print(i)

# Q3.The following code contains an error. Identify and correct it:
   
def my_func(x, y):
    return x + y
result = my_func(5,6)
print(result)


# Q4.
   
fruits = ["apple", "banana", "orange"]
fruits.append("grape")
print(fruits)



# Q5. What will be the output of this code?
   
a = (1, 2, 3)
b = list(a)
b.append(4)
print(a)

# Q6.

person = {"name": "Alice", "age": 25}
print(person.get("gender", "Gender not specified"))
person["age"] = 26
person["country"] = "USA"
print(person)

# Q7.

colors = ["red", "green", "blue"]
colors.append("yellow")
print(colors)

 
# Q8.

values = {100, 200, 300}
values_list = list(values)
print(values_list[1])  # valid



# Q9.

info = {"city": "New York", "country": "USA"}
info["population"] = 8000000
print(info)


# Q10.

count = 1  
while count <= 5  :
 print(count)  
 count = count + 1 


# Section C: Write Code For (10 Questions) 

# Q1. Write a lambda function to find the square of a given number.
squ=lambda x : x*x
num=int(input("enter the number "))
print(squ(num))
# Q2. Write a lambda function that returns "Even" if a number is even and "Odd" if it is odd.
even=lambda x : x % 2 == 0
odd= lambda x : x % 2 != 0
num=int(input("enter the nuumber "))       
if even(num):
   print(num,"even")
else:
   print(num,"odd")


# Q3. Write a Python program to create a dictionary that stores student names as keys and their scores as values. 
#     Write a function that returns the name of the student with the highest score.
student={"jay":49,"raj":50,"mina":65}


# Q4. Write a Python program using map() to double all the numbers in a list.
#     # Input: [1, 2, 3, 4, 5]
#     # Output: [2, 4, 6, 8, 10]

numbers = [1, 2, 3, 4, 5]

result = list(map(lambda x: x *2, numbers))
print(result)

# Q5. Write a Python program using filter() to extract words with more than 5 characters from a list.
#     # Input: ["apple", "banana", "cat", "elephant"]
#     # Output: ["banana", "elephant"]


Input= ["apple", "banana", "cat", "elephant"]
f= list(filter(lambda x: len(x) > 5, Input))
print(f)
# Q6. Write a program to fetch key of highest value from a Dictionary.
data = {"a": 10, "b": 45, "c": 32}

value = -1
key = None

for k in data:
    if data[k] > value:
        value = data[k]
        key = k

print(f"Key with highest value: {key}")


# Q7. Write a function that takes a string as input and returns the string in reverse order.
def rev(s):
    return s[::-1]

print(rev("hello"))  # Output: "olleh"


# Q8. Given two dictionaries, write a function to find and return a new dictionary containing only the common keys and their corresponding values.
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 20, "c": 30, "d": 40}

common_dict = {}

for k in dict1:
    if k in dict2:
        common_dict[k] = dict1[k]

print(common_dict)

 
# Q9. Write a function that takes a sentence and returns the longest word in it.
#     Input: "Python is a powerful programming language"
#     Output: "programming"
def long(sentence):
    words = sentence.split()
    return max(words, key=len)
text = "Python is a powerful programming language"
print(long(text))  


# Q10. Given a dictionary marks = {'Math': 90, 'Science': 85, 'English': 88}, calculate and print the total marks.
marks = {'Math': 90, 'Science': 85, 'English': 88}
total = sum(marks.values())
print(f"Total marks: {total}")

