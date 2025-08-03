# Encapsulation 
# access modifiers 
'''
public AM :- it can be assess any wah
Definition: No underscore before the variable name.
Access: Can be accessed and modified from anywhere.

Protected AM :- start with single undeerscoure(_)

Definition: One underscore before the name: _variable
Access: Can be accessed outside, but should not be modified directly. It's a convention, not a rule.



Private AM :- start with Double underscoure(__)
they can not be assess outside of the class 
Definition: Two underscores before the name: __variable
Access: Cannot be accessed directly from outside. Python uses name mangling to make it harder to access.



'''

class student:
    def __init__(self,name,age):
        self.name=name
        self.__age=age  # private variable 
    def get_age(self):    
        return self.__age
    def set_age(self,age):
        if 0 < age < 100:
            self.__age=age
        else:
            print("Invalide age")    
        

ob=student("jay",20)
print(ob.get_age())
ob.set_age(56)
print(ob.get_age())

#Create a class BankAccount and 
# private attribiutes account_no,account_holder,balance.
# Display and modify the attributes by using Encapsuation.
class BankAccount:
    def __init__(self, account_no, account_holder, balance):
        self.__account_no = account_no          # private
        self.__account_holder = account_holder  # private
        self.__balance = balance                # private

    def show_details(self):
        print("Account No:", self.__account_no)
        print("Account Holder:", self.__account_holder)
        print("Balance: ₹", self.__balance)


    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance!")


acc = BankAccount("12345", "Amit", 5000)

acc.show_details()

acc.deposit(1000)
acc.withdraw(2000)
acc.show_details()


class BankAccount:
    def __init__(self, account_no, account_holder, balance):
        self.__account_no = account_no
        self.__account_holder = account_holder
        self.__balance = balance

    def get_account_no(self):
        return self.__account_no

    def get_account_holder(self):
        return self.__account_holder

    def get_balance(self):
        return self.__balance

    def set_account_holder(self, name):
        self.__account_holder = name

    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Invalid amount")

acc = BankAccount("12345", "Amit", 5000)
print("Account No:", acc.get_account_no())
print("Account Holder:", acc.get_account_holder())
print("Balance: ₹", acc.get_balance())

acc.set_account_holder("Rahul")
acc.set_balance(7000)

print("\n--- After Update ---")
print("Account No:", acc.get_account_no())
print("Account Holder:", acc.get_account_holder())
print("Balance: ₹", acc.get_balance())

# Create car class and private attributes make,model,year,milage.
# Perform this through Encapsulation.

class Car:
    def __init__(self, make, model, year, mileage):
        self.__make = make        # private
        self.__model = model      # private
        self.__year = year        # private
        self.__mileage = mileage  # private

    # Getter methods
    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_mileage(self):
        return self.__mileage

    # Setter methods
    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_year(self, year):
        self.__year = year

    def set_mileage(self, mileage):
        if mileage >= 0:
            self.__mileage = mileage
        else:
            print("Invalid mileage")

# Create object of Car
car1 = Car("Toyota", "Camry", 2020, 15000)

# Display car details using getters
print("Make:", car1.get_make())
print("Model:", car1.get_model())
print("Year:", car1.get_year())
print("Mileage:", car1.get_mileage(), "km")

# Modify some details using setters
car1.set_make("Honda")
car1.set_model("Civic")
car1.set_mileage(18000)

# Display updated details
print("\n--- Updated Car Details ---")
print("Make:", car1.get_make())
print("Model:", car1.get_model())
print("Year:", car1.get_year())
print("Mileage:", car1.get_mileage(), "km")
