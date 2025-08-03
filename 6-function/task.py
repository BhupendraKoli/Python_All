# def add():
#     a = int(input("Enter first number to add: "))
#     b = int(input("Enter second number to add: "))
#     print("Addition:", a + b)

# def sub(a, b):
#     print("Subtraction:", a - b)

# def mul():
#     x = int(input("Enter first number to multiply: "))
#     y = int(input("Enter second number to multiply: "))
#     return x * y

# def div(x, y):   
#     return x / y

# count = 1
# while count < 5:
#     print('''
#       1. Addition 
#       2. Subtraction
#       3. Multiplication
#       4. Division
#       5. Exit
#     ''')
#     print(f"-----attempt-----{count}----remaining attempt-----{5-count}")
#     choice = int(input("Enter your choice: "))

#     if choice == 1:
#         add()
#         count += 1
#     elif choice == 2:
#         a = int(input("Enter first number to subtract: "))
#         b = int(input("Enter second number to subtract: "))
#         sub(a, b)
#         count += 1
#     elif choice == 3:
#         result = mul()
#         print("Multiplication:", result)
#         count += 1
#     elif choice == 4:
#         x = int(input("Enter numerator: "))
#         y = int(input("Enter denominator: "))
#         result = div(x, y)
#         print("Division:", result)
#         count += 1
#     elif choice == 5:
#         print("Exiting... Goodbye!")
#         break
#     else:
#         print("Invalid choice! Please enter a number from 1 to 5.")

# print("Loop completed after 5 valid operations.")



# 1. check the palindrome number using no return with argument.
def palindrome(num):
    rev = int(str(num)[::-1])
    if num == rev:
        return f"{num} is a palindrome number."
    else:
        return f"{num} is not a palindrome number."
num = int(input("Enter a number: "))
print(palindrome(num))




# 2. WAP to check the prime number using no return type with argument.
def prime(num):
    if num >0:
        for i in range(2, num):
            if (num % i) == 0:
                return f"{num} is not a prime number."
            else:
                return f"{num} is a prime number."
num=int(input("enter the number "))            
print(prime(num))           




# 3. WAP to check the Armstrong number using no return type with argument.
def armstrong(num):
    num1 = num
    sum = 0
    while num1 != 0:
        rem = num1 % 10
        sum = sum + rem ** 3
        num1 = num1 // 10
        if num == sum:
            return f"{num} is an Armstrong number."
        else:
            return f"{num} is not an Armstrong number."
num = int(input("Enter a number: "))
print(armstrong(num))

# 4. WAP to print the factorial number of any inputted number using no return type with argument.
# Function with no return type, with argument
def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    print(f"Factorial of {num} is {fact}")
number = int(input("Enter a number: "))
factorial(number)  # Call the function with an argument

# 5. WAP to print the fibonnoci series of any inputted number using no return type with argument
def fibonnoci(num):
    if num == 0:
        return f"Fibonnoci series of {num} is 0."
    elif num == 1:
        return f"Fibonnoci series of {num} is 0, 1."
    else:
        fib = [0, 1]
        for i in range(2, num):
            fib.append(fib[i - 1] + fib[i - 2])
            return f"Fibonnoci series of {num} is {fib}."
num = int(input("Enter a number: "))
print(fibonnoci(num))

