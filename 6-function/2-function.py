 # 2 No argument with return type
# a function has no parameter but it will return data 
def greet():
    return "Hello, how are you?"
print(greet()) # Hello, how are you?

# future operation using return data 
s=greet()
final=s+ " mansi "
print(final) # Hello, how are you? mansi


def add():
    num1=int(input("enter the first number "))
    num2=int(input("enter the second number "))
    return num1+num2

print(add()) # 10

# identify the number is even or odd 
def check():
    num=int(input("enter the number "))
    if num % 2==0:
        return "number is even"
    else:
        return "number is odd"
print(check())    
