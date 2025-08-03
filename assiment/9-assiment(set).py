# 1. Write a Python program to create a set.

s = {1, 2, 3}
print(s)

# 2. Write a Python program to iterate over sets.

for item in s:
    print(item)

# 3. Write a Python program to add member(s) to a set.

s.add(4)
print(s)

# 4. Write a Python program to remove item(s) from a given set.

s.remove(2)
print(s)

# 5. Write a Python program to remove an item from a set if it is present in the set.

s.discard(3)
print(s)

# 6. Write a Python program to create an intersection of sets.

a = {1,2,3}
b = {2,3,4}
print(a.intersection(b))

# 7. Write a Python program to create a union of sets.

print(a.union(b))

# 8. Write a Python program to create set difference.

print(a.difference(b))

# 9. Write a Python program to create a symmetric difference.

print(a.symmetric_difference(b))

# 10. Write a Python program to check if a set is a subset of another set.

print(a.issubset(b))

# 11. Write a Python program to create a shallow copy of sets.
# Note : Shallow copy is a bit-wise copy of an object. A new object is created that has an exact copy of the values in the original object.

copy_a = a.copy()
print(copy_a)

# 12. Write a Python program to remove all elements from a given set.

a.clear()
print(a)

# 13. Write a Python program that uses frozensets.
# Note: Frozensets behave just like sets except they are immutable.

fs = frozenset([1, 2, 3])
print(fs)

# 14. Write a Python program to find the maximum and minimum values in a set.

num_set = {5, 10, 3, 9}
print(max(num_set))
print(min(num_set))

# 15. Write a Python program to find the length of a set.

print(len(num_set))

# 16. Write a Python program to check if a given value is present in a set or not.

print(5 in num_set)

# 17. Write a Python program to check if two given sets have no elements in common.

set1 = {1,2,3}
set2 = {4,5,6}
print(set1.isdisjoint(set2))

# 18. Write a Python program to check if a given set is a superset of itself and a superset of another given set.

print(set1.issuperset(set1))
print(set2.issuperset({4}))

# 19. Write a Python program to find elements in a given set that are not in another set.

print(set1.difference(set2))

# 20. Write a Python program to remove the intersection of a second set with a first set.

set1 -= set1.intersection(set2)
print(set1)

# 21. Write a Python program to find all the unique words and count the frequency of occurrence from a given list of strings. Use Python set data type.

words = ["apple", "banana", "apple", "orange", "banana"]
unique = set(words)
for word in unique:
    print(f"{word}: {words.count(word)}")

# 22. Write a Python program that finds all pairs of elements in a list whose sum is equal to a given value.

lst = [1,2,3,4,5]
target = 5
for x in lst:
    for y in lst:
        if x != y and x+y == target:
            print(x,y)

# 23. Write a Python program to find the longest common prefix of all strings. Use the Python set.

strs = ["interview", "internet", "internal", "into"]
prefix = ""
for i in zip(*strs):
    if len(set(i)) == 1:
        prefix += i[0]
    else:
        break
print(prefix)

# 24. Write a Python program to find the two numbers whose product is maximum among all the pairs in a given list of numbers. Use the Python set.

nums = {1, 10, 2, 6, 5, 3}
nums_list = list(nums)
max_product = 0
pair = ()
for i in range(len(nums_list)):
    for j in range(i+1, len(nums_list)):
        product = nums_list[i] * nums_list[j]
        if product > max_product:
            max_product = product
            pair = (nums_list[i], nums_list[j])
print(pair, max_product)

# 25. Given two sets of numbers, write a Python program to find the missing numbers in the second set as compared to the first and vice versa. Use the Python set.

s1 = {1,2,3,4}
s2 = {3,4,5,6}
print("In s1 not s2:", s1 - s2)
print("In s2 not s1:", s2 - s1)

# 26. Write a Python program to find all the anagrams and group them together from a given list of strings. Use the Python data type.

words = ["bat","tab","cat","tac","dog"]
groups = {}
for word in words:
    key = "".join(sorted(word))
    groups.setdefault(key, []).append(word)
print(list(groups.values()))

# 27. Write a Python program to find all the anagrams in a given list of strings and then group them together. Use the Python data type.

# (same as above, different phrasing)
print(list(groups.values()))

# 28. Write a Python program to find all the unique combinations of 3 numbers from a given list of numbers, adding up to a target number.

nums = [1,2,3,4,5,6]
target = 10
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        for k in range(j+1,len(nums)):
            if nums[i]+nums[j]+nums[k]==target:
                print(nums[i],nums[j],nums[k])

# 29. Write a Python program to find the third largest number from a given list of numbers.Use the Python set data type.

nums = [1,2,3,4,5,6]
third = sorted(set(nums))[-3]
print(third)

# 30. Write a Python program to remove all duplicates from a given list of strings and return a list of unique strings. Use the Python set data type.

strings = ["apple","banana","apple","cherry"]
unique = list(set(strings))
print(unique)
