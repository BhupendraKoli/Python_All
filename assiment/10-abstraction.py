### Question 1: Basic Calculator
# Create a basic calculator program that offers a menu with the following options:
# 1. Addition
# 2. Subtraction
# 3. Multiplication
# 4. Division
# 5. Exit

# The program should prompt the user to enter two numbers and perform the selected operation.
# using abstraction in python 

from abc import ABC, abstractmethod

# Abstract class
class Calculator(ABC):
    @abstractmethod
    def calculate(self, a, b):
        pass

# Concrete classes
class Addition(Calculator):
    def calculate(self, a, b):
        return a + b

class Subtraction(Calculator):
    def calculate(self, a, b):
        return a - b

class Multiplication(Calculator):
    def calculate(self, a, b):
        return a * b

class Division(Calculator):
    def calculate(self, a, b):
        if b == 0:
            return "Error: Division by zero!"
        return a / b

# Menu-based interface
def main():
    while True:
        print("\n--- Basic Calculator ---")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '5':
            print("Exiting the calculator. Goodbye!")
            break

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                operation = Addition()
            elif choice == '2':
                operation = Subtraction()
            elif choice == '3':
                operation = Multiplication()
            elif choice == '4':
                operation = Division()
            else:
                print("Invalid choice. Try again.")
                continue

            result = operation.calculate(num1, num2)
            print("Result:", result)

        except ValueError:
            print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()


### Question 2: Area Calculator
# Create a program that calculates the area of different shapes. The menu should include:
# 1. Area of a Circle
# 2. Area of a Rectangle
# 3. Area of a Triangle
# 4. Exit

# The program should prompt the user for the necessary dimensions (e.g., radius, width, height, base) to compute the area.

from abc import ABC, abstractmethod
import math

# Abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Circle class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

# Rectangle class
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Triangle class
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# Menu-driven program
def main():
    while True:
        print("\n--- Area Calculator ---")
        print("1. Area of a Circle")
        print("2. Area of a Rectangle")
        print("3. Area of a Triangle")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            try:
                radius = float(input("Enter radius of the circle: "))
                shape = Circle(radius)
                print("Area of Circle:", shape.area())
            except ValueError:
                print("Invalid input. Please enter numeric values.")
        
        elif choice == '2':
            try:
                width = float(input("Enter width of the rectangle: "))
                height = float(input("Enter height of the rectangle: "))
                shape = Rectangle(width, height)
                print("Area of Rectangle:", shape.area())
            except ValueError:
                print("Invalid input. Please enter numeric values.")

        elif choice == '3':
            try:
                base = float(input("Enter base of the triangle: "))
                height = float(input("Enter height of the triangle: "))
                shape = Triangle(base, height)
                print("Area of Triangle:", shape.area())
            except ValueError:
                print("Invalid input. Please enter numeric values.")

        elif choice == '4':
            print("Exiting Area Calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please select from 1 to 4.")

if __name__ == "__main__":
    main()

# ### Question 3: Temperature Converter
# Create a temperature converter program with the following menu options:
# 1. Celsius to Fahrenheit
# 2. Fahrenheit to Celsius
# 3. Celsius to Kelvin
# 4. Kelvin to Celsius
# 5. Exit

# The program should prompt the user to enter a temperature and then perform the selected conversion.

from abc import ABC, abstractmethod

# Abstract class
class TemperatureConverter(ABC):
    @abstractmethod
    def convert(self, temp):
        pass

# Celsius to Fahrenheit
class CelsiusToFahrenheit(TemperatureConverter):
    def convert(self, temp):
        return (temp * 9/5) + 32

# Fahrenheit to Celsius
class FahrenheitToCelsius(TemperatureConverter):
    def convert(self, temp):
        return (temp - 32) * 5/9

# Celsius to Kelvin
class CelsiusToKelvin(TemperatureConverter):
    def convert(self, temp):
        return temp + 273.15

# Kelvin to Celsius
class KelvinToCelsius(TemperatureConverter):
    def convert(self, temp):
        return temp - 273.15

