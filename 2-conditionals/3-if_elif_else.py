# if elif else 
# will check the number is positive negative or zero 

num = int(input("Enter a number: "))
if num == 0:
    print("Number is zero")
elif num > 0:
    print("Number is positive")
else:
    print("Number is negative")



num = int(input("Enter a marks : "))
if num > 80:
    print("the grede is A ")
elif num > 70:
    print("The Gread iss B")
elif num >60 :
    print("The Gread iss C")
else:
    print("The gread is d")


#find the grestest numner 
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 > num2:
    print(F"{num1}is gretaer than nmu2")
else:
  print(F"{num2}is gretaer than nmu1")
 #find the grestest in 3 number
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
if num1 > num2 and num1 > num3:
    print(F"{num1}is gretaer than nmu2 and num3")
elif num2 > num3:
    print(F"{num2}is gretaer than nmu1 and num3")
else:
 print(F"{num3}is gretaer than nmu1 and num2")

 #find the smallest in 3 number
 num1 = int(input("Enter the first number: "))
 num2 = int(input("Enter the second number: "))
 num3 = int(input("Enter the third number: "))
 if num1 < num2 and num1 < num3:
     print(F"{num1}is smallest than nmu2 and num3")
 elif num2 < num3:
     print(F"{num2}is smallest than nmu1 and num3")
 else:
  print(F"{num3}is smallest than nmu1 and num2")

# vowel or constant
char = input("Enter a character: ")
if char in 'aeiouAEIOU':
   print(F"The {char} is a vowel.")
else:
   print(F"The {char} is a consonant.")
 #using or 

char= input("enter the charter ")
if char=="a" or char=="e" or char=="i" or char=="o" or char=="u":
   print(F"The {char} is a vowel.")
else:
 print(F"The {char} is a consonant.")