# tuple 
'''

tuple :- sequence data type 
it is ordered and unchangeable.
tuple is collection of hetrogeneous data 
tuple is enclosed in round brackets ()
tuple is immutable means it cannot be changed after it is created.  

allow duplicats 
immutable 

'''
# t=(1,2,3,"jay",52)
# print(t)
# print(type(t))
# print(len(t))

# # if i want to craete a tuple witha a single element 
# t=(1,) # comma is must after the element
# print(t)
# print(type(t))

# # indexing and slicing 
# t=(10,20,30,40,50,60,70,80,90)
# print(t[0]) # indexing
# print(t[1:5]) # slicing
# print(t[1:]) # slicing
# print(t[:5]) # slicing


t = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
# output:(30, 40, 50, 60)
print(t[2:6])
# output:(10, 20, 30, 40)
print(t[0:4])
# output:(60, 70, 80, 90, 100)
print(t[5:10])
# output:(10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
print(t)
# output:(10,30,50,70,90)
print(t[::2])
# output:(100, 90, 80, 70, 60, 50, 40, 30, 20, 10)
print(t[::-1])
# output:(100, 80, 60, 40, 20)
print(t[::-2])
# output:(90,100) By negative slicing
print(t[-2:])

# extract all the even number using slicing 
t=(1,2,3, 4,5,6,7,8,9,10)
print(t[1::2]) # even number
# extract all the odd number using slicing
print(t[::2]) # odd number


# nexted slicing 
list1=[[1,2,3],[4,5,7,8]]
print(list1[0][0])
print(list1[0][1])
print(list1[0][2]) 

print(list1[1][0]) 
print(list1[1][1])
print(list1[1][2])
print(list1[1][3])


l=[1,2,3,4,[5,6,7,"jay"]]
print(l[4][3]) # 5

l=[1,2,3,4,[5,6,7,"jay"],[1,2,3,"jiya"]]
print(l[5][3]) # jiya 
#fetch bill gates 
l=[1,2,3,[6,"bill",6,7],5,[1,2,"gates"],"jeh"]
a=(l[3][1])
b=(l[5][2])
print(a,b) 
# fetch jeff raw
l=[1,2,3,["jeff",4,5],3,(2,3,("raw")),8,9]
a=(l[3][0])
b=(l[5][2])
print(a,b)

# fetch daniel
x=[[[("daniel")]]]
print(x[0][0][0]) # danile


#fetch steve woz jeff

x=[1,2,[11,("steve",33)],[["woz"],"jeff"]]
a =( x[2][1][0])
b = (x[3][0][0])
c = (x[3][1])
print(a,b,c) # steve woz jeff

# packing and unpaking of tuple 
# pacikng allows assing mlutipla value for single tuple 
# unpacking allows to unpack the tuple into multiple variable
# packing
x="jay","jiya","jiyajiya",22,52
# print(type(x))
print(x)
print(type(x))
# unpacking extract the value into the seprect variable 
t=("jay",89,"uma",66)
a,b,c,d=t
print(a)
print(d)
# unpacking extract the value into the seprect variable
print(a,b,c,d)
#how to iterate a tuple 
tup1=(1,2,3,4,5)
for i in tup1:
    print(i)

tup1=(67,5,6,23,5,5)
print(tup1.count(5))
# how to find the index of the tuple
tup1=(1,2,3,4,5)
print(tup1.index(5))
# can we store list in tuple 
tup1=(1,2,3,4,5,[4,5,2,])
print(tup1)
print(type(tup1))
# In Python, you can store a list within a tuple. However, the list itself is not
# immutable, it's the tuple that is immutable. So, you can modify the list within
# the tuple, but you cannot modify the tuple itself.
tup1[5][0]="jay"

print(tup1)
# how to add element in tuple 
# tuples are immutable so we can't add element in tuple
# but we can convert tuple into list and then add element in list and then convert list into tupl
tup1=(1,2,3,4,5)
l=list(tup1)
# convert tuple into list
l.append(600)
# add element in list
# convert list into tuple
tup1=tuple(l)
print(tup1)


