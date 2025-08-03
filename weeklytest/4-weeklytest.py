# Section A: Theory (10 Questions)

# Q1. Explain the difference between for loop and while loop in python. Provide an example of each.
'''
A1. A for loop is used to iterate over a sequence (such as a list or string) and execute a block of code for each item in the sequence.
for i in range(5):
    print(i)

 
 A whileloop, on the other hand, continues to execute a block of code as long as a

 count = 0
while count < 5:
    print(count)
    count += 1


'''
# Q2. Discuss the role of the range() function in a for loop.
'''
The range() function generates a sequence of numbers. It is commonly used in for loops to define how many times the loop will run.
Example:
for i in range(3):
    print(i)
'''

# Q3. What is infinite loop? Provide an example and explain how to break out of it. 
'''
An infinite loop keeps running forever unless explicitly stopped with a break statement or an external interruption.
Example:
while True:
    user_input = input("Type 'exit' to stop: ")
    if user_input == 'exit':
        break


'''

# Q4. What is set, How it is different from list.
'''
A set is an unordered collection of unique items.

A list is an ordered collection that can have duplicate items.

Difference:
Sets do not allow duplicates; lists do.
Sets are unordered; lists are ordered.
Sets are faster for membership tests.

Example:
s = {1, 2, 3}
l = [1, 2, 2, 3]



'''

# Q5. What is List Comprehension?
'''
List comprehension is a concise way to create lists using a single line of code.
Example:
squares = [x**2 for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]

'''

# Q6. What is Dictionary, Brief it.
'''
A dictionary is an unordered collection of key-value pairs in Python.
Keys are unique.
Values can be of any type.
dictiinary is collection of uniqe data
it is mutable
it is ordered after python 3.6
is a indexed (keys are indexes)
key should br unique
are collection of key value pair ,are creatde using curely brackets {}
duplicat allow only value 
duplicate key is not allows
Example:

student = {"name": "Alice", "age": 20, "grade": "A"}


'''

# Q7. Discuss the difference between "and","or","not" logical operators in python.
'''
and: Returns True if both conditions are true.
or: Returns True if at least one condition is true.
not: Reverses the boolean value.


a = 5
print(a > 2 and a < 10)  # True
print(a > 2 or a < 3)    # True
print(not(a > 2))        # False


'''

# Q8. What is difference between Remove and Discard in set.
'''
remove(item) removes the item. If the item does not exist, it raises an error.
discard(item) removes the item. If the item does not exist, it does not raise error

s = {1, 2, 3}
s.remove(2)   # OK
s.discard(4)  # No error
# s.remove(4) # Will raise KeyError


'''
 
# Q9. What is the difference between lists, tuples and sets?

'''
List: A list is a collection of items that can be of any data type, including strings,
integers, floats, and other lists. Lists are denoted by square brackets [] and are
mutable.
Tuple: A tuple is a collection of items that can be of any data type, including
strings, integers, floats, and other tuples. Tuples are denoted by parentheses ()
and are immutable.
Set: A set is an unordered collection of unique items. Sets are denoted by curly
set in un index  set is mutable dose not allow duplicats 



'''

# Q10. Explain the concept of Nested if statement, Provide an example of a nested if statements.
'''
# A nested if statement is used to check multiple conditions in a single if statement.
# It is used when we need to check multiple conditions and perform different actions based on those conditions.
# The syntax of a nested if statement is as follows:
# if condition1:
#     if condition2:
#         # code to be executed if both conditions are true
#     else:
#         # code to be executed if condition1 is true but condition2 is false

num = 10
if num > 0:
    if num % 2 == 0:
        print("Positive even number")
    else:
        print("Positive odd number")
else:
    print("Not positive")


'''
# Section B: Write Code For (10 Questions) 

# Q1. Write a python program to print all odd numbers between 1 and 50 using while loop.
i = 1
while i <= 50:
    if i % 2 != 0:
        print(i, end=' ')
    i += 1


# Q2. Write a Python program that sums only the integers in the list using a loop.
#     data = [10, "apple", 5.5, 20, "banana", 30]
data = [10, "apple", 5.5, 20, "banana", 30]
total = 0
for item in data:
    if type(item) == int:
        total += item
print("Sum of integers:", total)

# Q3. Write a python program to calculate the sum of all even numbers between 1 and 50 using for loop.
sum_even = 0
for i in range(1, 51):
    if i % 2 == 0:
        sum_even += i
print("Sum of even numbers:", sum_even)


