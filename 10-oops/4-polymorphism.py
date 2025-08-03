# Polymorphism 
'''
# Poly - many 
# morphism - forms

It provides a way to perform single operation in diffrent forms 

1 method over loading 
2 method over riding 

we can achieved the # Polymorphism through mothed over riding 

two class 
method name same 
inheritance there 

'''
# method over riding :-
# method name is same and inhertance must be there 

class animal:
    def speck(self):
        print ("animal speck ")
class dog(animal):
    def speck(self):
        print("dog barks")
class cat (animal):
    def speck(self):
        print("cats mewo")           

ob1=dog()
ob1.speck()

ob2=cat()
ob2.speck()


# 1. Define a class Person with attributes for name and age.
#    Implement a subclass Employee with attributesemp_id, department.
#    Use method-overiding.

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class emp(person):
    def __init__(self,name,age,id,deparment ):
        super().__init__(name,age)
        self.id=id
        self.deparment=deparment

    def disply(self):
        print(f"the emp name {self.name} age {self.age}")
        print(f"the emp id {self.id} and department {self.deparment}")

ob1=emp("ram",20,201,"computer")
ob1.disply()

# 2. Define a class device brand and price.
#    Implement a subclass laptop with RAM and processor.
#    Overrides a method specification() to display all details.

# Base class
class Device:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def specification(self):
        print(f"Brand: {self.brand}")
        print(f"Price: ₹{self.price}")

# Subclass
class Laptop(Device):
    def __init__(self, brand, price, ram, processor):
        super().__init__(brand, price)
        self.ram = ram
        self.processor = processor

    def specification(self):  # Overriding the method
        super().specification()  # Call base class method
        print(f"RAM: {self.ram} GB")
        print(f"Processor: {self.processor}")

# Test
l1 = Laptop("HP", 55000, 16, "Intel i5")
l1.specification()

class Device:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def specification(self):
        print(f"The brand is {self.brand} and the price is {self.price}")

class Laptop(Device):
    def __init__(self, brand, price, RAM, proc):
        super().__init__(brand, price)  # Call parent constructor
        self.RAM = RAM
        self.proc = proc

    def specification(self):  # Overriding method
        super().specification()  # Call base class method
        print(f"The RAM is {self.RAM} and the processor is {self.proc}")

# Test
ob1 = Device("Lenovo", 50000)
ob1.specification()

print("----")

ob2 = Laptop("HP", 60000, "16GB", "Intel i7")
ob2.specification()


# 3. Define a class Employee with name,basic_salary.
#    Implement a subclass SalesEmployee with attributes sales_amount and commission_rate,
#    Override calculate_salary() to compute total_salary.
        

class Emp:
    def __init__(self, name, basic_salary):
        self.name = name
        self.basic_salary = basic_salary

    def calculate(self):
        print(f"The name is {self.name}")
        print(f"The basic salary is {self.basic_salary}")

class SalesEmp(Emp):
    def __init__(self, name, basic_salary, commission_rate, sales_amount):
        super().__init__(name, basic_salary)
        self.commission_rate = commission_rate
        self.sales_amount = sales_amount

    def calculate(self):
        super().calculate()
        total = (self.commission_rate * self.sales_amount) + self.basic_salary
        print(f"The total salary is {total}")

# Correct order of arguments: name, basic_salary, commission_rate, sales_amount
ob = SalesEmp("Bhupendra", 20000, 50, 500000)
ob.calculate()


# 4. Define a classStudent has name and marks (list of 3 subjects)
#    Method calculate_percentage() in Student gives average.
#    EngineeringStudent adds 2 more marks (for lab subjects) and overrides percentage logic.
#    Use super().calculate_percentage() to get base average and then compute combined
        
class student :
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark

    def claculate_precentage(self):
        avg=sum(self.mark) / len(self.mark) 
        print (f"The name of the sutudent is {self.name}")
        print(f"The three subject precentage is {avg}")
class engstudent(student):
    def __init__(self, name, mark,lab_mark):
        super().__init__(name, mark)
        self.lab_mark=lab_mark
    def claculate_precentage(self):
        super().claculate_precentage()
        total_marks = self.mark + self.lab_mark
        combined_avg = sum(total_marks) / len(total_marks)
        print(f"the total avg {combined_avg}") 

ob=engstudent("Bhupendra ",[90,95,70],[84,92])
ob.claculate_precentage()
                  
