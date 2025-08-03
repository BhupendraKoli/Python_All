# 1. Convert two list into one dictionary. (using zip function and without zip function)

l=[1,2,3,4]
l1=['a','b','c','d']
# Using zip function
d=dict(zip(l,l1))
print(d)
# Output: {1: 'a', 2: 'b', 3: 'c
# 4: 'd'}
# Without using zip function
d={}
for i in range(len(l)):
    d[l[i]]=l1[i]
print(d)


# 2. Write a Python script to sort (ascending and descending) a dictionary by value.
dics={"a":45,"b":89,"c":55,"d":44}
# Sorting dictionary by value in ascending order with out lamda function 

dics = {"a": 45, "b": 89, "c": 55, "d": 44}

# Convert to list of (key, value) pairs
items = list(dics.items())

# Sort ascending using simple loop (like bubble sort)
for i in range(len(items)):
    for j in range(i + 1, len(items)):
        if items[i][1] > items[j][1]:  # compare values
            items[i], items[j] = items[j], items[i]

# Create a new dictionary from sorted items
asc_dict = {}
for k, v in items:
    asc_dict[k] = v

print("Ascending:", asc_dict)

# For descending, reverse the sorted list
desc_dict = {}
for k, v in items[::-1]:
    desc_dict[k] = v

print("Descending:", desc_dict)


# 3. Write a Python program to combine two dictionary by adding values for common keys.
d1={"a":10,"b":20,"c":30}
d2={"a":15,"r":25,"u":35}
res=d1.copy()
for key,val in d2.items():
    if key in res:
        res[key]=res[key]+val
    else:
        res[key]=val
print(res)


# 4. Write a Python function to count the frequency of each word in a given text document 
#    and return a dictionary with word frequencies.

text="hello form user hello  "
words=text.split()
word_freq={}
for word in words:
    if word in word_freq:
        word_freq[word]+=1
    else:
        word_freq[word]=1
print(word_freq)


# 5. Given two dictionaries, write a function to find and return a new dictionary containing 
#    only the common keys and their corresponding values.
d1={1:"jay",2:"komal",3:"kiyara"}
d2={1:"ram",5:"aadity",6:"rahul"}
d={}
for key in d1:
    if key in d2:
        d[key] = (d1[key], d2[key]) 
print(d)

    
# 6. Develop a function that finds the element with the maximum frequency in a list 
#     and returns the element along with its frequency.
list1=[1,2,3,1,4,5,5,6,1,1,8,8,8,8,8,8]
max_freq_element = max(set(list1), key = list1.count)
print(max_freq_element, list1.count(max_freq_element))

list1 = [1, 2, 3, 1, 4, 5, 5, 6, 1, 1, 8, 8, 8, 8, 8, 8]

max_element = None
max_count = 0

for item in list1:
    count = list1.count(item)  # how many times item appears
    if count > max_count:
        max_count = count
        max_element = item

print("Element with max frequency:", max_element)
print("Frequency:", max_count)


    
# 7. Write a Python script to concatenate the following dictionaries to create a new one.
#     d1={1:20,2:30,3:70}
#     d2={4:89,5:90,6:87}
#     d3={7:90,8:34,9:63}
d1 = {1: 20, 2: 30, 3: 70}
d2 = {4: 89, 5: 90, 6: 87}
d3 = {7: 90, 8: 34, 9: 63}
new_dict = {}

new_dict.update(d1)
new_dict.update(d2)
new_dict.update(d3)

print(new_dict)

# 8. WAP and Find the Key with Maximum Value
d = {1: 20, 2: 45, 3: 30, 4: 90, 0: 95}
max_key = 0
max_value = 0
for i in d:
    if d[i] > max_value:
        max_value = d[i]
        max_key = i

print("Key with maximum value:", max_key ,"Maximum value:", max_value)

# 9. Write a function to invert a dictionary, swapping keys and values.(with duplicates value)
d = {"a": 1, "b": 2, "c": 1, "d": 3, "e": 2}

# Invert the dictionary
inverted = {}

for key, value in d.items():
    if value in inverted:
        inverted[value].append(key)
    else:
        inverted[value] = [key]

print("Inverted Dictionary:", inverted)

# 10. Find the common keys between two dictionaries and return a dictionary with common keys 
#     and their values from the first dictionary.

d1 = {"a": 10, "b": 20, "c": 30}
d2 = {"b": 99, "c": 88, "d": 77}

common = {}

for key in d1:
    if key in d2:
        common[key] = d1[key]

print("Common keys and values from d1:", common)

