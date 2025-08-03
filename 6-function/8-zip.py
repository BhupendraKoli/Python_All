# Zip function:

'''
The main function of paired a data to multiple function.
zip function also return the object.

'''
list1=[1,2,3,4]
list2=["komal","lina","omakar","piyu"]

res=tuple(zip(list1,list2))
print(res)

# ((1, 'komal'), (2, 'lina'), (3, 'omakar'), (4, 'piyu'))

res=list(zip(list1,list2))
print(res)

# [(1, 'komal'), (2, 'lina'), (3, 'omakar'), (4, 'piyu')]

res=dict(zip(list1,list2))
print(res)

# {1: 'komal', 2: 'lina', 3: 'omakar', 4: 'piyu'}  


# keys: multiple of 3
# values: multiple of 5
# Create dictionary using zip function


keys=[i * 3 for i in range(1,6)]
values=[i*5 for i in range(1,6)]

d=dict(zip(keys,values))
print(d)

# {3: 5, 6: 10, 9: 15, 12: 20, 15: 25}

# even keys between 10-20
# odd values between 0-10
# Create a dictionary using zip function

keys=[i for i in range(10,21) if i%2==0]
values=[i for i in range(0,11) if i%2!=0]

d=dict(zip(keys,values))
print(d)

# {10: 1, 12: 3, 14: 5, 16: 7, 18: 9}

#isinstance()

# isstance is a bulding function which use to check if a variable is an 
# instance of certain time.

x=5

print(isinstance(x,int))
# True

print(isinstance(x,str))
#False



