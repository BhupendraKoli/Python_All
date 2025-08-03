# what is constructure 
'''
init is a constructer which is used for intizilation

constructer is the way by which you will be able to provide
data to a class

is sepecile method in oops that is automaticily called whenan object 
of a class id created

'''
# class car:
#     def __init__(self,brand,color):
#         self.brand=brand
#         self.color=color

#     def disply(self):
#         print(f"the brand is {self.brand} and the color is {self.color}")

# ob=car("TATA","Black")
# ob.disply()



# Task:
# 1.Create a BankAccount class with a constructor that initializes 
# the account holder's name 
# and initial balance. Implement methods to deposit and withdraw money.

class bankacount:
    def __init__(self,holdername,blance):
        self.holdername=holdername
        self.blance=blance
    def dislply(self):
        print(f"the account holder name is {self.holdername} and tha blance of the acount is {self.blance}")
    def deop(self,amount):
        self.blance=self.blance+amount
        print(f" the diposited amount is {amount} the total is {self.blance}")
    def witd(self,amount1):
        if amount1 > self.blance:
            print("insifecient blance ")
        else:
            self.blance=self.blance-amount1
            print(f"the withrdro amount is {amount1} tatal ramaing balnce {self.blance}")


a=bankacount("Bhupendra",15000)
a.dislply()
a.deop(500)
a.witd(1000)
a.dislply()


# 2.Create a Student class with a constructor that takes the student's name and marks in three subjects. 
# Implement a method to calculate the average marks and determine the grade based on the average.

class Student:
    def __init__(self, name, mark1, mark2, mark3):
        self.name = name
        self.marks = [mark1, mark2, mark3]

    def calculate_average(self):
        return sum(self.marks) / len(self.marks)

    def determine_grade(self):
        avg = self.calculate_average()

        if avg >= 90:
            return "A+"
        elif avg >= 80:
            return "A"
        elif avg >= 70:
            return "B"
        elif avg >= 60:
            return "C"
        elif avg >= 50:
            return "D"
        else:
            return "F"

    def display_result(self):
        avg = self.calculate_average()
        grade = self.determine_grade()
        print(f"Student: {self.name}")
        print(f"Average Marks: {avg:.2f}")
        print(f"Grade: {grade}")

# Example usage:
student1 = Student("Bhupendra", 85, 90, 78)
student1.display_result()

# 3.Create a Rectangle class with a constructor that initializes the length and width. 
# Implement methods to calculate the area and perimeter of the rectangle.
        

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

# Example usage:
rect = Rectangle(10, 5)
print(f"Area: {rect.calculate_area()}")
print(f"Perimeter: {rect.calculate_perimeter()}")



