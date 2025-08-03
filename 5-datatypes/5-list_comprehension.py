# list comprehension 
'''
what is list comprehension 
list comprehension is a way to create a new list from an existing list or other iterable by applying an
expression to each element.
it is a compact way to create lists.
it is a one-liner way to create lists.
it is a way to create lists without using for loops.

listcomprehension  is a concise way to create a new list by 
perforing an operation on each item an existing list 

faster than the loop 
'''
# example of list comprehension
# i will genert a number and print there square 
# res=[]
# for i in range(1,6):
#     res.append(i*i)
# print(res)  # [1, 4, 9, 16, 25]

# # using list comprehension 
# # syntax [expression for item in iterable if condition]
# list1=[1,2,3,4,5]
# res=[i*i for i in list1]
# print(res)  # [1, 4, 9, 16, 25]

# # we will print the even number 1 to 20 
# res=[i for i in range(1,21) if i%2==0]
# print(res)  # [2, 4, 6, 8, 10,

# # we will print the square of the even numbers of 1 to 20 
# res=[i*i for i in range(1,21) if i%2==0]
# print(res)  # [4, 16, 36, 64, 100,


# odd=[i for i in range(1,21) if i%2!=0]
# print(odd)
# odd=[i*i for i in range(1,21) if i%2!=0]
# print(odd)

# # sum of list element 
# list1=[1,2,3,4,5]
# res=sum([i for i in list1])
# print(res) 
# #sum of  even element 
# list1=[1,2,3,4,5,6,7,8,]
# res=sum([i for i in list1 if i%2==0])
# print(res) 

# #you need to print 1st chara of string 
# list1=["banana ","apple","charry ","kivi"]
# res=[i[0] for i in list1]
# print(res)

# # fetch those string start with vowels 
# list1=["alice","kivi","kiya ","illina "]
# res=[i for i in list1 if i[0] in 'aeiou']
# print(res)  #

# 1. From a list of words, get the length of each word.l=["hello","hii","welcome","thankyou"]
l=["hello","hii","welcome","thankyou"]
res=[len(i) for i in l]
print(res)  # [5, 3, 7, 9]
# 2. Create a list of numbers from 1 to 50 that are divisible by both 3 and 5.[11,23,15,30,67,45]
res=[i for i in range(1,51) if i%3==0 and i%5==0]
print(res)  
# 3. Get the first letter of each word in a list if the word has more than 3 letters. 
w=["jay","kiya","jefff","lilyy"]
res=[i[0] for i in w if len(i)>3]
print(res)  # ['j', 'k', 'j']
# 4. Print the table of 8.
res=[i*8 for i in range(1,11)]
print(res)  # [8, 16, 24, 32, 40,
# 5. Write a Python program that takes a list of integers and returns the sum of the squares of the even numbers using list comprehension.
#    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#    Output: 220
numbers = [1, 2, 3, 4, 5, 6,7,8,9,10]
res=sum([i*i for i in numbers if i%2==0])
print(res)  # [4, 16, 36, 64, 100,
# 6. sentence = "list comprehension is cool" From sentence extract only vowel.
sentence = "list comprehension is cool"
res=[i for i in sentence if i in 'aeiou']
print(res)  # ['i', 'e', 'o']
# 7. Write a Python program that takes a list and returns a new list containing only the unique elements using list comprehension.
#    elements = [1, 2, 3, 2, 4, 5, 6, 3, 7]
#    Output: [1, 4, 5, 6, 7]
elements = [1, 2, 3, 2, 4, 5, 6, 3, 7]
res= [i for  i in elements if elements.count(i) == 1]
print(res)

# 8.  Given a list of integers, return a list with all negative numbers removed.
#    numbers = [-1, 2, -3, 4, -5, 6]
#    Output: [2, 4, 6]
numbers = [-1, 2,-3,4,-5,6]
res=[i for i in numbers if i>=0]
print(res)  # [2, 4, 6]
# 9 find the common element in two list using list comperhension 
list1=[1,2,3,4]
list2=[3,4,5,6]
res=[i for i in list1 if i in list2]
print(res)  # [3, 4]

# 10.Write a Python program that takes a list of integers and returns the count of the odd numbers using list comprehension.
numbers = [1, 2, 3, 4, 5,6,7,8,9]
odd=[i for i in numbers if i%2!=0]
print(odd)
res=len([i for i in numbers if i%2!=0])
print(res)  # 5