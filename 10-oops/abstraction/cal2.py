from cal1 import my_claculator

class implementation(my_claculator):


    def add(self):
        num1=int(input("enter the num1:- "))
        num2=int(input("enter the num2:- "))
        res=num1+num2
        print(f"the addtion of {num1} and {num2} is {res}")

    def sub(self):
        num1=int(input("enter the num1:- "))
        num2=int(input("enter the num2:- "))
        res=num1-num2
        print(f"the subration of {num1} and {num2} is {res}")

    def div(self):
        num1=int(input("enter the num1:- "))
        num2=int(input("enter the num2:- "))
        res=num1/num2
        print(f"the division of {num1} and {num2} is {res}") 

    def mul(self):
        num1=int(input("enter the num1:- "))
        num2=int(input("enter the num2:- "))
        res=num1*num2
        print(f"the multipication of {num1} and {num2} is {res}")    

