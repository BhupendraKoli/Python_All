# string 
#what is string ?
#string is a sequence of characters
#string is a collection of characters
#string is a sequence of characters enclosed in quotes
'''
string squence data type 
collection of hetreogeounes data type 
string is a collection of characters
string is a sequence of characters enclosed in quotes
indexed and orderde
im mutable 
allow duplicats 
enclosed in single doubole triple codes 


'''
# string="Im from pune"
# print(string)
# print(type(string))
# print(len(string))

# print(string[0])

# print(string[8:13])

# text = "Hello, World!"

# # o/p:Hello by +ve slicing
# print(text[:5])
# # o/p:World!  by +ve slicing
# print(text[7:])
# # o/p:Hello by -ve slicing
# print(text[:-6])
# # o/p:World! by -ve slicing
# print(text[-7:])



# inbuilt method in string 
#1. lower()
#2. upper()
#3. title()
#4. count()
#5. find()
#6. replace()
#7. split()
#8. join()
#9. strip()
#10. lstrip()
#11. rstrip()
#12. isalnum()
#13. isalpha()
#14. isdigit()
#15. islower()

string="mumbai"
s=string
#upper
#lower
print(s.upper()) #MUMBAI
print(s.lower()) #mumbai
# #title
# print(s.title()) #Mumbai
# #count
# print(s.count('m')) #2
# #find
# print(s.find('m')) #0
# #replace
# print(s.replace('m','M')) #Mumbai
# #split
# print(s.split('u')) #['mumba', 'i']


#strip()
#it will removw the white spaces form the both site
# s="   pune   "
# print(len(s))
# res=s.strip()
# print(res)
# print(len(res)) #pune

s="      mumbai      "
print(len(s))
res=s.lstrip()
print(res) #mumbai
print(len(res))
# rstrip()
res=s.rstrip()
print(res) #mumbai

#spilt() imp function 
#it will split the string into list

s="this is pune"
res=s.split()
print(res) #['this', 'is', 'pune']

s="this is-pune"
res=s.split('-')
print(res) #['this is pune']

# take the full name of the user it must have first name middle name last name .
# print it with using f string 
# name=str(input("enter your full name "))
# s=name.split()
# if len(s)==3:
#     print(f"first name is {s[0]} middel name {s[1]} last name{[2]}")
# else:
#     print("invalid name")

# full_name = input("Enter your full name : ")
# first, middle, last = full_name.split()
# print(f"Your full name is: {first} {middle} {last}")

#replace 
#it will replace the string with the other string
s="pune is good city"
print(s.replace('pune','mumbai'))
#output mumbai is good city  

s="hello this is my friend vani"
res=s.replace('vani','komal')
print(res) #hello this is my friend komal

# captilize 
# it will convert the first letter of the string into capital letter
s="hello this is my friend vani"
res=s.capitalize()
print(res) #Hello this is my friend vani
# title()
# it will convert the first letter of each word into capital letter
s="hello this is my friend vani"
res=s.title()
print(res) #Hello This Is My Friend Vani

# swapcase()
# it will convert the capital letter into small letter and small letter into capital letter
s="Hello"
res=s.swapcase()
print(res) #hELLO
# casefold()
# it will convert the string into lower case letter
s="Hello"
res=s.casefold()
print(res) #hello

#.format()
name="komal"
age=20
res="my name is {} and my age is {}".format(name,age)
print(res)

#output my name is komal and my age is 20

#you need to print your basic info using .formate 
name="Bhupendra"
age=20
add="jalgoan"
edu="BCA "
res="my name is {} and my age is {} and i am from {} and i have done {}".format(name,age,add,edu)
print(res)
#output my name is Bhupendra and my age is 20 and i am from jalgoan and i have done BCA

#count()
# it will count the number of times the string is present in the string
# s="hello hello hello"
# sub=input("enter the substrung:-")
# res=s.count(sub)
# print(res) #6

s="hello hello hello"
res=s.count("l")
print(res) #6

# startsswith()
# it will check whether the string starts with the given string or not
# boolen value return 
s="hello world"
res=s.startswith("h")
print(res) #True

# endswith()
# it will check whether the string ends with the given string or not
# boolean value return
s="hello world"
res=s.endswith("d")
print(res) #True

# find()
# it will return the index of the first occurrence of the given string in the string
# if the string is not found it will return -1
s="hello world"
res=s.find("o")
print(res) #4
# find() function is case sensitive

# index()
# it will return the index of the first occurrence of the given string in the string
# if the string is not found it will raise a value error
s="hello world"
res=s.index("o")
print(res) #4

# rfind and rindex 
# it will return the index of the last occurrence of the given string in the string

