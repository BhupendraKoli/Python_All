# 1. Write a Python program to sum all the items in a list. 
l=[1,2,3,4,5]
a=0
print(sum(l))
for i in l :
    a+=i
print(a)
# 2. Write a Python program to multiply all the items in a list. 
l=[1,2,3,4,5]
mul=1
for i in l :
    mul*=i
print(mul)


# 3. Write a Python program to get the largest number from a list. 
numbers = [4, 7, 2, 9, 5]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num

print("The largest number is:", largest)


# 4. Write a Python program to get the smallest number from a list. 
l=[20,50,60,30,10]
small=l[0]
for i in l:
    if i < small:
        small = i 
print("the small number is ",small)        

# 5. Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same. 
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2
sample_list = ['abc', 'xyz', 'aba', '1221']
count = 0

for word in sample_list:
    if len(word) >= 2 and word[0] == word[-1]:
        count += 1

print("Expected Result:", count)


# 6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples. 
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

# use key in sorted()
sorted_list = sorted(sample_list, key=lambda x: x[-1])

print("Expected Result:", sorted_list)


# 7. Write a Python program to remove duplicates from a list. 
sample_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = list(set(sample_list))
print("Unique list:", unique_list)


unique_list = []
for item in sample_list:
    if item not in unique_list:
        unique_list.append(item)
print("Unique list with order preserved:", unique_list)


# 8. Write a Python program to check if a list is empty or not. 
my_list = []

if not my_list:
    print("List is empty")
else:
    print("List is not empty")



# 9. Write a Python program to clone or copy a list. 
original_list = [1, 2, 3, 4]
cloned_list = original_list.copy()
print("Cloned list:", cloned_list)


# 10. Write a Python program to find the list of words that are longer than n from a given list of words. 
words = ['hello', 'hi', 'world', 'python']
n = 3

long_words = [word for word in words if len(word) > n]
print("Words longer than", n, ":", long_words)


# 11. Write a Python function that takes two lists and returns True if they have at least one common member. 
l1=[1,2,3,4]
l2=[0,5,6,7]
for item in l1:
        if item in l2:
            print(True) 
  
 

# 12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. 
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']
sample_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
first_part = sample_list[1:4]
result = first_part  

print("Updated list:", result)


# 13. Write a Python program to generate a 3*4*6 3D array whose each element is *. 
array = [[['*' for _ in range(6)] for _ in range(4)] for _ in range(3)]
print(array)


# 14. Write a Python program to print the numbers of a specified list after removing even numbers from it. 
sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = [x for x in sample_list if x % 2 != 0]
print("After removing even numbers:", result)


# 15. Write a Python program to shuffle and print a specified list. 
# deterministic reorder instead of shuffle
my_list = [1, 2, 3, 4, 5]

# for example, reversing elements
my_list = my_list[::-1]
print("Reordered list:", my_list)


# 16. Write a Python program to generate and print a list of the first and last 5 elements where the values are square numbers between 1 and 30 (both included). 
squares = [i**2 for i in range(1, 31)]
result = squares[:5] + squares[-5:]
print("First and last 5 squares:", result)


# 17. Write a Python program to generate and print a list except for the first 5 elements, where the values are square numbers between 1 and 30 (both included). 
squares = [i**2 for i in range(1, 31)]
result = squares[5:]
print("Squares except first 5:", result)

# 18. Write a Python program to generate all permutations of a list in Python. 

lst = [1, 2, 3]
n = len(lst)

for i in range(n):
    for j in range(n):
        for k in range(n):
            # check for unique indices
            if i != j and j != k and i != k:
                print([lst[i], lst[j], lst[k]])



# 19. Write a Python program to calculate the difference between the two lists. 
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

# elements in list1 but not in list2
diff = list(set(list1) - set(list2))
print("Difference (list1 - list2):", diff)


# 20. Write a Python program to access the index of a list. 
my_list = ['a', 'b', 'c', 'd']

for index, value in enumerate(my_list):
    print(f"Index {index}: {value}")



# 21. Write a Python program to convert a list of characters into a string. 
char_list = ['H', 'e', 'l', 'l', 'o']
result = ''.join(char_list)
print("String:", result)


# 22. Write a Python program to find the index of an item in a specified list. 
my_list = ['apple', 'banana', 'cherry']
index = my_list.index('banana')
print("Index of 'banana':", index)


# 23. Write a Python program to flatten a shallow list. 
shallow_list = [[1, 2], [3, 4], [5, 6]]
flat_list = [item for sublist in shallow_list for item in sublist]
print("Flattened list:", flat_list)


# 24. Write a Python program to append a list to the second list. 
list1 = [1, 2, 3]
list2 = [4, 5, 6]

list2.extend(list1)  # list1 is appended to list2
print("Combined list:", list2)


# 25. Write a Python program to select an item randomly from a list. 


# 26. Write a Python program to check whether two lists are circularly identical. 


# 27. Write a Python program to find the second smallest number in a list. 
my_list = [5, 1, 8, 3, 2]
unique_list = list(set(my_list))  # remove duplicates
unique_list.sort()
print("Second smallest:", unique_list[1])


# 28. Write a Python program to find the second largest number in a list. 
my_list = [5, 1, 8, 3, 2]
unique_list = list(set(my_list))  # remove duplicates
unique_list.sort()
print("Second largest:", unique_list[-2])


# 29. Write a Python program to get unique values from a list. 
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_values = list(set(my_list))
print("Unique values:", unique_values)


# 30. Write a Python program to get the frequency of elements in a list. 
my_list = [1, 2, 2, 3, 3, 3, 4]

freq = {}

for item in my_list:
    found = False
    for key in freq:
        if key == item:
            freq[key] += 1
            found = True
            break
    if not found:
        freq[item] = 1

print(freq)


# 31. Write a Python program to count the number of elements in a list within a specified range. 

my_list = [10, 20, 30, 40, 50, 60]
count = 0

low = 15
high = 45

for item in my_list:
    if item >= low and item <= high:
        count += 1

print("Count in range:", count)

# 32. Write a Python program to check whether a list contains a sublist. 
main_list = [1, 2, 3, 4, 5]
sub_list = [3, 4]

found = False
for i in range(len(main_list) - len(sub_list) + 1):
    match = True
    for j in range(len(sub_list)):
        if main_list[i + j] != sub_list[j]:
            match = False
            break
    if match:
        found = True
        break

if found:
    print("Sublist found")
else:
    print("Sublist not found")


# 33. Write a Python program to generate all sublists of a list. 
# Assignment(python list).txt
# Displaying Assignment(python list).txt.
# Assignment (list)
# Mithila Puranik
# •
# 26 Jun
# 100 points
# Due Today

# Assignment(python list).txt
# Text
# Class comments
lst = [1, 2, 3]
n = len(lst)

for i in range(n):
    for j in range(i+1, n+1):
        sublist = []
        for k in range(i, j):
            sublist.append(lst[k])
        print(sublist)
