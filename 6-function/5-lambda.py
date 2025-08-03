# lambda function 
'''
lambda is a small and anonymus function.
The word anonymous means without a name or not identified by name. It comes from the Greek roots "an-" (meaning "without") and "onyma" (meaning "name").
In Python, a lambda function is a small anonymous function that can take any number of arguments, but
can only have one expression.

it is a single expression, which can take any number of arguments, but can only have one expression
it is used to define small functions, which can be passed around as arguments to higher-order functions.



syntax :-

lambda arguments : expression

'''
# example of lambda function
x = lambda a, b : a + b
print(x(5, 7))  # output: 12

add= lambda x,y,z: x+y+z
print(add(4,5,6))

res=lambda a,b, c: a*b*c 
print(res(1,2,3))



# 1.Create a lambda function to add two numbers.
add= lambda a,b : a+b
print(add(5,60))

# 2.Create a lambda function to find the square of a number(take user input)
square=lambda x:x**2
num=int(input("enter a number: "))
print(square(num))

# 3.Print the cube of numbers from 1 to 5 using a lambda in a for loop.
cube=lambda x:x**3
for i in range(1,6):
    print("the cube of ",i,"is ",cube(i))

# 4.Use a lambda to check if a number is even or odd
even=lambda x:x%2==0

num=int(input("enter a number: "))
if even(num):
    print(num,"is even")
else:
    print(num,"is odd")

# 5.Use a lambda function to multiply each number in a list by 10
numbers=[1,2,3,4,5]
multi=lambda x:x*10
for i in numbers:
    print(multi(i))

