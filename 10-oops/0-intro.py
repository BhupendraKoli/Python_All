# what is oops 
# Object-Oriented Programming. It is a programming paradigm that organizes software design around data, or objects, rather than functions and logic. 

'''
why use the oops:-
it increses the readability of the code 
the code is in the stryctured form 
it make code more re useable and easier to work with the large program 



Classes:
class is a blue print of object 
it is not a real entity 

Blueprints for creating objects. 
They define attributes (data) and methods (functions) that objects of that class will possess.


Objects:
it is real entity which has its own identity ,state and behaviour 
it is a instances/object of a class 


Instances of a class. 
They are created based on the class blueprint and contain their own unique data and 
can utilize the methods defined in their class.


There are four pillares in oops
 1 Inheritance
 2 Abstraction
 3 Polymorphism 
 4 Encapsulation


'''

class palindrom:
    def get_palindrom(self,num):
        temp=num
        rev=0
        while temp != 0:
            digit=temp % 10
            rev=rev*10+digit
            temp=temp//10
        if rev==num:
            print("palindrom")
        else:
            print("not palindrom")

ob=palindrom()
ob.get_palindrom(121)


# wap takes the no as an argumanet and check it is armstron or not 

class armstrong:
    def get_arm(self,num):
        temp=num
        s=0
        p=len(str(num))
        while temp != 0:
            digit=temp%10
            s=s+digit**p
            temp=temp//10 
        if num == s:
            print(num,"is armstrong number")
        else:
            print(num,"is not armstrong")

ob=armstrong()
ob.get_arm(131)                
