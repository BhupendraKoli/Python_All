# # iterative for loop
# l=[4,1,2,2,25]
# print(l)

# for i in l:
#     print(i)

#len function 
'''
The len() function returns the number of items in an object.
len is in bulit function in python 
that return the number of element in an object
exces one one element 


'''    
# print(len(l))

# l=[4,1,2,2,25]

# for i in range (len(l)):
#     print(l[i])

# # will print index with values in the list 

# l=[50,60,70,80,90,100]
# for i in range(len(l)): # 
#     print(i, ":",l[i]) # will print index of the list not the value of the 
    

# l=[50,60,70,80,90,100]
# for i in l:  # i has value 
#     print(l.index(i),":",i) # will print value of the list not the index of the list


# # will print the even element of the list
# l=[50,60,70,85,97,100]
# for i in l:
#     if i%2==0:
#         print(i)

# # will print all even indexed elements
# l=[55,65,75,85,97,101]
# for i in range(len(l)):
#     if i%2==0:
#         print(l[i],":",i)

# # will print the odd element of the list
# l=[50,60,70,85,97,100]
# for i in l:
#     if i%2!=0:
#         print(i)


# # will print all odd indexed elements
# l=[55,65,75,85,97,101]
# for i in range(len(l)):
#     if i%2!=0:
#         print(l[i],":",i)


# print the list in revers way
# l=[50,60,70,80,90,100]

# for i in range(len(l)-1,-1,-1):
#     print(l[i],end=" ")


# Questions:

# print the elements of list l=[6,5,4,3,2,1]
l=[6,5,4,3,2,1]
for i in l:
    print(i,end=" ") # will print all elements of the list  


# print the no not divisible by 5 from list l=[1,2,3,5,15,10,4]

a=[1,2,3,5,15,10,4]
for i in a:
    if i%5!=0:
       print(i)

# # print the no divisible by 3 from list l=[1,2,3,5,6,10,9]
l=[1,2,3,5,6,10,9]
for i in l:
    if i%3!=0:
       print(i, end=" ") 
# # print the even indexed elements of list l=[16,15,11,13,1,10]
l=[16,15,11,13,1,10]
for i in range(len(l)):
    if i%2==0:
        print(l[i],":",i)  # will print the even indexed elements of the list

# # print the elements of list which are not s l=['a','z','s','x','p']

l=['a','z','s','x','p']
for i in l:
    if i!='s':
        print(i)  # will print all elements except 's' from the list

