'''
Section A: Theory (10 Questions)

1.What are the key differences between lists and arrays in Python? Discuss their uses and limitations.
Lists
Can store elements of different data types (e.g., [1, "apple", 3.5])
Dynamic in size (can grow/shrink)
Built-in Python data type
More flexible but slower for numerical computation

Arrays (from array module or numpy arrays)
Usually store elements of the same data type (e.g., all integers)
More memory-efficient and faster for large numerical data
Need to import array or numpy to use them
Support element-wise operations in numpy

Uses:
Lists: general-purpose container
Arrays: scientific/numerical computing

Limitations:
Lists: slower for number crunching
Arrays: limited to one data type


2.Explain the concept of a set in Python. How does it differ from a list? Provide examples to illustrate your answer.
A set in Python is an unordered collection of unique elements. Sets are similar to the mathematical concept of a set:
No duplicate items are allowed
The elements are unordered (so they do not have an index)
Sets are mutable (you can add or remove items), but the elements themselves must be immutable (like numbers, strings, or tuples)
Python implements sets using hash tables, which makes membership testing (e.g., if x in my_set) very fast.


3.Describe how a dictionary works in Python. What are the primary operations you can perform on dictionaries?

A dictionary in Python is a collection of key-value pairs. Each key maps to a value, like an address book mapping names to phone numbers.
Key features:
Unordered (but insertion-ordered since Python 3.7)
Keys must be unique and immutable (e.g., strings, numbers, tuples)
Values can be any data type and can be duplicated
Internally uses a hash table for fast lookup, insertion, and deletion

4.How do you perform slicing on a list in Python? Provide examples demonstrating various slicing techniques.
Slicing is a technique to extract a portion of a list by specifying a range of indices.
list[start : end : step]
start — the index to begin (inclusive)
end — the index to stop (exclusive)
step — how many elements to skip
If you omit any of these, Python uses sensible defaults:
start defaults to 0
end defaults to the length of the list
step defaults to 1


5.What are the advantages of using sets over lists in Python? In what scenarios would you prefer using a set?
1. No duplicates allowed
Sets automatically remove duplicates.
Lists allow duplicates, so you have to remove them manually if needed.
2. Faster membership testing
Sets use a hash table under the hood.
Checking x in set is O(1) on average, while x in list is O(n).
3. Built-in set operations
Sets provide convenient operations like union, intersection, and difference, which are not directly supported by lists.
4. Cleaner code for unique collections
Sets make the code simpler when you only care about unique elements, avoiding extra filtering.
5. Mathematical set operations
Sets directly support powerful operations for comparing and combining data in a way lists cannot.


6.Explain the difference between dict.items(), dict.keys(), and dict.values() in Python. Provide examples for each.
 dict.keys()
Returns a view object of all the keys in the dictionary.
You can loop over it or convert it to a list.

dict.values()
Returns a view object of all the values in the dictionary.
Useful when you only care about the stored data, not the keys.

dict.items()
Returns a view of key-value pairs as tuples.
Handy for iterating through both the keys and the values at once.


7.How can you iterate over a list in Python? Discuss different methods and their use cases.

Using list comprehensions
Using a while loop
Using enumerate()
Using index with range()
Using a simple for loop

8.How can you perform set operations like union, intersection, and difference in Python? Provide code snippets for each operation.

1. Union
Combines elements from both sets
Removes duplicates

2. Intersection
Keeps only elements present in both sets

3. Difference
Elements in the first set but not in the second

4. Symmetric difference
Elements in either set, but not in both

9.Explain the Function and its types.

1 No argument, no return type
Function takes no input arguments and does not return anything.
It just performs an action.

def greet():
    print("Hello, welcome!")

greet()  # prints Hello, welcome!
Use case: When you only need to display something or perform an action, without needing input or output.

2 No argument, with return type
Function takes no arguments but returns a value.

def get_pi():
    return 3.14159

value = get_pi()
print(value)  # 3.14159
Use case: When you want to return a fixed value from a function.

3 With argument, no return type
Function takes arguments but does not return anything; just performs a task using the arguments.

def print_square(num):
    print("Square is", num * num)

print_square(5)  # prints Square is 25
 Use case: When you need to process user data and display results but don’t need to return a value.

4 With argument, with return type
Function takes arguments and returns a value.
def add(a, b):
    return a + b

result = add(3, 4)
print(result)  # 7
Use case: When you need both input and output from a function.



10.Compare and contrast lists, sets, and dictionaries in Python. Discuss their unique features, performance implications, and appropriate use cases.

1 Lists
Features
Ordered (elements have a defined sequence)
Allow duplicate elements
Mutable (can change elements, append, delete)
Supports indexing and slicing

Performance
Searching elements: O(n) linear time
Adding/removing at the end: O(1) (amortized)
Inserting/removing in the middle: O(n)

Use cases
Maintaining an ordered collection
When duplicate items are neede
When position/index of items matters
fruits = ["apple", "banana", "cherry", "apple"]

2 Sets
Features
Unordered
No duplicate elements
Mutable
No indexing/slicing
Uses a hash table internally

Performance
Membership tests: O(1) average time
Adding/removing: O(1) average
No support for accessing elements by index

Use cases
When you need to store unique elements
Fast membership testing
Performing set operations (union, intersection, difference)
unique_colors = {"red", "green", "blue"}

3 Dictionaries

Features
Unordered (but insertion-ordered since Python 3.7)
Store key–value pairs
Keys must be unique and immutable
Values can be any data type
Mutable

Performance
Lookup by key: O(1) average time
Insertion/deletion: O(1) average
Fast, thanks to hash table implementation

Use cases
When you want to associate data (mapping a key to a value)
When fast key-based lookup is needed
Storing structured data
Example:
student = {"name": "Alice", "age": 20}
'''

