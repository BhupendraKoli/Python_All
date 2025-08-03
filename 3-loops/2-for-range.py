# for loop range 
#range 
'''
 range is the inbuilt function in python is used to generete 
  the sequence of numbers
  it is used to generate the sequence of numbers from 0 to n-1
  range(start ,stop,stap)

  start is the starting point of the sequence
  stop is the end point of the sequence
  step is the increment between the sequence
  

'''
'''
for i in range(1,5): # 5 is excludeue
    print(i,end=" ")  # prints 1,2,3,4

# will print number 0 to 10 
for i in range(11):
    print(i, end=" ")  # prints 0,1,2,3,4,

# will print number 0 to 10 with increment of 2
for i in range(0,11,2):
    print(i, end=" ")  # prints 0,2,4,6,8

# i want to print in verse  manner 10-1 
for i in range(10,0,-1):
    print(i,end=" ") # prints 10,9,8,7,6,5
'''
# # Q1 disply the number from 1 to 100
# for i in range(1,101):
#     print(i,end=" \n ") # prints 1,2,3,4,5,6

# # Q3 write a program to print all natural number from 1 to n
# n = int(input("enter the number:"))
# for i in range(1,n+1):
#     print(i,end=" \n ") # prints 1,2,3,4,5,6

# # Q4 write a program to print all natural number in revers form  n to 1
# n = int(input("enter the number:"))
# for i in range(n,0,-1):
#     print(i,end="\n ") # prints 1,2,3,4,5,
#     print("")

# # Q2 display the all even number from 1 to 100
# for i in range(0,101,2):
#     print(i,end=" \n") # prints 0,2,4,6,8,10

#  # Q5 display the all odd number from 1 to 100
# for i in range(1,101,2):
#         print(i,end=" ") # prints 1,3,5,7,9,11

# #  Q6. Write a program to find sum of all natural numbers between 1 to n
# n = int(input("Enter a positive number: "))
# sum = 0
# for i in range(1, n + 1):
#     sum += i
# print("Sum of natural numbers from 1 to", n, "is:", sum)

# # Q7. Write a program to find sum of all even numbers between 1 to n.
# # n = int(input("Enter a positive number: "))
# # sum = 0
# # for i in range(0, n + 1, 2):
# #      sum += i
# #      print("Sum of even numbers from 1 to", n, "is:", sum)

# n = int(input("Enter a number: "))
# sum_even = 0

# for i in range(1, n + 1):
#     if i % 2 == 0:
#         sum_even += i

# print("Sum of even numbers from 1 to", n, "is:", sum_even)


# ## Q8. Write a program to find sum of all odd numbers between 1 to n.
# # n = int(input("Enter a positive number: "))
# # sum = 0
# # for i in range(1, n + 1, 2):
# #      sum += i
# #      print("Sum of odd numbers from 1 to", n, "is:", sum)
# n = int(input("Enter a number: "))
# sum_odd = 0

# for i in range(1, n + 1):
#     if i % 2 != 0:
#         sum_odd += i

# print("Sum of odd numbers from 1 to", n, "is:", sum_odd)


# # Q9.Wap enter your name and print it five times.
# n=str(input(" enter the name "))
# for i in range(6):
#      print(n) # prints name 5 times

# Q10.Write a program take input first and last no and display all odd numbers between them and find sum and count
first = int(input("Enter the first number: "))
last = int(input("Enter the last number: "))
odd_sum = 0
odd_count = 0

# print("Odd numbers between", first, "and", last, "are:")
for num in range(first , last+1):
    if num % 2 != 0:
        print(num, end=" ")
        odd_sum += num
        odd_count += 1
print("\nTotal odd numbers:", odd_count)
print("Sum of odd numbers:", odd_sum)


# Q12.Print table of 7.(format: 7 X 1=7)
for i in range(1,11):
    print(f"7 x {i} = {7*i}") # prints table of


    
# Q11.Wap take input first and last no and display all even numbers between them and find sum and count.
first = int(input("Enter the first number: "))
last = int(input("Enter the last number: "))
even_sum = 0
even_count = 0
print("Even numbers between", first, "and", last, "are:")
for num in range(first + 1, last):
    if num % 2 == 0:
        print(num, end=" ")
        even_sum += num
        even_count += 1
print("\nTotal even numbers:", even_count)
print("Sum of even numbers:", even_sum)