# Menu-driven program
def main():
    while True:
        print("\n--- Temperature Converter ---")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Celsius to Kelvin")
        print("4. Kelvin to Celsius")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '5':
            print("Exiting Temperature Converter. Goodbye!")
            break

        try:
            temp = float(input("Enter temperature: "))

            if choice == '1':
                converter = CelsiusToFahrenheit()
            elif choice == '2':
                converter = FahrenheitToCelsius()
            elif choice == '3':
                converter = CelsiusToKelvin()
            elif choice == '4':
                converter = KelvinToCelsius()
            else:
                print("Invalid choice. Please select from 1 to 5.")
                continue

            result = converter.convert(temp)
            print("Converted Temperature:", round(result, 2))

        except ValueError:
            print("Invalid input. Please enter a numeric temperature.")

if __name__ == "__main__":
    main()

### Question 4: Unit Converter
# Create a unit converter program with the following menu options:
# 1. Kilometers to Miles
# 2. Miles to Kilometers
# 3. Kilograms to Pounds
# 4. Pounds to Kilograms
# 5. Exit

# The program should prompt the user to enter a value and then perform the selected conversion.


from abc import ABC, abstractmethod

# Abstract class
class UnitConverter(ABC):
    @abstractmethod
    def convert(self, value):
        pass

# Concrete conversion classes
class KmToMiles(UnitConverter):
    def convert(self, value):
        return value * 0.621371

class MilesToKm(UnitConverter):
    def convert(self, value):
        return value / 0.621371

class KgToPounds(UnitConverter):
    def convert(self, value):
        return value * 2.20462

class PoundsToKg(UnitConverter):
    def convert(self, value):
        return value / 2.20462

