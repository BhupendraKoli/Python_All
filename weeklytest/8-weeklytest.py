'''
Section A:


1. What is OOPS? Brief it.
OOPS is Object-Oriented Programming, a programming approach centered around objects instead of functions.
It helps in modeling real-world interactions and makes code reusable and easier to maintain.

Classes:
class is a blue print of object 
it is not a real entity 

Blueprints for creating objects. 
They define attributes (data) and methods (functions) that objects of that class will possess.


Objects:
it is real entity which has its own identity ,state and behaviour 
it is a instances/object of a class 

Core principles include:
Objects: Instances representing entities.
Classes: Blueprints for objects, defining properties and behaviors.
Encapsulation: Combining data and methods within a class and controlling access.
Inheritance: Allowing classes to inherit features from others for code reuse.
Polymorphism: Enabling objects of different types to be treated similarly.
Abstraction: Focusing on essential features and hiding complexity.


2. Explain the difference between mutable and immutable data types in Python.
Mutable types :-
can be changed after creation, affecting the original object (e.g., Lists, Dictionaries, Sets). 
They are useful when data needs frequent updates.

Immutable types :-
cannot be changed after creation; modifications create a new object (e.g., Integers, Strings, Tuples). 
They are used when data integrity or constancy is required.

3. What is the difference between a list, tuple, set, and dictionary in Python?
List: Ordered, mutable, allows duplicates, accessed by index, uses [].

Tuple: Ordered, immutable, allows duplicates, accessed by index, uses ().

Set: Unordered, mutable, unique elements only, no index access, uses {}.

Dictionary: Unordered collection of unique key-value pairs, mutable, accessed by keys, uses {}.

4. What is a lambda function in Python? How is it different from a regular function?

Lambda functions are anonymous functions defined with lambda, taking multiple arguments but having a single expression. 
They are often used for short operations or as arguments to other functions.
Regular functions are defined with def, have a name, can contain multiple lines of code, and use return.
Key differences lie in definition, naming, body complexity, and return behavior.


5. What does the enumerate() function do in Python? Provide a use case.

The enumerate() function adds a counter to an iterable, yielding (index, item) pairs. You can set a starting index.
Use Case: Iterating through a list to display items with their position.
fruits = ["apple", "banana", "cherry"]
for position, fruit in enumerate(fruits, start=1):
    print(f"Position {position}: {fruit}")


6. How does the zip() function work in Python? What happens if the input iterables are of unequal length?

The zip() function combines elements from multiple iterables into tuples, creating an iterator.
If iterables have unequal lengths, zip() stops when the shortest one is finished, ignoring extra elements in longer iterables.
list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c']
zipped_list = list(zip(list1, list2))
print("Unequal lengths result:", zipped_list) # Output: [(1, 'a'), (2, 'b'), (3, 'c')]


7. What is Function? Brief it.

A function is a block of reusable code for a specific task.
It can take inputs, process them, and return a result.
Functions improve code organization and reusability. Python functions are defined using def.


8. Explain the difference between for and while loops in Python. When would you use one over the other?

For loops are for iterating over sequences when the number of iterations is known (e.g., lists, ranges).

While loops are used when the number of iterations is unknown and depends on a condition remaining true.
Use for for known iterations and while for condition-based iterations

9. What is the difference between break, continue, and pass in loop control statements?

Break: Exits the loop entirely.
Continue: Skips the rest of the current iteration and moves to the next.
Pass: A null operation used as a placeholder where syntax requires a statement but no action is needed.


10. How do if, elif, and else statements work in Python? How is indentation significant in conditionals?

if executes code if a condition is true.
elif (else if) checks subsequent conditions if previous ones were false.
else runs if all previous conditions are false.
Python uses indentation (typically 4 spaces or 1 tab) to define code blocks within these statements; incorrect indentation causes errors.

x = 10
if x > 0:
    print("Positive number")
elif x < 0:
    print("Negative number")
else:
    print("Zero")



'''
'''

Section B:


'''
1.

numbers = [1, 2, 3]
numbers.append(4)  
print(numbers)