s="hello world"
res=s.rindex("o")
print(res) #4

s="hello world"
res=s.rfind("o")
print(res) #4

# center(length , chara)
# it will return a string that is centered in a string of given width
# it will pad the string with the given character
s="hello"
res=s.center(10,"*")
print(res) #*****hello*****
# ljust(length , chara)
# it will return a string that is left justified in a string of given width
# it will pad the string with the given character

# check a number is automorphic or not ?
# automorphic number is number whose square  endwith the number itself 
# 5 is automorphic number because 5*5 = 25 and 25 end with
# 5

# num=int(input("enter the number "))
# squre=num*num
# str_num=str(num)
# str_squre=str(squre)
# if str_squre.endswith(str_num):
#     print(num,"is automorphic number")
# else:
#     print(num,"is not automorphic number")


# isalnum ()
# it will return true if all the characters in the string are alphanumeric
# i.e either digit or alphabet
# it will return false otherwise
s="hello123"
res=s.isalnum()
print(res) # true 
# isalpha ()
# it will return true if all the characters in the string are alphabet
# it will return false otherwise
s="hello123"
res=s.isalpha()
print(res) # false

# isdigit ()
# it will return true if all the characters in the string are digit
# it will return false otherwise]
s="123"
res=s.isdigit()
print(res) # true

# isascii()
# isascci checek the all alphtabet number ans special charter also 
# it will return true if all the characters in the string are ascii
# it will return false otherwise
s="hello125@"
res=s.isascii()
print(res) # true

# islower 
# it will return true if all the characters in the string are in lower case
# it will return false otherwise
s="hello"
res=s.islower()
print(res) # true
# isupper()
# it will return true if all the characters in the string are in upper case
# it will return false otherwise
s="HELLo"
res=s.isupper()                                         
print(res) # true

# join ()
# it will convert elements of iterables into string
# it will join all the elements of the list into a string
# it will take a string as an argument
# it will return a string where all the elements of the list are joined by the string
# s=" "
l=["hello","world","banana"]
res= " ".join(l)
print(res) # hello world banana

t=("jon","peter","vicky")
res= "@".join(t)
print(res) # jon@peter@vicky

# isspace ()
# it will return true if all the characters in the string are space
# it will return false otherwise
s="   "
res=s.isspace()
print(res) # true


# # 1. WAP to print all the consonants char from the String.
# text = "hello"
# vowels = "aeiouAEIOU"
# print("Consonants in the string are:")
# for char in text:
#     if char.isalpha() and char not in vowels:
#         print(char, end='')


# # 2. Print the words which starts from vowels in list.["amayra","rohit","illina","virat"]
# s=["amayra","rohit","illina","virat"]
# for i in s:
#     if i[0].lower() in 'aeiou':
#         print(i)

# # 3. WAP to convert all the consonants char in lowercase case.
# s="HELLO WORD"
# res=s.lower()
# print(res) # hello word
# # 4. WAP to check whether the all strings are in upper case or not:
# s="HELLO"
# res=s.isupper()
# print(res) # true
# # 5.WAP to check whether the all strings are in lower case or not:
# s="hello"
# res=s.islower()
# print(res) # true

# # wap to replace all vowel char to # and consonant chr to *
# s="hello world"

# s = input("Enter a string: ")
# for ch in s:
#     if ch.lower() in 'aeiou':
#         print('#', end='')
#     elif ch.isalpha():
#         print('*', end='')
#     else:
#         print(ch, end='')

# # WAP to replace all vowel chars with '#' and consonant chars with '*'

# text = input("Enter a string: ")
# result = ""

# for char in text:
#     if char.lower() in 'aeiou':
#         result += '#'
#     elif char.isalpha():
#         result += '*'
#     else:
#         result += char  # Keep spaces, digits, punctuation unchanged

# print("Modified string:", result)

# # wap to relpave all even positio char to  % 
# s = input("Enter a string: ")
# result = ""
# for i in range(len(s)):
#     if (i) % 2 == 0: 
#         result += '%'
#     else:
#         result += s[i]

# print("Modified string:", result)

# partition 
# it is use to seprated a string on specifified and return a tuple
s="i like python and  java "
res=s.partition("python")
print(res) # ('i like ', 'python', ' and  java ')

# rpartition()
# it is use to seprated a string on specifified and return a tuple
# it is work from right side
s="i like python and  java and  java script"
res=s.rpartition("java")
print(res) # ('i like python and  ', 'java', ' and  java script')

#zfill()
# add the zero at the beging of the string until it reche at specified lenthe 
# it is use to fill zero in the left side of string
# it is use to make the string of equal length'
s="123"
res=s.zfill(5)
print(res) # 00123

