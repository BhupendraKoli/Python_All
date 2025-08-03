# 
# l1=[1,2,3,42,5]
# sum=0
# for i in l1:
#     if i % 2 == 0:
#          print(i)
#          sum+=i
# print(sum )       


# Write a Python program that:

# Takes input from the user in the form of multiple student records, where each record includes:
# Student name (string)
# A list of 3 integer marks
# Remove any student who has scored less than 35 in any subject.
# For remaining students:
# Calculate average marks
# Assign a grade:

# A: average ≥ 85
# B: average ≥ 70
# C: average ≥ 50
# D: average < 50

# Store the result in a dictionary in this format:
# { "Name": ("Grade", AverageMarks) }
# (Use dictionary comprehension)
# Create a function to print a star pattern based on the grade:

# A → *****
# B → ****
# C → ***
# D → **

# You must use:

# List
# Tuple
# Loop
# Function
# Dictionary
# Comprehension
# Pattern printing

# No built-in libraries like pandas. Input should be taken at runtime.
# ovs-dbtx-ccm

def get_student_data():
    global students
    students=[]
    n=int(input("enter number of students : "))
    for i in range (n):
        name =input("enter name of student : ")
        marks=list(map(int,input("enter marks : ").split()))
        students.append((name,marks))

def less(marks):
    remove=[]
    if marks < 35:
        marks.remove()

def avg_marks():
    filtered=[]
    for student in students:
        marks=student
        avg=sum(marks)/len(marks)
        return avg

def grade(avg):
    if avg >=85:
        return 'A'
    elif avg >=70:
        return 'B'
    elif avg >=50:
        return 'C'
    else :
        return 'D'

def pattern(grade):
    if grade =='A':
        print("*")
    elif grade=='B':
        print("")
    elif grade=='C':
        print("*")
    else :
        print("")

get_student_data()
res_dict=students
for name , grade, avg in students():
    grade=grade(avg)
    res_dict = (f"{name} : {grade},{avg}")