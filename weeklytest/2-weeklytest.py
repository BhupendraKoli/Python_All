'''
Q1. Explain the difference between for loop and while loop in python. Provide an example of each

    for loop: Used when you want to iterate over a sequence (like a list, string, or range) a specific number of times.

    for i in range(5):
    print(i)
    Output: 0, 1, 2, 3, 4

    while loop: Used when you want to repeat an action as long as a condition is true.

     i = 0
    while i < 5:
       print(i)
       i += 1
       Output: 0, 1, 2, 3, 4


Q2. Discuss the role of the range() function in a for loop.
    
    The range() function generates a sequence of numbers.
    It's commonly used with for loops to repeat a block of code a specific number of times.
    for i in range(3):  # i will be 0, 1, 2
       print("Hello")
        Output: Hello, Hello, Hello


Q3. What is an infinite loop? Provide an example and explain how to break out of it.
     An infinite loop keeps running forever because the condition never becomes false.
    You can use the break statement to exit it manually.

      Example:

      while True:
         name = input("Type 'exit' to quit: ")
         if name == "exit":
          break

Q4. What is a set? How is it different from a list?
      A set is an unordered collection of unique elements.
      A list is an ordered collection and can contain duplicates.
      Example:
        my_set = {1, 2, 3, 3}
        print(my_set)  # Output: {1, 2, 3}

        my_list = [1, 2, 3, 3]
        print(my_list)  # Output: [1, 2, 3, 3]

Q5. What is an Interpreted Language?
     An interpreted language executes code line-by-line using an interpreter.
     Python is an interpreted language, which makes it easier for debugging but may run slower than compiled languages.


Q6. Difference between if, elif, and else statement. Provide an example.
    if: Tests the first condition.
    elif: Tests other conditions if the previous ones are false.
    else: Executes if all if and elif conditions are false.

 Example:
    x = 10
    if x < 0:
        print("Negative")
    elif x == 0:
        print("Zero")
    else:
        print("Positive")

Q7. Discuss the difference between and, or, not logical operators in Python.
     and: Returns True if both conditions are True.
     or: Returns True if at least one condition is True.
     not: Reverses the result (True becomes False, and vice versa).
        
Q8. How can you convert a string to an integer? Example s = "6"
     Use the int() function:

     s = "6"
     num = int(s)
     print(num + 4)  # Output: 10


Q9 What is the difference between lists, tuples, and sets?    
    1. Lists
         Ordered: Yes  items maintain the order you add them.
         Mutable: Yes  you can add, remove, or change elements.
         Allows Duplicates: Yes  the same value can appear multiple times.
         Indexable: Yes access items by position using [index].
         Syntax: Square brackets [].

    2. Tuples
         Ordered: Yes
         Immutable: Yes – once created, cannot change values.
         Allows Duplicates: Yes
         Indexable: Yes
         Syntax: Parentheses ().
    
    3. Sets
         Ordered: No items do not maintain insertion order.
         Mutable: Yes you can add or remove items.
         Allows Duplicates: No  only unique values are allowed.
         Indexable: No  cannot access items using an index.
         Syntax: Curly braces {}.     
         

Q10. Explain the concept of Nested if statement. Provide an example.
      A nested if means an if statement inside another if block.

      Example:
      x = 10
      if x > 5:
          if x < 20:
              print("x is between 5 and 20")     

'''
# Q1. Write a python program to print all odd numbers between 1 and 50 using while loop.
i = 1
while i <= 50:
    if i % 2 != 0:
        print(i ,end=" ")
    i += 1


# Q2. Write a Python program that sums only the integers in the list using a loop.
#     data = [10, "apple", 5.5, 20, "banana", 30]
data = [10, "apple", 5.5, 20, "banana", 30]
total = 0
for i in data:
    if type(i) == int:
        total += i
print("Sum of integers:", total)



# Q3. Write a python program to calculate the sum of all even numbers between 1 and 50 using for loop.
i=1
sum_even=0
for i in range(1,51):
    if i % 2 == 0:
        sum_even += i
print("Sum of even numbers:", sum_even)


# Q4. WAP and calculate the area of rectangle.
l=int(input("enter the length "))
b=int(input("enter the breadth "))
area=l*b
print("area of rectangle is ",area)


