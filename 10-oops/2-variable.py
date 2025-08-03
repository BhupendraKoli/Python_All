# Type of variables
 # 1 Class variable 
     # that store in the class 
 # 2 Instance Variable
      # that store in the method 

# Type of Method
 # 1 Class method 
''' # its come with cls keyword
    # get the details of class lavel variable 
    # use to access the class lavel veriable 
    # and need to diclere @classmethod class methd decoreter'''
 # 2 Instanve method 
''' # its come with the self keyword only
    # to get the detils of intances that menas the object
    # work with the instance variable'''
 # 3 static method 
''' # Doesn't take self or cls.
    # Cannot access instance or class variables directly.
    # Used for utility functions that are related to the class but don't need instance or class data.
    # Declared using the @staticmethod decorator
'''


class student:
    school="codenera"
    def __init__(self,name,m1,m2,m3):
        self.name=name
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    
    @classmethod
    def get_school(cls):
        return (cls.school)
    
    @staticmethod
    def info():
        print("this class of student ")



    
ob=student("koli",10,20,30)
print(ob.avg())    # instance methode
print(student.get_school()) # class method 
ob.info() # statice method 
        
# 1.Write a Python class Student with instance variables name and marks. 
# Add an instance method display() that prints the student's details.


class student:
    def __init__(self,name , mark ):
        self.name=name
        self.mark=mark
    def display(self):
        print(f"The name of the student is {self.name} \n The mark he get in exam {self.mark}")    

ob=student("Bhupendra",95)
ob.display()

# 2.Modify the Student class to include a method update_marks(new_marks), which updates the marks of a student.


class student:
    def __init__(self,name , mark ):
        self.name=name
        self.mark=mark
    def update_mark(self,update):
        self.update=update
        
            
    def display(self):
        print(f"The name of the student is {self.name} \n The mark he get in exam {self.mark} \n the updated mark is {self.update}")    


a=student("Bhupendra",95)
a.update_mark(97)
a.display()


# 3.Define a class Company with a class variable company_name = "TechCorp". 
# Add a class method set_company_name(cls, new_name) to change the company name.


class company:
    company_name = "TechCorp"
    @classmethod
    def set_company_name(cls, new_name):
        cls.new_name=new_name
        return (f"the old name of compny is {cls.company_name} and the new name is {new_name}")

print(company.set_company_name("koli"))    


# 4.Create a class Person with name and age attributes.
# Add a class method from_birth_year(cls, name, birth_year) that calculates the age from the birth year.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        current_year = 2025 
        age = current_year - birth_year
        return cls(name, age)

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

ob=Person.from_birth_year("Bhupendra",2004)
ob.display()
 
  # 6.Create a class Vehicle with:
# --Instance attributes brand and model.
# --A class method set_default_brand(cls, brand_name).
# --A static method is_motor_vehicle(wheels) that returns True if wheels > 2.


class vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    @classmethod
    def  set_default_brand(cls, brand_name) :
        cls.brand_name=brand_name
        print(f"the brand is {brand_name}")
    @staticmethod
    def is_motor_vehicle(wheels):
        if wheels > 2:
            print("True")
        else:
            print("Flase")

ob=vehicle("Tata","B6")
ob.is_motor_vehicle(5)                
        
# 5.Define a class MathOperations that includes a static method add(x, y) which returns the sum of x and y.

class mathop:
    @staticmethod
    def add(x,y):
        return x+y    

ob=mathop
print(ob.add(2,3))