# Menu-driven program
def main():
    while True:
        print("\n--- Unit Converter ---")
        print("1. Kilometers to Miles")
        print("2. Miles to Kilometers")
        print("3. Kilograms to Pounds")
        print("4. Pounds to Kilograms")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '5':
            print("Exiting Unit Converter. Goodbye!")
            break

        try:
            value = float(input("Enter the value to convert: "))

            if choice == '1':
                converter = KmToMiles()
            elif choice == '2':
                converter = MilesToKm()
            elif choice == '3':
                converter = KgToPounds()
            elif choice == '4':
                converter = PoundsToKg()
            else:
                print("Invalid choice. Please select from 1 to 5.")
                continue

            result = converter.convert(value)
            print("Converted Value:", round(result, 4))

        except ValueError:
            print("Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    main()


# ### Question 5: Loan Calculator
# Create a loan calculator program with the following menu options:
# 1. Calculate Monthly Payment
# 2. Calculate Total Payment
# 3. Exit

# The program should prompt the user to enter the loan amount, annual interest rate, and loan term (in years) to compute the monthly payment and total payment.

from abc import ABC, abstractmethod

# Abstract class
class LoanCalculator(ABC):
    @abstractmethod
    def calculate(self, principal, annual_rate, years):
        pass

# Monthly payment = [P * r * (1 + r)^n] / [(1 + r)^n – 1]
class MonthlyPaymentCalculator(LoanCalculator):
    def calculate(self, principal, annual_rate, years):
        monthly_rate = annual_rate / 100 / 12
        num_payments = years * 12
        if monthly_rate == 0:
            return principal / num_payments
        return (principal * monthly_rate * (1 + monthly_rate) ** num_payments) / ((1 + monthly_rate) ** num_payments - 1)

class TotalPaymentCalculator(LoanCalculator):
    def calculate(self, principal, annual_rate, years):
        monthly_calc = MonthlyPaymentCalculator()
        monthly_payment = monthly_calc.calculate(principal, annual_rate, years)
        return monthly_payment * years * 12

# Menu-driven program
def main():
    while True:
        print("\n--- Loan Calculator ---")
        print("1. Calculate Monthly Payment")
        print("2. Calculate Total Payment")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '3':
            print("Exiting Loan Calculator. Goodbye!")
            break

        try:
            principal = float(input("Enter loan amount (principal): "))
            annual_rate = float(input("Enter annual interest rate (in %): "))
            years = int(input("Enter loan term (in years): "))

            if choice == '1':
                calculator = MonthlyPaymentCalculator()
                result = calculator.calculate(principal, annual_rate, years)
                print(f"Monthly Payment: ₹{round(result, 2)}")
            elif choice == '2':
                calculator = TotalPaymentCalculator()
                result = calculator.calculate(principal, annual_rate, years)
                print(f"Total Payment: ₹{round(result, 2)}")
            else:
                print("Invalid choice. Please select 1 to 3.")
        except ValueError:
            print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()



# ### Question 6: BMI Calculator
# Create a BMI (Body Mass Index) calculator program with the following menu options:
# 1. Calculate BMI
# 2. Exit

# The program should prompt the user to enter their weight (in kilograms or pounds) and height (in meters or inches), then calculate and display the BMI.

from abc import ABC, abstractmethod

# Abstract base class
class BMICalculator(ABC):
    @abstractmethod
    def calculate_bmi(self, weight, height):
        pass

# BMI = weight (kg) / height² (m²)
class MetricBMICalculator(BMICalculator):
    def calculate_bmi(self, weight, height):
        return weight / (height ** 2)

# BMI = 703 * weight (lbs) / height² (in²)
class ImperialBMICalculator(BMICalculator):
    def calculate_bmi(self, weight, height):
        return 703 * weight / (height ** 2)

# Function to interpret BMI result
def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

# Menu-driven program
def main():
    while True:
        print("\n--- BMI Calculator ---")
        print("1. Calculate BMI")
        print("2. Exit")

        choice = input("Enter your choice (1-2): ")

        if choice == '2':
            print("Exiting BMI Calculator. Stay healthy!")
            break

        print("\nSelect Unit System:")
        print("1. Metric (kg, meters)")
        print("2. Imperial (pounds, inches)")
        unit_choice = input("Enter unit system (1 or 2): ")

        try:
            weight = float(input("Enter your weight: "))
            height = float(input("Enter your height: "))

            if unit_choice == '1':
                calculator = MetricBMICalculator()
            elif unit_choice == '2':
                calculator = ImperialBMICalculator()
            else:
                print("Invalid unit system selected.")
                continue

            bmi = calculator.calculate_bmi(weight, height)
            print(f"\nYour BMI is: {round(bmi, 2)}")
            print("Category:", interpret_bmi(bmi))

        except ValueError:
            print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()


### Question 7: Currency Converter
# Create a currency converter program with the following menu options:
# 1. USD to EUR
# 2. EUR to USD
# 3. USD to GBP
# 4. GBP to USD
# 5. Exit

# The program should prompt the user to enter an amount in one currency and convert it to another currency using a predefined exchange rate.

from abc import ABC, abstractmethod

# Abstract base class
class CurrencyConverter(ABC):
    @abstractmethod
    def convert(self, amount):
        pass

# Concrete conversion classes with fixed exchange rates
class UsdToEur(CurrencyConverter):
    def convert(self, amount):
        return amount * 0.85  # Example rate

class EurToUsd(CurrencyConverter):
    def convert(self, amount):
        return amount * 1.18  # Example rate

class UsdToGbp(CurrencyConverter):
    def convert(self, amount):
        return amount * 0.75  # Example rate

class GbpToUsd(CurrencyConverter):
    def convert(self, amount):
        return amount * 1.33  # Example rate

# Menu-driven program
def main():
    while True:
        print("\n--- Currency Converter ---")
        print("1. USD to EUR")
        print("2. EUR to USD")
        print("3. USD to GBP")
        print("4. GBP to USD")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '5':
            print("Exiting Currency Converter. Goodbye!")
            break

        try:
            amount = float(input("Enter amount to convert: "))

            if choice == '1':
                converter = UsdToEur()
            elif choice == '2':
                converter = EurToUsd()
            elif choice == '3':
                converter = UsdToGbp()
            elif choice == '4':
                converter = GbpToUsd()
            else:
                print("Invalid choice. Please choose from 1 to 5.")
                continue

            converted = converter.convert(amount)
            print("Converted Amount:", round(converted, 2))

        except ValueError:
            print("Invalid input. Please enter a numeric amount.")

if __name__ == "__main__":
    main()


### Question 8: Quadratic Equation Solver
# Create a quadratic equation solver program with the following menu options:
# 1. Solve Quadratic Equation
# 2. Exit

# The program should prompt the user to enter the coefficients (a, b, c) of a quadratic equation (ax^2 + bx + c = 0) and then calculate and display the roots.

from abc import ABC, abstractmethod
import cmath  # for complex number support

# Abstract base class
class QuadraticSolver(ABC):
    @abstractmethod
    def solve(self, a, b, c):
        pass

# Concrete implementation
class EquationSolver(QuadraticSolver):
    def solve(self, a, b, c):
        if a == 0:
            return "Not a quadratic equation (a ≠ 0 required)."

        discriminant = (b ** 2) - (4 * a * c)
        root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
        root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)

        return root1, root2

