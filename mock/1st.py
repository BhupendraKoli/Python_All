'''
Take a  list of tuples from user where each tuple contains the name of a student and their score in a test. Write a Python program that does the following:

From the list of tuples, extract:
All names into a list
All scores into a separate list
Using loops and operators, compute:
The average score
The highest and lowest scores
Print a star (*) pattern for each student based on their score:
For every 10 marks, print 1 star
Example: if a student scores 47, print 4 stars
Use exception handling to manage:
If a score is not an integer or float, raise and handle a custom exception InvalidScoreError


'''
# # Ask how many students
# n = int(input("Enter the number of students: "))

# # Create an empty list to store tuples
# students = []
# marks=[]

# # Loop to take (name, score) input
# for i in range(n):
#     name = input(f"Enter the name of student {i+1}: ")
#     score_input = input(f"Enter the score of {name}: ")
#     score=int(score_input)

#     # Store as a tuple in the list
#     students.append((name))
#     marks.append(( score))

# # Print the final list of tuples
# print("\nList of student tuples:")
# print(students)
# print(marks)


# # ---- Calculations using loops and operators ----

# # Calculate average
# total = 0
# for m in marks:
#     total += m
# average = total / len(marks)

# # Find highest and lowest
# highest = marks[0]
# lowest = marks[0]

# for m in marks:
#     if m > highest:
#         highest = m
#     if m < lowest:
#         lowest = m

# # ---- Output results ----
# print("\n--- Score Analysis ---")
# print("Average score:", average)
# print("Highest score:", highest)
# print("Lowest score:", lowest)

# # Star pattern output
# print("\n--- Star Patterns (1 star per 10 marks) ---")
# for i in range(n):
#     name = students[i]
#     score = marks[i]
#     stars = score // 10
#     print(f"{name} ({score}): {'*' * stars}")

################################################################################


# Initialize lists
students = []
marks = []

try:
    n = int(input("Enter the number of students: "))

    for i in range(n):
        name = input(f"\nEnter the name of student {i+1}: ")
        score_input = input(f"Enter the score of {name}: ")

        # Manually validate score input (allowing int/float)
        if score_input.replace('.', '', 1).isdigit():
            score = float(score_input) if '.' in score_input else int(score_input)
        else:
            raise Exception(f"Invalid score for {name}: '{score_input}' is not a number.")

        if score < 0:
            raise Exception(f"Score cannot be negative for {name}.")

        students.append(name)
        marks.append(score)

    # Calculate average, highest, and lowest using loop
    total = 0
    highest = marks[0]
    lowest = marks[0]

    for m in marks:
        total += m
        if m > highest:
            highest = m
        if m < lowest:
            lowest = m

    average = total / len(marks)

    # Output results
    print("\n--- Score Analysis ---")
    print("Students:", students)
    print("Marks:", marks)
    print("Average score:", average)
    print("Highest score:", highest)
    print("Lowest score:", lowest)

    # Print star pattern
    print("\n--- Star Patterns (1 star per 10 marks) ---")
    for i in range(n):
        name = students[i]
        score = marks[i]
        stars = int(score) // 10
        print(f"{name} ({score}): {'*' * stars}")

except ValueError:
    print("Invalid input! Please enter a valid number of students.")
except Exception as e:
    print("Error:", e)