#concat
# it will concatenate two list
list1=(1,2,3,4,5)
list2=(6,7,8,9,10)
res=list1+list2
print(res)
#product of list 
l=[1,2,3,4,5]
res=l*2
print(res)

print(max(list1))
print(min(list1))
print(sum(list1))

list1=[[1,2,3,4],[7,6,4,3,2]]
for i in list1:
    for j in i:
        print(j,end="\n " )


tup1=((1,2,3,4),(22,5,6,5))
for i in tup1:
    for j in i:
        print(j,end=" ")

# 1. Python program to find tuples which have all elements divisible by K from a list of tuples
# Input : test_list = [(6, 24, 12), (60, 12, 6), (12, 18, 21)], K = 6 
# Output : [(6, 24, 12), (60, 12, 6)] 
# Explaination : Both tuples have all elements multiple of 6.
test_list = [(6, 24, 12), (60, 12, 6), (12, 18, 21)]
K = 6
# using list comprehension to filter tuples
for i in test_list:
    if all(j % K == 0 for j in i):
        print(i)



test_list = [(6, 24, 12), (60, 12, 6), (12, 18, 21)]
K = 6
result = []

for tup in test_list:
    is_divisible = True  
    for j in tup:
        if j % K != 0:
            is_divisible = False  
    if is_divisible:
        result.append(tup)
print("Tuples with all elements divisible by", K, ":", result)

# 2. Python program to find Tuples with positive elements in List of tuples
# Input : test_list = [(4, 5, 9), (-3, 2, 3), (-3, 5, 6), (4, -6)] 
# Output : [(4, 5, 9)] 
# Explaination : Extracted tuples with all positive elements.

test_list = [(4, 5, 9), (-3, 2, 3), (-3, 5, 6), (4, -6)] 
res=[]
for i in test_list:
    zero=True
    for j in i:
        if j<=0:
            zero=False
    if zero:
        res.append(i)
print(res)
        
 # 3. Python | Removing duplicates from tuple
# The original tuple is : (1, 3, 5, 2, 3, 5, 1, 1, 3)
# The tuple after removing duplicates : (1, 3, 5, 2)
tup1 =(1, 3, 5, 2, 3, 5, 1, 1, 3)
res=[]
for i in tup1:
   if i not in res:
      res.append(i)
print(res)


# 4. Python | Remove duplicate lists in tuples (Preserving Order)

# The original tuple is : ([4, 7, 8], [1, 2, 3], [4, 7, 8], [9, 10, 11], [1, 2, 3])
# The unique lists tuple is : [[4, 7, 8], [1, 2, 3], [9, 10, 11]]

tup1=([4, 7, 8], [1, 2, 3], [4, 7, 8], [9, 10, 11], [1, 2, 3])
res=[]
for i in tup1:
    if i not  in res:
        res.append(i)
print(res)

# Write a  Python program to remove an empty tuple(s) from a list of tuples.
# Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
# Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']

l= [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
res=[]
for i in l:
    if i :
        res.append(i)
print(res)

# 5. Python – Sum of tuple elements
# The original tuple is : (7, 8, 9, 1, 10, 7)
# The summation of tuple elements are: 42
tup1 = (7, 8, 9, 1, 10,7)
res = sum(tup1)
print(res)



# All the zeros (0) should be in left side of the list and 1 should be in roght side. 
#    list1=[1,0,1,0,0,1,1]
#    output:[0,0,0,1,1,1,1]
list1=[1,0,1,0,0,1,1]
list1.sort()
print(list1)


list1 = [1, 0, 1, 0, 0, 1, 1]
zeros = []
ones = []
for i in list1:
    if i == 0:
        zeros.append(0)
    else:
        ones.append(1)
list1 = zeros + ones

print(list1)
