# 1. Write a Python program to check if a number entered by the user is positive, negative, or zero. 
num=int(input("enter the number ")) 
if num ==0:
    print("The number is Zero")
elif num >0:
    print("the number is positive number ")
else:
    print("the number in negative ")

# 2. Create a program that takes an integer input and checks if it is even or odd. 
num=int(input("enter the number ")) 
if num % 2 ==0:
    print("the number is even ")
else:
    print("the number is odd ")


# 3. Write a Python script to determine if a person is eligible to vote (18 years or older).  
age=int(input("enter youe Age "))
if age >= 18 :
    print(f"According to your age you are able to vote ")
else:
    print("you are not able to vota")

# 4. Develop a program that takes three numbers as input and prints the largest among them.  
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
if num1 > num2 and num1 > num3:
    print(F"{num1}is gretaer than nmu2 and num3")
elif num2 > num3:
    print(F"{num2}is gretaer than nmu1 and num3")
else:
 print(F"{num3}is gretaer than nmu1 and num2")

# 5. Write a Python program that asks the user for a year and checks if it is a leap year.  
year=int(input("enter the year"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
    else:
        print(f"{year} is a leap year")
else:
 print(f"{year} is not a leap year")

# 6. Create a program that takes a character as input and determines whether it is a vowel or a consonant.  
char = input("Enter a character: ")
if char in 'aeiouAEIOU':
   print(F"The {char} is a vowel.")
else:
   print(F"The {char} is a consonant.")

# 7. Write a Python script that asks the user for a password and grants access only if the password matches "Python123".
password=(input("Enter the password:-"))
origanal_pass="Python123"
if password == origanal_pass:
    print("  access granted  ")  
else:
    print("access failed")

# 8. Develop a program to check if a given number is divisible by both 5 and 7. 
number=int(input("enter the number")) 
if number % 5 == 0 and number %7==0:
  print(f"{number} is divisible by 5 and 7")
else:
  print(f"{number} is not divisible by 5 and 7 ")  

# 9. Write a Python program that determines whether a triangle is equilateral, isosceles, or scalene based on user inputs for three sides.  
side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))
if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
    if side1 == side2 == side3:
        print("The triangle is Equilateral.")
    elif side1 == side2 or side1 == side3 or side2 == side3:
        print("The triangle is Isosceles.")
    else:
        print("The triangle is Scalene.")

else:
    print("The input values do not form a valid triangle.")

# 10. Create a program that takes a student's marks as input and prints the grade according to the following rules:  
#    - Above 90: A  
#    - 80 to 90: B  
#    - 70 to 79: C  
#    - 60 to 69: D  
#    - Below 60: F  
marks = float(input("Enter the student's marks (out of 100): "))
if marks > 90:
    grade = 'A'
elif marks >= 80:
    grade = 'B'
elif marks >= 70:
    grade = 'C'
elif marks >= 60:
    grade = 'D'
else:
    grade = 'F'


print("The grade is:", grade)





# 11. Write a program to display menu program and perform a task according to input.
   
#        *****************MENU*****************
#         1.ADD
#         2.SUB
#         3.MULTIPLY
#         4.DIVIDE
      
#           ENTER YOUR CHOICE=
#           ENTER FIRST NO=
#           ENTER SECOND NO=
#           RESULT=


print("*****************MENU*****************")
print("1. ADD")
print("2. SUB")
print("3. MULTIPLY")
print("4. DIVIDE")

choice = int(input("ENTER YOUR CHOICE: "))
num1 = float(input("ENTER FIRST NO: "))
num2 = float(input("ENTER SECOND NO: "))
if choice == 1:
    result = num1 + num2
    print("RESULT =", result)
elif choice == 2:
    result = num1 - num2
    print("RESULT =", result)
elif choice == 3:
    result = num1 * num2
    print("RESULT =", result)
elif choice == 4:
    if num2 != 0:
        result = num1 / num2
        print("RESULT =", result)
    else:
        print("ERROR: Division by zero is not allowed.")
else:
    print("INVALID CHOICE")


# 12.Write a program to Determine if a character is a vowel or consonant.

char = input("Enter a character: ")
if char in 'aeiouAEIOU':
   print(F"The {char} is a vowel.")
else:
   print(F"The {char} is a consonant.")
