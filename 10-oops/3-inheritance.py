# what is inheritance 

'''
inheratiance allows us to create class which inherits all 
the methods and properties form prent class to child class

types of inheritance 
1 single inheritance 
2 multi level inheritabnce 
3 multiple inheretance
4 hierarchical inheritance 
5 hybrid inheitance 


'''

class A : #preant class 
    def feature(self):
        print("this is from g=ferature1 ")
    def feature2(self):
        print("this is from g=ferature2 ")

class B (A): #child class 
    def feature3(self):
        print("this is from g=ferature3 ")
    def feature4(self):
        print("this is from g=ferature4 ")

ob=B()
ob.feature()
ob.feature2()
ob.feature3()
ob.feature4()

# single inheritance 

# there are only one preant class and one child class 
class parent():
    def display(self):
        print("this is parent")
class child(parent):   
    def dis2(self):
        print("this is child ")    
      
ob=child()
ob.display()
ob.dis2()



class emp:
    def __init__(self,name,id):
        self.name=name
        self.id=id
class programmer (emp):
    def display(self):
        print(f"the name of empoyyee is name {self.name}")
        print(f"the name of empoyyee is id {self.id}") 

ob=programmer("Bhupendra",11)
ob.display()
        

# mlutiple inheritance 


class pr1:
    def method1(self):
        print("this is pr1")
class pr2 :
    def method2(self):
        print("this is pr2")

class child (pr1,pr2):
    def method3(self):
        print("this is child ")

ob=child()
ob.method1()
ob.method2()
ob.method3()


# multi level inheritance 

# class inherite form other class form itself another class 

class grdpra:
    def method1(self):
        print("this grand preant class")
class pra(grdpra):
    def method2(self):
        print("this is preant ")
class child(pra):
    def method3(self): 
        print("this is child ")

ob=child()
ob.method1()
ob.method2()
ob.method3()

# hierarchical inheritance 
# two child class one pratent class 
# mulitpla child class inhert form single preant class 

class parent:
    def method1(self):
        print("this is parent ")
class child1(parent):
    def method2(self):
        print("this is child 1")   
class child2(parent):
    def method3(self):
         print("this is second child")            

ob=child1()
ob1=child2()
ob.method1()         
ob.method2()
ob1.method1()
ob1.method3()


# hybride inheritance 
#combination of 2 different inheritance 

# 1.Wap create a parent class that takes a list and finds min and max number and 
# make a child class and print a table of that max and min number.
# Parent class
# Parent class
class Numbers:
    def __init__(self, num_list):
        self.num_list = num_list

    def get_min(self):
        return min(self.num_list)

    def get_max(self):
        return max(self.num_list)

# Child class
class Table(Numbers):
    def show_tables(self):
        min_num = self.get_min()
        max_num = self.get_max()

        print(f"\nTable of Min Number ({min_num}):")
        for i in range(1, 11):
            print(f"{min_num} x {i} = {min_num * i}")

        print(f"\nTable of Max Number ({max_num}):")
        for i in range(1, 11):
            print(f"{max_num} x {i} = {max_num * i}")

# Example
numbers = [5, 12, 3, 9, 20]
t = Table(numbers)
t.show_tables()


# 2.Create a class that takes a string and counts the number of vowels and consonants. 
# then create a derived class that prints these counts and also prints the string in reverse.
        
# Parent class
class MyString:
    def __init__(self, text):
        self.text = text

    def count_vowels(self):
        count = 0
        for ch in self.text.lower():
            if ch in "aeiou":
                count += 1
        return count

    def count_consonants(self):
        count = 0
        for ch in self.text.lower():
            if ch.isalpha() and ch not in "aeiou":
                count += 1
        return count

# Child class
class MyStringDetails(MyString):
    def show_info(self):
        vowels = self.count_vowels()
        consonants = self.count_consonants()
        reversed_text = self.text[::-1]

        print("Original String:", self.text)
        print("Number of Vowels:", vowels)
        print("Number of Consonants:", consonants)
        print("Reversed String:", reversed_text)

# Example
s = MyStringDetails("Python Programming")
s.show_info()


# 4.Create a class that takes a string and checks whether it is a palindrome.
# Then, create a derived class that also counts the number of uppercase and lowercase letters.
# Base class
# class CheckPalindrome:
#     def __init__(self, text):
#         self.text = text

#     def is_palindrome(self):
#         return self.text == self.text[::-1]

