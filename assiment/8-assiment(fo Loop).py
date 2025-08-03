# 1. Write a Python program to print "Hello, World!" five times using a for loop.

for i in range(5):
    print("Hello, World!")

# 2. Write a Python program to print numbers from 1 to 10 using a while loop.

i = 1
while i <= 10:
    print(i)
    i += 1

# 3. Write a Python program to print the characters of a given word one by one using a for loop.

word = "Programming"
for char in word:
    print(char)

# 4. Write a Python program to print "Python is fun!" ten times using a while loop.

count = 0
while count < 10:
    print("Python is fun!")
    count += 1

# 5. Write a Python program to iterate over a given list and print each item using a for loop.

my_list = ["apple", "banana", "cherry", "date"]
for item in my_list:
    print(item)

# 6. Write a Python program to iterate over a given tuple and print each item using a while loop.

my_tuple = ("red", "green", "blue", "yellow")
index = 0
while index < len(my_tuple):
    print(my_tuple[index])
    index += 1

# 7. Write a Python program to print all elements of a given list using a for loop with range().

numbers = [10, 20, 30, 40, 50]
for i in range(len(numbers)):
    print(numbers[i])

# 8. Write a Python program to print all elements of a string using a for loop.

text = "HelloPython"
for ch in text:
    print(ch)

# 9. Write a Python program to print all keys of a given dictionary using a for loop.

my_dict = {"name": "Alice", "age": 25, "city": "New York"}
for key in my_dict:
    print(key)

# 10. Write a Python program to print all values of a given dictionary using a while loop.

values = list(my_dict.values())
i = 0
while i < len(values):
    print(values[i])
    i += 1

# 11. Write a Python program to iterate over a set and print each element using a for loop.

my_set = {"apple", "banana", "cherry"}
for item in my_set:
    print(item)

# 12. Write a Python program to iterate over a given list and print only the elements that have the letter "A".

fruits = ["Apple", "Banana", "Mango", "Orange", "Kiwi"]
for fruit in fruits:
    if "A" in fruit or "a" in fruit:
        print(fruit)

# 13. Write a Python program to iterate over a given tuple and stop when it finds the element "Stop".

things = ("Go", "Run", "Walk", "Stop", "Jump")
for item in things:
    if item == "Stop":
        break
    print(item)

# 14. Write a Python program to print all elements of a list in reverse order using a for loop.

nums = [1, 2, 3, 4, 5]
for i in range(len(nums)-1, -1, -1):
    print(nums[i])

# 15. Write a Python program to print every second character of a list using a for loop with range().

letters = ["a", "b", "c", "d", "e", "f", "g"]
for i in range(0, len(letters), 2):
    print(letters[i])
