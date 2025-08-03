# while loop
'''
the block of code excute undre cartain condition 
to handle the repetive task

parameters 
1 initilization
2 condition 
3 block of code
4 increment decrememnt
'''
# i need to print oython for 5 times
# i = 0
# while i<5:
#     print("python")
#     i = i+1

# print number from 0 to 1
# a = 1
# while a<=10:
#     print(a,end="")
#     a = a+1 
#     a = 1
# print number from 10 to 1





'''
    #1. Display numbers from 1 to 100.
i = 1
while i <= 100:
    print(i, end=' ')
    i += 1
    print("\n")
#2. Display all even numbers from 1 to 100.
# i = 2
# while i <= 100:
#     print(i, end=' ')
#     i += 2
i = 1
while i <= 100:
    if i % 2 == 0:
        print(i, end=" ")
    i += 1  # This must be outside the if block


#3. Write a program to print all natural numbers from 1 to n. - using while loop
n = int(input("Enter the value of n: "))
i = 1
while i <= n:
    print(i, end=' ')
    i += 1
    print("\n")
#4. Write a program to print all natural numbers in reverse (from n to 1). - using while loop
n = int(input("Enter the value of n: "))
i = n
while i >= 1:
    print(i, end=' ')
    i -= 1
    print("\n")
#5. Write a program to print all even numbers between 1 to 100. - using while loop.
i = 2
while i <= 100:
    print(i, end=' ')
    i += 2
    
# will print even number from 1 yo 20 and count it
i=1
c=0
while i <= 20:
    if i % 2 == 0:
        print(i, end=' ')
        c = c+1
    i=i+1   

# sum of all even number
s=0
i=1
while i <= 10:
    if i % 2 == 0:
        print(i,end="")
        s = s + i
    i=i+1
print("\n the sum of even number sum",s)  
#6. Write a program to print all odd numbers between 1 to 100. - using
i = 1
while i <= 100:
    if i % 2 != 0:
        print(i, end=' ')
    i += 1
# 7. Write a program to find sum of all natural numbers between 1 to n.
n = int(input("Enter the value of n: "))
i = 1
total = 0
while i <= n:
    total += i
    i += 1
print("Sum of natural numbers from 1 to", n, "is:", total)
# 8. Write a program to find count of all odd numbers between 1 to n.
n = int(input("Enter the value of n: "))
i = 1
count = 0
while i <= n:
    if i % 2 != 0:
        count += 1
    i += 1
print("Count of odd numbers from 1 to", n, "is:", count)

#9. Write a program to find sum of all even numbers between 1 to n.
n = int(input("Enter the value of n: "))
i = 1
total = 0
while i <= n:
    if i % 2 == 0:
        total += i
    i += 1
print("Sum of even numbers from 1 to", n, "is:", total)

#10.Display all odd numbers from 200 to 300.
i = 200
while i <= 300:
    if i % 2 != 0:
        print(i, end=' ')
    i += 1
'''
# nested while loop 
# i=1
# while i<=5:
#     print("codenera ",end="")
#     j=1
#     while j<=3:
#      print("python ",end="")
#      j+=1
#     print("") 
#     i+=1

# write a Python program using a nested while loop to print all pairs (i, j), 
# where i ranges from 1 to 3 and j ranges from 1 to 3
i=1
while i<=3:
   j=1
   while j<=3:
    print((i,j),end=" ")
    j+=1
   print("")
   i+=1