# # Derived class
# class CountCases(CheckPalindrome):
#     def count_upper_lower(self):
#         upper = 0
#         lower = 0
#         for ch in self.text:
#             if ch.isupper():
#                 upper += 1
#             elif ch.islower():
#                 lower += 1
#         print("Uppercase letters:", upper)
#         print("Lowercase letters:", lower)

# # Taking input
# s = input("Enter a string: ")
# obj = CountCases(s)

# # Output
# if obj.is_palindrome():
#     print("It is a palindrome.")
# else:
#     print("It is not a palindrome.")

# obj.count_upper_lower()




##### SUPER METHOD #####


class person:
    def __init__(self,name ,age):
        self.name=name
        self.age=age
class emp(person):
    def __init__(self, name, age,salary):
        super().__init__(name, age)
        self.salary=salary

    def cla_bonus(self):
        bonus=0.10*self.salary
        print(f"the name of emp {self.name} and bonus is {bonus}")


ob=emp("naman",25,55000)
ob.cla_bonus()       


# 2.Create 3 class person(name,age), student(grade) and teacher(subject) perform Hierarchical Inheritance 
#    and print the information of student and teacher. Use super method.

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class student(person):
    def __init__(self, name, age,grade):
        super().__init__(name, age)      
        self.grade=grade 

class teacher(person):
    def __init__(self, name, age,subject):
        super().__init__(name, age)
        
        self.subject=subject
    def display(self):
        print(f"The name of student is {self.name}")
        print(f"The age of student is {self.age}")
        # print(f"the gread is {self.grade}")
        print(f"the subject is {self.subject}")

ob=teacher("koli",20,"math")
ob.display()


# 3.Define a class Vehicle with attributes for brand and year.
# Implement a subclass Car that adds an attribute for mileage and a 
# method to calculate the fuel cost for a trip given a distance and cost per kilometer

class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

class Car(Vehicle):
    def __init__(self, brand, year, mileage):
        super().__init__(brand, year)
        self.mileage = mileage

    def fuel_cost(self, distance, cost_per_km):
        return distance * cost_per_km

    def display_details(self, distance, cost_per_km):
        print("Brand:", self.brand)
        print("Year:", self.year)
        print("Mileage:", self.mileage, "km/l")
        cost = self.fuel_cost(distance, cost_per_km)
        print(f"Fuel cost for {distance} km: ₹{cost}")

car1 = Car("Toyota", 2022, 18)
car1.display_details(150, 5)  

# 4.Define a class Appliance with attributes for brand and power (in watts).
# Implement a subclass WashingMachine that adds an attribute for capacity (in kg) and a method to calculate electricity usage for a given number of hours.


class Appliance:
    def __init__(self, brand, power):
        self.brand = brand
        self.power = power 

class WashingMachine(Appliance):
    def __init__(self, brand, power, capacity):
        super().__init__(brand, power)
        self.capacity = capacity 

    def elect(self, hours):
        usage = (self.power / 1000) * hours
        return usage

    def display(self, hours):
        print("Brand:", self.brand)
        print("Power:", self.power, "watts")
        print("Capacity:", self.capacity, "kg")
        print("Usage Time:", hours, "hours")
        usage = self.elect(hours)
        print(f"Electricity used: {usage:.2f} kWh")

ob = WashingMachine("LG", 2000, 7)  
ob.display(3)  



# Create a base class Person with attributes:name,age

# Create a class Student that inherits from Person and has:roll_number

# Create a class Teacher that also inherits from Person and has:subject

# Create a class TeachingAssistant that inherits from both Student and Teacher.

# The TeachingAssistant class should have a method display_info() that prints:Name, Age, Roll Number, and Subject.


# Base class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Student inherits from Person
class Student(Person):
    def __init__(self, name, age, roll_number):
        Person.__init__(self, name, age)
        self.roll_number = roll_number

# Teacher inherits from Person
class Teacher(Person):
    def __init__(self, name, age, subject):
        Person.__init__(self, name, age)
        self.subject = subject

# TeachingAssistant inherits from both Student and Teacher
class TeachingAssistant(Student, Teacher):
    def __init__(self, name, age, roll_number, subject):
        Student.__init__(self, name, age, roll_number)
        Teacher.__init__(self, name, age, subject)

    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll Number:", self.roll_number)
        print("Subject:", self.subject)

# Example usage
ta = TeachingAssistant("Rahul", 22, "CS101", "Python Programming")
ta.display_info()

