# what is hof 
# hof is a higher order function
# a higher order function is a function that takes another function as an argument or returns a function as
# its result
# hof is used to abstract away common logic and make code more reusable and modular
# hof is used to create a function that can be used to create other functions
'''
there are mainaly 3 inbuilt hof 
1.map
2 filter 
3 reduce
# map is used to apply a function to each item in an iterable
# filter is used to filter out items from an iterable based on a condition
# reduce is used to apply a function to each item in an iterable and reduce it to a singl
# value


 map function 
 syntax  
 map(function,iterable)



'''
def add(x):
    return x +2

l=[1,2,3,4,5]
res=list(map(add,l))
print(res)  #output [3, 4, 5, 6,7]



def add(x):
    return x *2

l=[1,2,3,4,5]
res=list(map(add,l))
print(res)


# map function using lamda :
l=[1,2,3,4,5]
l1=[5,8,2,1,8]
res=list(map((lambda x,y:x+y),l,l1))
print(res)  #output [6, 10, 5, 5, 13


# convert all word into the upper case 
word=["hello","word","python "]
res=list(map(str.upper,word))
r=list(map((lambda x: x.upper()),word))
print(r)
print(res)  #output ['HELLO', 'WORD', 'PYTHON ']

'''
Write a Python program that takes a list of numbers 
and returns a new list containing the squares of those numbers using the map() function 
and a user-defined function.
'''
def square(x):
    return x ** 2
numbers = [1, 2, 3, 4, 5]
result = list(map(square, numbers))
print(result)  # output [1, 4, 9, 16, 25

numbers = [1, 2, 3, 4, 5]

result = list(map(lambda x: x ** 2, numbers))
print(result)  # output [1, 4, 9, 16, 25

# find the squre of the number 
l=[2,3,5]
res=list(map(lambda x:x*2,l))
print(res)



# filter function
# filter (function,itrable ) 
# need to print only even number 

l=[1,2,3,4,5]
def even(num):
    if num % 2 == 0:
        return num

res=list(filter(even,l))
print(res)

# using lambda function 
r=list(filter((lambda x :x %2==0),l))
print(r)

'''
filter the strint with length > 3
word=["sun","moon","sky","planet"]

'''
word=["sun","moon","sky","planet"]
l=len(word)
def a(x):
    return len(x) > 3
   
res=list(filter(a,word)) 
print(res )   


f= list(filter(lambda x: len(x) > 3, word))
print(f)
