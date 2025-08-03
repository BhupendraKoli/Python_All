# with argument with raturn type 
# a function which take parameter and return data 
def get_data(name, age, gender):
    return f"Name: {name}, Age: {age}, Gender: {gender}"
# calling the function with argument
print(get_data("John", 25, "Male"))

def add(num1,num2,):
    return num1 + num2
print(add(12,3))

'''
you have to take a user input as choice 
if choice==1 to add() function execute 
if choice==2 to sub() function execute 
if choice==3 to mul() function execute 
if choice==4 to div() function execute 

add() no argument no return type 
sub() with argument no return type
mul() no argument with return type
div()  argument with return type 

'''
# 1. No argument, no return type
def add():
    a = int(input("Enter first number to add: "))
    b = int(input("Enter second number to add: "))
    print("Addition:", a + b)

# 2. With argument, no return type
def sub(a, b):
    print("Subtraction:", a - b)

# 3. No argument, return type
def mul():
    x = int(input("Enter first number to multiply: "))
    y = int(input("Enter second number to multiply: "))
    return x * y

# 4. With argument and return type
def div(x, y):   
   return x/y

print('''
      1 addition 
      2 substraction
      3 multiplication
      4 division
''')
choice = int(input("Enter your choice: "))

if choice == 1:
    add()
elif choice == 2:
    a = int(input("Enter first number to subtract: "))
    b = int(input("Enter second number to subtract: "))
    sub(a, b)
elif choice == 3:
    result = mul()
    print("Multiplication:", result)
elif choice == 4:
    x = int(input("Enter numerator: "))
    y = int(input("Enter denominator: "))
    result = div(x, y)
    print("Division:", result)
else:
    print("Invalid choice!")



def add():
    a = int(input("Enter first number to add: "))
    b = int(input("Enter second number to add: "))
    print("Addition:", a + b)

def sub(a, b):
    print("Subtraction:", a - b)

def mul():
    x = int(input("Enter first number to multiply: "))
    y = int(input("Enter second number to multiply: "))
    return x * y

def div(x, y):   
    return x / y
count = 0
while count <= 5:
    print('''
      1. Addition 
      2. Subtraction
      3. Multiplication
      4. Division
      5. Exit
    ''')

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add()
    elif choice == 2:
        a = int(input("Enter first number to subtract: "))
        b = int(input("Enter second number to subtract: "))
        sub(a, b)
    elif choice == 3:
        result = mul()
        print("Multiplication:", result)
    elif choice == 4:
        x = int(input("Enter numerator: "))
        y = int(input("Enter denominator: "))
        result = div(x, y)
        print("Division:", result)   
    elif choice == 5:
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")


        