2.

t = (1, 2, 3)
t_list = list(t)
t_list[0] = 5
t = tuple(t_list)
print(t)  # Output: (5, 2, 3)




3.

s = set([1, 2, 2, 3, 4, 4])
s_list = list(s)
print(s_list[0])  # Might be any element, as sets are unordered

4. 

add = lambda x, y: x + y
print(add(3, 4))


5. 

fruits = ['apple', 'banana', 'cherry']
for fruit, i in enumerate(fruits):
    print(fruit, i)


6. 

names = ['Alice', 'Bob', 'Charlie']
scores = [90, 80, 70]

for name, score in zip(names, scores, strict=True):
    print(name, score)


names = ['Alice', 'Bob']
scores = [90, 80, 70]

for name, score in zip(names, scores):  # default behavior: shortest list wins
    print(name, score)



# 7. 

# x = input("Enter expression: ")
# print(eval(x))


8. 

for i in range(5):
 print("Number is:", i)

9. 

x = 10
if x > 5:
    print("Greater than 5")
else:
    print("small than 5")    


# 10.

for i in range(5):
    if i == 3:
        pass
        print("Skipped")
    print(i)


# Section C:


# 1. Write a Python program to find the sum of all even numbers in a given list.
l1=[1,2,3,42,5]
sum=0
for i in l1:
    if i % 2 == 0:
         print(i)
         sum+=i
print(sum )   

# 2. Given a list of tuples [(1, 2), (3, 4), (5, 6)], write a program to print the sum of each pair.
pairs = [(1, 2), (3, 4), (5, 6)]
for a, b in pairs:
    print(a + b)

# 3. Write a Python program to print all unique common elements between two lists using sets.
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

common = set(list1) & set(list2)
print(common)

# 4. Use a lambda function with filter() to extract all odd numbers from a given list.
numbers = [1, 2, 3, 4, 5, 6, 7]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)

# 5. Given a list of items, use enumerate() to print each item along with its index.
items = ['apple', 'banana', 'cherry']
for index, item in enumerate(items):
    print(index, item)

# 6. Create a dictionary by zipping two lists, e.g., names = ['Alice', 'Bob'] and scores = [85, 90].
names = ['Alice', 'Bob']
scores = [85, 90]

result = dict(zip(names, scores))
print(result)

# 7. Create an Employee class that has a constructor accepting name, designation, and salary. 
#    Implement a method to increase the salary by a given percentage.
class Employee:
    def __init__(self, name, designation, salary):
        self.name = name
        self.designation = designation
        self.salary = salary

    def increase_salary(self, percentage):
        increase = self.salary * (percentage / 100)
        self.salary += increase
        print(f"New salary for {self.name}: {self.salary}")

emp = Employee("Alice", "Developer", 50000)
emp.increase_salary(10)

# 8. Write a Python program that prints numbers from 1 to 50. For multiples of 3, print "Fizz", for 5 "Buzz", and for both "FizzBuzz".
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# 9. Write a program to print the following pattern:

#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *
 
n = 5  # height of the top half

for i in range(1, 2 * n):
    if i <= n:
        stars = 2 * i - 1
        spaces = n - i
    else:
        stars = 2 * (2 * n - i) - 1
        spaces = i - n
    print(' ' * spaces + '*' * stars)

# 10. Create a NumberCheck class with a constructor (__init__) that initializes a number.
# and check a Number is Armstrong or not. Display in a method.
class NumberCheck:
    def __init__(self, number):
        self.number = number

    def check_armstrong(self):
        num = self.number
        temp = num
        count = 0
        while temp > 0:
            count += 1
            temp //= 10

        temp = num
        total = 0

        while temp > 0:
            digit = temp % 10

            power = 1
            for _ in range(count):
                power *= digit
            total += power
            temp //= 10

        if total == num:
            print(f"{num} is an Armstrong number.")
        else:
            print(f"{num} is not an Armstrong number.")
            
n = int(input("Enter a number: "))
obj = NumberCheck(n)
obj.check_armstrong()

