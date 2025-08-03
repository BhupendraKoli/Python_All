# Enumerate function:

'''
Enumerate is a small inbuit function in a python which is specially used to extract a index and value from a itterable.

'''

list1=[11,22,33,44,55]

for i in range(len(list1)):
    print(i,list1[i])

# By using enumerate function:

list1=[11,22,33,44,55]

for index,val in enumerate(list1):
    print(index,val)

fruit=["apple","grapes","lichy"]

for i,val in enumerate(fruit,start=2):
    print(i,val)

# You need to convert a list into dictionary by using enumerate.

list1=["hello","hi","Thankyou"]

d={}

for i,val in enumerate(list1):
    d[i]=val
print(d)









