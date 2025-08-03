# 
# Q1. Write a program to take two integer inputs from the user and find their difference and quotient.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Difference:", a - b)
if b != 0:
    print("Quotient:", a // b)
else:
    print("Cannot divide by zero")

# Q2. Take three integer inputs from the user. First, find the sum of all three numbers, then calculate the product of the first and third number. Print both the sum and the product.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
print("Sum:", a + b + c)
print("Product of first and third:", a * c)

# Q3. Write a program to input the base and height of a triangle and calculate its area.
base = float(input("Enter base of triangle: "))
height = float(input("Enter height of triangle: "))
area = 0.5 * base * height
print("Area of triangle:", area)

# Q4. Take two integer inputs from the user. Calculate the square of their sum and the cube of their difference. Print both results.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
sum_square = (a + b) ** 2
diff_cube = (a - b) ** 3
print("Square of sum:", sum_square)
print("Cube of difference:", diff_cube)

# Q5. Write a program to input the radius of a circle and find its circumference.
radius = float(input("Enter radius: "))
circumference = 2 * 3.1416 * radius
print("Circumference of circle:", circumference)

# Q6. Take three integer inputs from the user. Calculate the average of all three, then find the difference between the first and second number. Print the average and the difference.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
average = (a + b + c) / 3
diff = a - b
print("Average:", average)
print("Difference between first and second:", diff)

# Q7. Write a program to input two floating-point numbers and find their sum and division.
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("Sum:", a + b)
if b != 0:
    print("Division:", a / b)
else:
    print("Cannot divide by zero")

# Q8. Take three integer inputs from the user. Multiply the first two, then add the third number to the product. Print the final result.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
result = (a * b) + c
print("Final result:", result)

# Q9. Write a program to input the principal amount, rate of interest, and time period in years, then calculate the compound interest.
p = float(input("Enter principal: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time in years: "))
ci = p * ((1 + r/100) ** t - 1)
print("Compound Interest:", ci)

# Q10. Take four integer inputs from the user. Calculate the product of the first two and the sum of the last two. Then find the difference between the sum and the product.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))
product = a * b
sum_last = c + d
difference = sum_last - product
print("Difference:", difference)

# Q11. Write a program to input the side of a square and calculate its area and perimeter.
side = float(input("Enter side of square: "))
area = side * side
perimeter = 4 * side
print("Area:", area)
print("Perimeter:", perimeter)

# Q12. Take three integer inputs from the user. Calculate the sum of the first two and the product of the second and third. Print both results.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
sum_ab = a + b
product_bc = b * c
print("Sum of first two:", sum_ab)
print("Product of second and third:", product_bc)

# Q13. Write a program to input the length, width, and height of a cuboid, then calculate its volume.
l = float(input("Enter length: "))
w = float(input("Enter width: "))
h = float(input("Enter height: "))
volume = l * w * h
print("Volume of cuboid:", volume)

# Q14. Take two integer inputs from the user. Calculate the square of the first number and the cube of the second number. Print both results.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Square of first:", a ** 2)
print("Cube of second:", b ** 3)

# Q15. Write a program to input the base and height of a parallelogram and calculate its area.
base = float(input("Enter base: "))
height = float(input("Enter height: "))
area = base * height
print("Area of parallelogram:", area)

# Q16. Take four integer inputs from the user. Add the first and second, and subtract the third from the result. Then multiply by the fourth number. Print the final result.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))
result = ((a + b) - c) * d
print("Final result:", result)

# Q17. Write a program to input the diameter of a circle and find its area.
diameter = float(input("Enter diameter: "))
radius = diameter / 2
area = 3.1416 * radius * radius
print("Area of circle:", area)

# Q18. Take two floating-point numbers as input. Find the sum and average of the two numbers.
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("Sum:", a + b)
print("Average:", (a + b) / 2)

# Q19. Write a program to input the side of a cube and calculate its surface area.
side = float(input("Enter side of cube: "))
surface_area = 6 * side * side
print("Surface area of cube:", surface_area)

# Q20. Take five integer inputs from the user. Find the sum of all five and calculate the average. Print both results.
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = int(input("Enter number 3: "))
d = int(input("Enter number 4: "))
e = int(input("Enter number 5: "))
sum_all = a + b + c + d + e
average = sum_all / 5
print("Sum:", sum_all)
print("Average:", average)

# Q21. Write a program to input the distance in kilometers and convert it to miles.
km = float(input("Enter distance in kilometers: "))
miles = km * 0.621371
print("Distance in miles:", miles)

# Q22. Take three integer inputs from the user. Calculate the difference between the first and second, then add the third number.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
result = (a - b) + c
print("Final result:", result)

# Q23. Write a program to input two integers and swap their values using a temporary variable.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
temp = a
a = b
b = temp
print("After swapping:")
print("First number:", a)
print("Second number:", b)

# Q24. Take three integer inputs. Multiply all three numbers and print the result.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
print("Product:", a * b * c)

# Q25. Write a program to input a number of days and convert it into weeks and days.
days = int(input("Enter number of days: "))
weeks = days // 7
remaining_days = days % 7
print("Number of weeks:", weeks)
print("Number of remaining days:", remaining_days)