# Q5. WAP input three no ,now add first two no and subtract third no from them.
a=int(input("enter the first number "))
b=int(input("enter the second number "))
c=int(input("enter the third number "))
sum=a+b
sub=sum-c
print("result is ",sub)
# Q6. list1=[4,3,2,1,3,2,3,4,56,3,7,543,2,3]
#     Remove all the 3 from list.

list1=[4,3,2,1,3,2,3,4,56,3,7,543,2,3]
new_list=[]
for i in list1:
    if i !=3:
        new_list.append(i)
print(new_list)




# Q7.Write a Python program that takes a list and a value as input and returns the number of times the value appears in the list
user_list = input("Enter list elements separated by space: ")
value = input("Enter value to count: ")
count = user_list.count(value)
print(f"'{value}' appears {count} times.")


# Q8. WAP to check the use is eligible for insurance or not, if use is married and age is greater then 30 years then he is eligible for the insurance.
married = input("Are you married? (yes/no): ")
age = int(input("Enter your age: "))

if married == "yes" and age > 30:
    print("Eligible for insurance.")
else:
    print("Not eligible for insurance.")

# Q9.  WAP to remove all the even elements from the list
l=[1,2,3,4,5,6,7,8,9,10]
a=[]
for i in l :
    if i%2!=0:
        a=a+[i]
print(a)
        

# Q10.Given a list of mixed data types, write a program that returns two separate lists: one with only numeric values (int and float), 
#     and another with only string values.
#    mixed_list = [10, "hello", 3.14, 42, "world", 7.5]
mixed_list = [10, "hello", 3.14, 42, "world", 7.5]
num_list=[]
string_list=[]
for i in mixed_list:
    if type(i)==int or type(i)==float:
        num_list=num_list+[i]
    elif type(i)==str:
        string_list=string_list+[i]
print(num_list)
print(string_list)


'''
Q1.

age = input("Enter your age: ")

if age >= 18:
print("You are eligible to vote.")
elif age < 18:
print("You are not eligible to vote.")
else
print("Invalid input.")

Q2.

num = int(input("Enter a number: "))  

if num > 0  
    print("The number is positive.")  
elif num = 0:  
    print("The number is zero.")  
else:  
    print("The number is negative.")  

Q3.

count = 1  
while count <= 5  
print(count)  
    count = count + 1  
Q4.

for i in range(1, 10)  
    print i  

Q5.

for i in range(3):  
for j in range(3):  
    print("*", end=" ")  
print() 

Q6.

num1 = input("Enter first number: ")  
num2 = input("Enter second number: ")  
sum = num1 + num2  
print("Sum:", sum)  

Q7.

fruits = ("apple", "banana", "cherry")  
fruits[1] = "orange"  
print(fruits) 

Q8.

num = "10"  
result = num * 2  
print(result)  

Q9.
age=input("enter your age:" )

Q10.

colors = ["red", "blue", "green"]  
print(colors[3])

'''

# Q 1
age = int(input("Enter your age: "))  # Convert input to integer

if age >= 18:
    print("You are eligible to vote.")
elif age < 18:
    print("You are not eligible to vote.")
else:
    print("Invalid input.")  # This 'else' is unnecessary; age < 18 already handled

# Q 2
num = int(input("Enter a number: "))  

if num > 0:
    print("The number is positive.")
elif num == 0:
    print("The number is zero.")
else:
    print("The number is negative.")

# Q3
count = 1  
while count <= 5:
    print(count)
    count = count + 1

# Q 4
for i in range(1, 10):
    print(i)

#Q5
for i in range(3):  
    for j in range(3):  
        print("*", end=" ")
    print() 

#Q6
num1 = int(input("Enter first number: "))  
num2 = int(input("Enter second number: "))  
sum = num1 + num2  
print("Sum:", sum)

#Q7
fruits = ("apple", "banana", "cherry")
# To modify, convert to list first:
fruits_list = list(fruits)
fruits_list[1] = "orange"
fruits = tuple(fruits_list)
print(fruits)

#Q8
num = 10
result = num * 2
print(result)  
#Q9
age = input("Enter your age: ")
print("You entered age:", age)
#Q10
colors = ["red", "blue", "green"]  
print(colors)