# print the string with with index number 
s="i am a data scientist"
for i in range(len(s)):
    print(f"{i}   {s[i]}")


# reverse a string 
# it is use to reverse the string
s="123456789"
res=s[::-1]
print(res) 

# revers the string using loop 
s="123456789"
res = ""
# for i in range(len(s)-1,-1,-1):
#     res += s[i]
# print(res)

for i in s :
    res=i+res
print(res)

# sorted ()
# it is use to sort the string
# it is use to sort the string in alpabetical order

s="python"
res=sorted(s)
print(res)

# need to check the given string are anagraams or not 
# anagram is a word or phrase formed by rearranging the letters of a different word or phras
# it is use to check the given string are anagram or not

# net ten
# pot top 
# a man a plan a canal panama

# str1 = input("Enter first string: ")
# str2 = input("Enter second string: ")

# if sorted(str1) == sorted(str2):
#     print("Strings are anagrams")
# else:
#     print("Strings are not anagrams")

# to get the output s="123"
l=[1,2,3]
s = " "
for i in l:
    s += str(i)
print(s)

# WAP and print len of word and word in a tuple of a list.
word = ["aman", "virat", "rohiiiit", "siyaa"]
result = []
for i in word:
    result.append((len(i), i ))

print(result)


#input  s="1,2"
# output l=[1,2]
# using list comprehension 
s="1,2"
l = [int(i) for i in s.split(",")]
print(l)

# input "i like python "
#output "python like i "
 
s = "i like python "
l = s.split()
l.sort(reverse=True)
s = " ".join(l)
print(s)

s="i like python "
l = s.split()[::-1]
s = " ".join(l)
print(s)

# Reverse the words, order should be maintained
# str="Hello world "
# output: "olleh dlrow"
s = "Hello world "
l = s.split()[::-1]
s = " ".join(l)
print(s[::-1])

s="hello word"
word=s.split()
for i in word :
    print(i[::-1], end=" ")

# 1.WAP to print the username only from the list of email
# # input= ["virat@gmail.com","dhoni@gmail.com","rohit@gmail.com"]
# # output: [virat,dhoni,rohit]
# email=["virat@gmail.com","dhoni@gmail.com","rohit@gmail.com"]

s= ["virat@gmail.com","dhoni@gmail.com","rohit@gmail.com"]
# output: [virat,dhoni,rohit]
s=[i.split("@")[0] for i in s]
print(s)
# using for loop 
s= ["virat@gmail.com","dhoni@gmail.com","rohit@gmail.com"]
a=[]
for i in s:
    a.append(i.split("@")[0])
print(a)

# # 2.Count Words in a Sentence:
# # # Given a sentence, count the number of words in it using the split method.
# string="hello this is a final match"
# output: 6
string="hello this is a final match"
print(len(string))
print(len(string.split()))

# # 3.Extract Domain Names from Emails:
# # # Given a list of email addresses, extract the domain names using the split method
# input= ["user1@example.com", "user2@domain.com", "user3@company.org"]
# output: ["example.com", "domain.com", "company.org"]input= ["user1@example.com", "user2@domain.com", "user3@company.org"]

str= ["user1@example.com", "user2@domain.com", "user3@company.org"]
str=[i.split("@")[1] for i in str]
print(str)

# 4. Convert a Sentence into a List of Words:
#    Given a sentence, convert it into a list of words.
s="hello what are you doing ?"
s=s.split()
print(s)

# 5. Find the Longest Word in a Sentence:
# # Given a sentence, find the longest word using the split method.
# # sentence = "Identify the longest word in this sentence."
# # output: 'sentence.'
sentence = "Identify the longest word in this sentence."
# using max function

srt1=len(sentence)
max(sentence.split())
print(srt1)
# using for loop
sentence = "Identify the longest word in this sentence."
max_word = ""
for word in sentence.split():
    if len(word) > len(max_word):
        max_word = word
print(max_word)


# 6.Check for Palindrome Words in a Sentence:
# #Given a sentence, check which words are palindromes using the split method.
# #sentence = "Madam Arora teaches malayalam"
# #output: ['madam', 'Arora', 'malayalam']
sentence = "Madam Arora teaches malayalam"
# using list comprehension
palindrome_words = [word for word in sentence.split() if word.lower() == word.lower()[::-1]]
print(palindrome_words)
# USING FOR LOOP 
sentence = "Madam Arora teaches malayalam"
palindrome_words = []
for word in sentence.split():
    if word.lower() == word.lower()[::-1]:
        palindrome_words.append(word)
print(palindrome_words)