# Q4. Write a Python program to find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2700 (both included).
for i in range(1500, 2701):
    if i % 7 == 0 and i % 5 == 0:
        print(i, end=' ')


# Q5. Find the second largest element from list.(without using inbuilt function)
lst = [4, 10, 3, 5, 8, 2]
first = second = float('-inf')
for num in lst:
    if num > first:
        second = first
        first = num
    elif num > second and num != first:
        second = num
print("Second largest:", second)


# Q6. list1=[4,3,2,1,3,2,3,4,56,3,7,543,2,3]
#     Remove all the 3 from list.
list1 = [4,3,2,1,3,2,3,4,56,3,7,543,2,3]
while 3 in list1:
    list1.remove(3)
print("List after removing 3s:", list1)


# Q7.Write a Python program that takes a list and a value as input and returns the number of times the value appears in the list
lst = [1, 2, 2, 3, 2, 4, 5]
val = 2
count = 0

for i in lst:
    if i == val:
        count += 1

print("Count:", count)


# Q8. Check an element is present in a Tuple.
tup = (1, 2, 3, 4, 5)
element = 3
if element in tup:
    print("Element is present")
else:
    print("Element is not present")


# Q9.  WAP to remove all the even elements from the list
lst = [1, 2, 3, 4, 5, 6, 7, 8]
result = []
for num in lst:
    if num % 2 != 0:
        result.append(num)
print("List after removing even numbers:", result)


# Q10.Given a list of mixed data types, write a program that returns two separate lists: one with only numeric values (int and float), 
#     and another with only string values.
#    mixed_list = [10, "hello", 3.14, 42, "world", 7.5]
mixed_list = [10, "hello", 3.14, 42, "world", 7.5]

num_list = []
str_list = []

for item in mixed_list:
    if type(item) == int or type(item) == float:
        num_list.append(item)
    elif type(item) == str:
        str_list.append(item)

print("Numbers:", num_list)
print("Strings:", str_list)

# Section C: Correct the Code (10 Questions)

# Q1.

# my_list = [1, 2, 3, 4]
# my_list.append(5, 6)
# print(my_list)

my_list = [1, 2, 3, 4]
my_list.extend([5, 6])  # Corrected: append() takes one argument; use extend() for multiple
print(my_list)


# Q2.

# numbers = [10, 20, 30, 40]
# print(numbers[4]) 


numbers = [10, 20, 30, 40]
# print(numbers[4])  # Error: index 4 doesn't exist
print(numbers[3])    # Fixed: Last index is 3


# Q3.

# count = 1  
# while count <= 5  
# print(count)  
#     count = count + 1  

count = 1  
while count <= 5:       # Fixed: added colon
    print(count)        # Fixed: added indentation
    count = count + 1


# Q4.

# my_tuple = (1, 2, 3)
# my_tuple[0] = 10
# print(my_tuple)

my_tuple = (1, 2, 3)
# my_tuple[0] = 10       # Error: Tuples are immutable
# Fix: Convert to list if you want to modify
my_list = list(my_tuple)
my_list[0] = 10
print(tuple(my_list))


# Q5.

# for i in range(3):  
# for j in range(3):  
#     print("*", end=" ")  
# print() 

for i in range(3):  
    for j in range(3):  
        print("*", end=" ")  
    print()   # Fixed: indent print() correctly for rows


# Q6.

# num1 = input("Enter first number: ")  
# num2 = input("Enter second number: ")  
# sum = num1 + num2  
# print("Sum:", sum)  

num1 = input("Enter first number: ")  
num2 = input("Enter second number: ")  
sum = int(num1) + int(num2)   # Fixed: convert input to int
print("Sum:", sum)




# Q7.

# fruits = ["apple", "banana", "cherry"]
# fruits.remove("mango")
# print(fruits) 

fruits = ["apple", "banana", "cherry"]
if "mango" in fruits:
    fruits.remove("mango")  # Avoids ValueError
print(fruits)



# Q8.

# num = "10"  
# result = num * 2  
# print(result)  

num = "10"  
result = int(num) * 2     # Fixed: convert to int before multiplication
print(result)


# Q9.

# student = {1,2,3,4}  
# student.add(2,3,5) 
# print(student)

student = {1, 2, 3, 4}
student.update([2, 3, 5])  # Fixed: use update() with iterable
print(student)


# Q10.

# my_dict = {1: "apple", 2: "banana"}
# print(my_dict[3])

my_dict = {1: "apple", 2: "banana"}
# print(my_dict[3])  # Error: KeyError if 3 doesn't exist
print(my_dict.get(3, "Not Found"))  # Safer: use get() with default