# Section B: Correct the Code (10 Questions)


# 1. my_set = {1, 2, 3}
#    my_set.add[4]

# 2. my_set = {1, 2, 3}
#    my_set.remove(5)

# 3. a = {1, 2}
#    b = {3, 4}
#    result = a.union[b]

# 4. text = "hello"
#    letters = set(text)
#    print(letters[0])

# 5. nums = [1, 2, 2, 3]
#    squares = {x*x for x in nums if x => 2}

# 6. s = "python"
#    rev = s.reverse()

# 7. msg = "hello world"
#    msg.replace("world", "Python")
#    print(msg) 

# 8. word = "elephant"
#    if word.startwith("el"): 
#    print("Yes")

# 9. student = {"name": "Alice", "age": 20}
#    print(student["grade"])

# 10. data = {"a": 1, "b": 2}
# data.update["c"] = 3

# Question 1
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)

# Question 2
my_set = {1, 2, 3}
my_set.discard(5)  # safe if element not found
print(my_set)

# Question 3
a = {1, 2}
b = {3, 4}
result = a.union(b)
print(result)

# Question 4
text = "hello"
letters = list(set(text))
print(letters[0])  # index after converting to list

# Question 5
nums = [1, 2, 2, 3]
squares = {x * x for x in nums if x >= 2}
print(squares)

# Question 6
s = "python"
rev = s[::-1]
print(rev)

# Question 7
msg = "hello world"
msg = msg.replace("world", "Python")
print(msg)

# Question 8
word = "elephant"
if word.startswith("el"):
    print("Yes")

# Question 9
student = {"name": "Alice", "age": 20}
print(student.get("grade", "N/A"))  # safe fallback

# Question 10
data = {"a": 1, "b": 2}
data.update({"c": 3})
print(data)


# Section C

# 1. Write a Python program that takes a list of integers and returns all possible sublists of the original list.
def all_sublists(lst):
    sublists = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            sublists.append(lst[i:j])
    return sublists

lst = [1, 2, 3]
print(" All sublists of", lst, "are", all_sublists(lst))


# 2. Print all prime numbers between 1 and 20 using nested for loop.
print(" Prime numbers from 1 to 20:")
for num in range(2, 21):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
print()


# 3. Given a list of words, group them into a dictionary by first letter.
words = ['apple', 'banana', 'avocado']
grouped = {}
for word in words:
    first = word[0]
    grouped.setdefault(first, []).append(word)
print(" Grouped words by first letter:", grouped)


# 4. Write a Python program that sorts a list of tuples based on the sum of elements in each tuple without using the sorted() function.
tuples = [(1, 2), (3, 4), (0, 0)]
for i in range(len(tuples)):
    min_idx = i
    for j in range(i + 1, len(tuples)):
        if sum(tuples[j]) < sum(tuples[min_idx]):
            min_idx = j
    tuples[i], tuples[min_idx] = tuples[min_idx], tuples[i]
print(" Sorted tuples by sum:", tuples)


# 5. Given a sentence, count the frequency of each word.
sentence = "this is a test this is"
words = sentence.split()
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1
print(" Word frequency:", freq)


# 6. Count vowels and consonants from a string.
text = "hello world"
vowels = "aeiou"
v_count = 0
c_count = 0
for ch in text.lower():
    if ch.isalpha():
        if ch in vowels:
            v_count += 1
        else:
            c_count += 1
print(" vowels =", v_count, "consonants =", c_count)


# 7. Write a Python program that finds all combinations of a list of numbers that sum up to a given target.
#    The numbers in the list can be used multiple times.
def combination_sum(nums, target, current=[], results=[]):
    if sum(current) == target:
        results.append(current[:])
        return
    if sum(current) > target:
        return
    for num in nums:
        current.append(num)
        combination_sum(nums, target, current, results)
        current.pop()
    return results

nums = [2, 3, 5]
target = 8
print(" Combinations summing to", target, "are", combination_sum(nums, target))


# 8. Remove all key-value pairs where the value is less than 10.
d = {"a": 5, "b": 12, "c": 8, "d": 15}
filtered = {k: v for k, v in d.items() if v >= 10}
print(" After removing values < 10:", filtered)


# 9. Remove all duplicate characters from a string.
s = "programming"
result = ""
for ch in s:
    if ch not in result:
        result += ch
print(" String after removing duplicates:", result)


# 10. Write a Python program that reads a list of integers and performs the following:
#     Counts the frequency of each integer using a dictionary.
#     Finds the top 1 most frequent integers.
nums = [1, 2, 2, 3, 3, 3, 4]
count = {}
for n in nums:
    count[n] = count.get(n, 0) + 1
top = max(count, key=count.get)
print(" Frequency dictionary:", count)
print(" Top 1 most frequent integer:", top)