# Menu-driven interface
def main():
    while True:
        print("\n--- Quadratic Equation Solver ---")
        print("1. Solve Quadratic Equation")
        print("2. Exit")

        choice = input("Enter your choice (1-2): ")

        if choice == '2':
            print("Exiting the program. Goodbye!")
            break

        try:
            a = float(input("Enter coefficient a: "))
            b = float(input("Enter coefficient b: "))
            c = float(input("Enter coefficient c: "))

            solver = EquationSolver()
            result = solver.solve(a, b, c)

            if isinstance(result, str):
                print(result)
            else:
                root1, root2 = result
                print(f"Root 1: {root1}")
                print(f"Root 2: {root2}")

        except ValueError:
            print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()


### Question 9: Speed Calculator
# Create a speed calculator program with the following menu options:
# 1. Calculate Speed (Distance/Time)
# 2. Calculate Distance (Speed*Time)
# 3. Calculate Time (Distance/Speed)
# 4. Exit

# The program should prompt the user to enter the necessary values and perform the selected calculation.

from abc import ABC, abstractmethod

# Abstract base class
class SpeedCalculator(ABC):
    @abstractmethod
    def calculate(self, val1, val2):
        pass

# Concrete calculation classes
class Speed(SpeedCalculator):  # Speed = Distance / Time
    def calculate(self, distance, time):
        if time == 0:
            return "Time cannot be zero."
        return distance / time

class Distance(SpeedCalculator):  # Distance = Speed * Time
    def calculate(self, speed, time):
        return speed * time

class Time(SpeedCalculator):  # Time = Distance / Speed
    def calculate(self, distance, speed):
        if speed == 0:
            return "Speed cannot be zero."
        return distance / speed

# Menu-driven interface
def main():
    while True:
        print("\n--- Speed Calculator ---")
        print("1. Calculate Speed (Distance / Time)")
        print("2. Calculate Distance (Speed * Time)")
        print("3. Calculate Time (Distance / Speed)")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '4':
            print("Exiting Speed Calculator. Goodbye!")
            break

        try:
            if choice == '1':
                distance = float(input("Enter distance (e.g., km): "))
                time = float(input("Enter time (e.g., hours): "))
                calculator = Speed()
                result = calculator.calculate(distance, time)

            elif choice == '2':
                speed = float(input("Enter speed (e.g., km/h): "))
                time = float(input("Enter time (e.g., hours): "))
                calculator = Distance()
                result = calculator.calculate(speed, time)

            elif choice == '3':
                distance = float(input("Enter distance (e.g., km): "))
                speed = float(input("Enter speed (e.g., km/h): "))
                calculator = Time()
                result = calculator.calculate(distance, speed)

            else:
                print("Invalid choice. Please select from 1 to 4.")
                continue

            print("Result:", result)

        except ValueError:
            print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()


### Question 10: Age Calculator
# Create an age calculator program with the following menu options:
# 1. Calculate Age
# 2. Exit

# The program should prompt the user to enter their birthdate and then calculate and display their age in years, months, and days.

from abc import ABC, abstractmethod
from datetime import datetime, date

# Abstract base class
class AgeCalculator(ABC):
    @abstractmethod
    def calculate_age(self, birthdate):
        pass

# Concrete implementation
class SimpleAgeCalculator(AgeCalculator):
    def calculate_age(self, birthdate):
        today = date.today()
        years = today.year - birthdate.year
        months = today.month - birthdate.month
        days = today.day - birthdate.day

        if days < 0:
            months -= 1
            prev_month = (today.month - 1) if today.month > 1 else 12
            prev_year = today.year if today.month > 1 else today.year - 1
            days += (date(prev_year, prev_month % 12 + 1, 1) - date(prev_year, prev_month, 1)).days

        if months < 0:
            years -= 1
            months += 12

        return years, months, days

# Menu-driven interface
def main():
    while True:
        print("\n--- Age Calculator ---")
        print("1. Calculate Age")
        print("2. Exit")

        choice = input("Enter your choice (1-2): ")

        if choice == '2':
            print("Exiting Age Calculator. Goodbye!")
            break

        try:
            dob_str = input("Enter your birthdate (YYYY-MM-DD): ")
            birthdate = datetime.strptime(dob_str, "%Y-%m-%d").date()

            calculator = SimpleAgeCalculator()
            years, months, days = calculator.calculate_age(birthdate)

            print(f"\nYour age is: {years} years, {months} months, and {days} days.")
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

if __name__ == "__main__":
    main()
