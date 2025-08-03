# Exception Handling 
'''
excepetion handling is nothing but unwanted event that occurs during 
the execution of a program and interrupts the flow of the program 
By using exception handling we can handle those exception by using :
1. Try Block
2. Except Block
3. Else Block
4. Finally Block


'''
# try block except block
'''
try :
      # code may that cause error

except:
      # code runs if error occour      



'''
try:
    print("hello")
except:
    print("error to handle ")

# try:
#     print(a)
# except:
#     print("error occurs ")            


x=3
try:
    print("the value of 3*3*3 =",x**x)
except:
    print("error")    
else:
    print("no error")    
finally:
    print("always excutes")

# output
# the value of 3*3*3 = 27
# no error
# always excutes


# zeroDivisionError 




# try:
#     x=int(input("enter the number "))
#     y=int(input("enter the number"))
#     print(x/y)
# except ZeroDivisionError:
#     print("you can not divided by zero ")
# else:
#     print("No error ")        


# try:
#     x=int(input("enter the number "))
#     y=int(input("enter the number"))
#     print(x/y)
# except:
#     print("you can not divided by zero ")
# else:
#     print("No error ")        


# try:
#     x=int(input("enter the number "))
#     y=int(input("enter the number"))
#     print(x/y)
# except ZeroDivisionError:
#     print("you can not divided by zero ")
# except ValueError:
#     print("enter the valid number")
# else:
#     print("No error ")    
# finally:
#     print("always excute ")    


# 1. First Element of the List
#    - Input: A list.
#    - Output: The first element of the list, or a custom message 
#     if the list is empty.
#    - Example:
#      - Input: [1, 2, 3]
#      - Output: 1
#      - Input: []
#      - Output: "The list is empty"


a=[1,2,3,4]
try:
    print(a[0])
except:
    print("the list is empty ")  


# 2. Convert List Elements to Integers
#    - Input: A list of strings.
#    - Output: A list of integers, or a custom message if conversion fails.
#    - Example:
#      - Input: ["1", "2", "three"]
#      - Output: "Error: Cannot convert all elements to integers"


a=["1", "2", "three"]
try:
    print(int(a))
except:
    print("Error: Cannot convert all elements to integers")    

try:
    list1=[1,2,"three"]
    res=(int (i)for i in list1)
    print(res)
except:
    print("Error: Cannot convert all elements to integers")    

# 3. Access Element at Index
#    - Input: A list and an index.
#    - Output: The element at the specified index, or a custom message if the index is out of bounds.
#    - Example:
#      - Input: [1, 2, 3], 1
#      - Output: 2
#      - Input: [1, 2, 3], 5
#      - Output: "Index out of range"


try:
    a=[1, 2, 3], 5
    b=a[a]
    print(b)
except:
    print("Index out of range")    


# 4. Find the Maximum Element in a List
#    - Input: A list of integers.
#    - Output: The maximum element, or a custom message if the list is empty.
#    - Example:
#      - Input: [1, 2, 3]
#      - Output: 3
#      - Input: []
#      - Output: "The list is empty


# try:
#     a=list(input("enter the list "))
#     print(max(a))
# except:
#     print("this list is empty ")    


# Raise keyword 
'''
This statement is used to explicitly trigger an exception, 
which can be a built-in exception or a custom user-defined exception.
'''
# try:
#     age=int(input("enter the age "))
#     if age < 18:
#         raise ValueError ("you are underaged")
#     else:
#         print("you are eligibla for voting")
# except ValueError as e:
#     print("error ",e )


# Write a program that asks for a password. If the password is less than 6 characters, 
# raise a ValueError with message "Password too short" and handle it.
try:
    password=input("enter the password ")
    if len(password) < 6 :
        raise ValueError ("password is to short enter the new password")
    else :
        print("your password is strong ")
except ValueError as a:
    print("error",a)        

# Write a function check_marks(marks) where marks must be between 0 and 100. Raise ValueError if the marks are outside this range.
try :
    marks=int(input("enter the mark"))
    if marks > 100:
        raise ValueError (" the marks cant greater than 100")
    elif marks < 0:
        raise ValueError (" the marks cant lass than 0")
    else:
        print("the mark is ",marks)
except ValueError as a:
    print("error",a)

# using finction 
def get_marks():
    try:
        marks = int(input("Enter the mark: "))
        
        if marks > 100:
            raise ValueError("The marks can't be greater than 100")
        elif marks < 0:
            raise ValueError("The marks can't be less than 0")
        else:
            print("The mark is", marks)
    
    except ValueError as e:
        print("Error:", e)
        
get_marks()
