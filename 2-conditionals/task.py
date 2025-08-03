#1.Print WOOW if score given by user is between 75 to 100 else BOO

score = int(input("Enter the score: "))

if 75 < score < 100:
    print("WOOW")
else:
    print("BOO")

# 2. Print Perfect if no 1 ;Good if no is between 0.9 to 0.6 ;Fine if 0.5;Poor if less than 0.5 and greater than 0 

number = float(input("Enter the number between 0 and 1: "))

if number == 1:
    print("Perfect")
elif 0.6 <= number < 1:
    print("Good")
elif number == 0.5:
    print("Fine")
elif 0 < number < 0.5:
    print("Poor")
else:
    print("Invalid input")

#3. Find the elder of two brothers Tim and Jim whose ages are given by user.

tim_age = int(input("Enter Tim's age: "))
jim_age = int(input("Enter Jim's age: "))

if tim_age > jim_age:
    print("Tim is elder")
elif jim_age > tim_age:
    print("Jim is elder")
else:
    print("Both are of the same age")

#4.Find the youngest of two sisters Ana and Mary whose ages are given by user.

ana_age = int(input("Enter Ana's age: "))
mary_age = int(input("Enter Mary's age: "))

if ana_age < mary_age:
    print("Ana is the youngest")
elif mary_age < ana_age:
    print("Mary is the youngest")
else:
    print("Both are of the same age")

#5. Print the Grade of student for given percentage (A(75-100),
  #  B(60-75),C(50-60),D(40-50),F(s<40))

percentage = float(input("Enter the percentage: "))

if 75 <= percentage <= 100:
    print("Grade A")
elif 60 <= percentage < 75:
    print("Grade B")
elif 50 <= percentage < 60:
    print("Grade C")
elif 40 <= percentage < 50:
    print("Grade D")
elif percentage < 40:
    print("Grade F")
else:
    print("Invalid input")

# using and operter

percentage = float(input("Enter the percentage: "))

if percentage >= 75 and percentage <= 100:
    print("Grade A")
elif percentage >= 60 and percentage < 75:
    print("Grade B")
elif percentage >= 50 and percentage < 60:
    print("Grade C")
elif percentage >= 40 and percentage < 50:
    print("Grade D")
elif percentage >= 0 and percentage < 40:
    print("Grade F")
else:
    print("Invalid input")
