
# 1.WAP to print all the even number between 100-300.
for i in range(100,301):
    if i % 2 == 0:
     print(i ,end=" ")


# 2.WAP to count all the even number between 300-700.
count = 0
for i in range(300,701):
   if i % 2 ==0:
      count += 1
print("Total even numbers between 300-700 are:", count)

# 3.WAP to print the square of each number 10-200
for i in range(10, 201):
    print(f"Square of {i} is {i**2}")


# 4.WAP to print the table of inputed number from user.
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")


# 5.WAP to find the sum of all even number between 200-500. 
sum_even = 0
for i in range(200, 501):
    if i % 2 == 0:
        sum_even += i
print("Sum of even numbers:", sum_even)

# 6.WAP to find the sum of all odd number between 300-450.
sum_odd = 0
for i in range(300, 451):
    if i % 2 != 0:
        sum_odd += i
print("Sum of odd numbers:", sum_odd)

# 7.WAP to find the average between 100-300.
total = 0
count = 0
for i in range(100, 301):
    total += i
    count += 1
average = total / count
print("Average:", average)

# 8.WAP and Print Reverse a number.
num = int(input("Enter a number: "))
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10
print("Reversed number:", reverse)

# 9.Find the sum of even number of n digit number.
num = input("Enter an n-digit number: ")
sum_even = 0
for digit in num:
    if int(digit) % 2 == 0:
        sum_even += int(digit)
print("Sum of even digits:", sum_even)

# 10.Find the sum of n digit number.
num = input("Enter an n-digit number: ")
sum_digits = 0
for digit in num:
    sum_digits += int(digit)
print("Sum of digits:", sum_digits)

# 11.Find and Print the even and odd number from n digit number.
num = input("Enter an n-digit number: ")
print("Even digits:", end=' ')
for digit in num:
    if int(digit) % 2 == 0:
        print(digit, end=' ')
print("\nOdd digits:", end=' ')
for digit in num:
    if int(digit) % 2 != 0:
        print(digit, end=' ')

# 12.WAP to find factorial of a number.
num = int(input("Enter a number: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print(f"Factorial of {num} is {fact}")