# 13.Treasure Hunt Decision
# You're on a treasure hunt, and you find three chests. Chest A says it has gold, Chest B says it has a map, and Chest C says, "Choose wisely."  
# Write a program that takes the chest you choose as input and:  
# - If you pick A, you get gold if the code says "lucky day," else a trap.  
# - If you pick B, you get a map if the chest color is "red"; otherwise, it's fake.  
# - If you pick C, it gives you a riddle to solve to proceed.


# Display choices
print("You are on a treasure hunt and find three chests:")
print("Chest A: 'I have gold'")
print("Chest B: 'I have a map'")
print("Chest C: 'Choose wisely'")

# Take user input
choice = input("Which chest do you choose? (A/B/C): ")

if choice == 'A' or choice == 'a':
    code = input("Enter the secret code: ")
    if code == "lucky day":
        print("Congratulations! You found gold! 💰")
    else:
        print("Oh no! It's a trap! 😱")

elif choice == 'B' or choice == 'b':
    color = input("Enter the color of the chest: ")
    if color == "red":
        print("You found the map! 🗺️ Proceed to the next clue.")
    else:
        print("It's a fake map! Better luck next time. ❌")

elif choice == 'C' or choice == 'c':
    print("You must solve this riddle to proceed:")
    print("Riddle: What has keys but can’t open locks?")
    answer = input("Your answer: ")
    if answer == "piano" or answer == "a piano":
        print("Correct! You may proceed. 🎉")
    else:
        print("Wrong answer! The path remains hidden. 🔒")

else:
    print("Invalid choice! Please select A, B, or C.")

# 14. Alien Invasion
# An alien spaceship lands, and you’re asked three questions by the alien leader.  
# - If your favorite color is "green," they’ll ask about your favorite animal.  
# - If it’s "blue," they’ll ask for a secret code.  
# - For any other color, they’ll challenge you to a duel.  
# Write a program to handle this interaction and decide your fate.

# Alien encounter begins
print("An alien spaceship lands! 👽 The alien leader approaches you.")

# Ask for favorite color
color = input("Alien: What is your favorite color? ")

if color == "green" or color == "Green":
    animal = input("Alien: What is your favorite animal? ")
    print("Alien: Hmm... interesting. We love " + animal + " too. You may live. 🛸")

elif color == "blue" or color == "Blue":
    code = input("Alien: Enter the secret code: ")
    if code == "42":
        print("Alien: You know the code! Welcome, friend of the stars! 🚀")
    else:
        print("Alien: Wrong code. Prepare to be zapped! ⚡")

else:
    print("Alien: Unknown color... You must face me in a duel! 🥊")
    weapon = input("Choose your weapon (laser/sword/shield): ")
    print("Alien: Interesting choice. Let the duel begin with your " + weapon + "! 💥")


# 15. Magic Potion Mix
# A wizard gives you three ingredients to mix into a potion: Dragon Scale, Phoenix Feather, and Mermaid Tears.  
# - If you mix Dragon Scale and Phoenix Feather, you can fly.  
# - If you mix Phoenix Feather and Mermaid Tears, you breathe underwater.  
# - If you mix Dragon Scale and Mermaid Tears, you become invisible.  
# Write a program that takes two ingredients as input and outputs the potion's effect.
# Display ingredients
print("The wizard gives you three ingredients:")
print("- Dragon Scale")
print("- Phoenix Feather")
print("- Mermaid Tears")

# Get user inputs
ingredient1 = input("Enter first ingredient: ")
ingredient2 = input("Enter second ingredient: ")

# Check combinations (order-independent)
if (ingredient1 == "Dragon Scale" and ingredient2 == "Phoenix Feather") or \
   (ingredient1 == "Phoenix Feather" and ingredient2 == "Dragon Scale"):
    print("You mixed the potion... You can now fly!")

elif (ingredient1 == "Phoenix Feather" and ingredient2 == "Mermaid Tears") or \
     (ingredient1 == "Mermaid Tears" and ingredient2 == "Phoenix Feather"):
    print("You mixed the potion... You can breathe underwater!")

elif (ingredient1 == "Dragon Scale" and ingredient2 == "Mermaid Tears") or \
     (ingredient1 == "Mermaid Tears" and ingredient2 == "Dragon Scale"):
    print("You mixed the potion... You become invisible! ")

else:
    print("Nothing happens... Are you sure these are magical ingredients? ")
