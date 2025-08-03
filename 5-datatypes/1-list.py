# sequence data type 
'''
List :-
list is a collection hetrogeneous data 
list is indexed and ordered
list is sequence data type that cantion all data types 
list is mutable (changeing modify the list )
allow duplicatis value 
list are created using square brackets [] or the list() function 



'''
# # creating a list
# my_list = [1, 2, 3, 4, 5,"jay ",True,6+7j]
# print(my_list)


# list1=list((1,2,3,2,5,8))
# print(list1)
# print(type(list1))


# l=[]
# print(l)
# # list in order 
# l=[1,2,3,4,5]
# print(l)

# #list are indexed
# list5=[40,52,56,58,59,]
# print(list5[0]) # using index value 
# #syntax data_type_name[index number]
# print(list5[2])


# list2=[65,66,67,68,69]
# print(list2[3])
# print(list2[0])
# print(list2[2])
# print(list2[4])

# #negstive index start form -1 and start form end 
# #last element
# print(list2[-1])
# print(list2[-5])

# # slicing we can slice the range value of element 
# # syntax data_type_name[start index : end index : step value]
# #default value of start index is 0 and end index is last index and step value is
# # positive indexing 
# mylist=[45,67,12,34,11,89,43,23]
# print(mylist[0:3])
# print(mylist[3:6])
# print(mylist[0:6:2])
# print(mylist[::]) # all list will be print 
# print(mylist[::2]) # all list with step value 2 will be print
# print(mylist[5::])
# print(mylist[1:4])
# print(mylist[::-1])
# print(mylist[::3])

# #nagative indexing
# print(mylist[-8:-5])
# print(mylist[-5:-2])
# print(mylist[-8:])


# l=[7,6,4,5,3,2,1]

# # o/p : 5 using positive indexing
# # o/p : 5 using negative indexing
# # o/p : [4,5,3] using positive slicing
# # o/p : [4,5,3] using negative slicing
# # o/p : [1,2,3,5,4,6,7]
# # o/p: [7,4,3,1]
# # o/p: [1,3,4,7]
# print(l[3])
# print(l[-4])
# print(l[2:5])
# print(l[-5:-2])
# print(l[::-1])
# print(l[::2])
# print(l[-1::-2])

# l=[2,3,4,5,6,7,8]
# print(l[4:]) # useing +ve slicing 
# print(l[-3:]) # use -ve slicing



# # mutablitiy modification of list 
# list3=[23,45,67,12,89,34]
# list3[0]=230 # list is mutable so we can modify it
# print(list3)

# list3[0:2]=["koli","jem","lll"]
# print(list3)
# print(list3[2])
# print(list3[3])
# print(list3)

# #inbulit methods of list 
# #append() method add element in last  but in single index  emlemnt 
# # it willadd an element of the  end of the list at single index
# list4=[1,2,3,4,5,6,7,8,9]
# list4.append(10)
# print(list4)

# list4=[1,2,3,4,5,6,7,8,9]
# list4.append((10,"koli"))
# print(list4)
# print(list4[-1])

# # extend()
# # extend() method add multiple element in list at last index
# list4=[1,2,3,4,5,6,7,8,9]
# list4.extend([10,20,30,40,50])
# print(list4)
# print(list4[-1])


# # insert() 
# #insert(position,elemnt)
# # insert() method add element in list at specific index
# l=[1,2,3,4,5]
# l.insert(3,10)
# print(l)
# l.insert(0,100)
# print(l)
# l.insert(0,[101,202])
# print(l)
# print(l[0])
# l.insert(-1,500)
# print(l)

# # remove() method remove element from list
# list1=[67,12,89,34,23]
# list1.remove(12)
# print(list1)


# list1=[67,12,89,34,23,12]
# list1.remove(12)
# print(list1)
# # pop method
# # pop() method remove element from list at specific index last value 

# list1=[67,12,89,34,23,12]
# list1.pop()
# print(list1)
# # clear()
# # clear() method remove all element from list
# # struture will remains 
# list1=[67,12,89,34,23,12]
# list1.clear()
# print(list1)

# # delet
# # del keyword remove element from list at specific index
# # delete permenantly 

# list8=[67,12,89,34,23,12]
# del list8[2] 
# print(list8)

# list8=[67,12,89,34,23,12]
# del list8[0:2] 
# print(list8)


# list8=[67,12,89,34,23,12]
# del list8[::2] 
# print(list8)


# # Write a program to count the elements in a list.
# l1=[1,2,3,4,5,6]
# s=0
# for i in l1:
#    s=s+1
# print(s,end=" ")
# print("\n ----------------")

# # # or
# l1=[1,2,3,4,5,6]
# s=len(l1)
# print(s,end=" ")
# print("\n ----------------")

# # Write a program to sum of elements in a list.
# l1=[1,2,3,4,5,6]
# total=sum(l1)
# print(total,end=" ")
# print("\n ----------------")


# # WAP to remove all the negative elements from lits.
# l1=[1,2,-3,4,-5,6]
# res=[]
# for i in l1:
#     if i>=0:
#      res.append(i)
# print(res)
# print("\n ----------------")


# # WAP to remove the duplicates element from the list
# #  list1=[2,3,3,4,6]
# #  output: [2,3,4,6]
# l1=[2,3,3,4,6]
# l1.remove(3)
# print(l1)

# # remove all the three in the list 
# # list1=[2,3,3,4,6]
# # output: [2,4,6]
# l1=[2,3,3,4,6]
# for i in l1:
#    if i!=3:
#       print(i,end=" ")
  
# l1=[2,3,3,4,6,2]
# res=[]
# for i in l1:
#    if i not in res:
#       res.append(i)
# print(res)


# # write a program to print the square of all list items:[1,2,3,4]
# l1=[1,2,3,4]
# for i in l1:
#    print(i**2,end=" ")
# print("\n ----------------")
# # Add single element at the end of the list.
# l1=[4,5,6,7,8]
# l1.append(9)
# print(l1)
# print("\n ----------------")
# # Add multiple elements at the end of the list.
# l1=[4,5,6,7,8]
# l1.extend([9,10,11])
# print(l1)

# # index ()
# # it will give the first index position of 1st occurance of speficied value 
# l1=[1,2,3,5,6,8,2]
# print(l1.index(2))  # output: 1

# # count()
# # it will give the count of the specified value in the list
# l1=[1,2,3,5,6,8,2,2,2,2,]
# print(l1.count(2))  # output: 2

# #reverse()
# # it will reverse the list
# l1=[1,2,3,5,6,8,]
# l1.reverse()
# print(l1)  # output: [2, 8, 6, 5,

# #sort()
# # it will sort the list in ascending order
# l1=[1,4,3,5,6,2]
# l1.sort()
# print(l1)  # output: [1, 2, 3, 5,

# # print given list in descending order 
# l1=[1,4,3,5,6,2]
# l1.sort(reverse=True)
# print(l1)  # output: [6, 5, 4, 3,

# list1 = [11,93,12,12,89]
# list1.sort()
# list1.reverse()
# print(list1)

# #concat
# # it will concatenate two list
# list1=[1,2,3,4,5]
# list2=[6,7,8,9,10]
# res=list1+list2
# print(res)
# #product of list 
# l=[1,2,3,4,5]
# res=l*2
# print(res)

# #min and mix and  sum
# list1=[23,52,56,5,96]
# print(min(list1))
# print(max(list1))
# print(sum(list1))


# # deep copy 
# # it will create a copy of the list\
# # the changes will replact in orignal list also
# a=[1,2,3,4,5]
# b=a
# b.append(100)
# print("orignal list",a)
# print("copied list",b)

# #shallow copy
# # it will create a copy of the list
# # the changes will not replact in orignal list
# # it will created using .copy() function 
# a=[1,2,3,4,5]
# b=a.copy()
# b.append(100)
# print("orignal list",a)
# print("copied list",b)
# print(id(a))
# print(id(b))
# # id() function returns the unique identifier of the specified object.
# # id() function returns the “identity” of the object which is an integer that is guaranteed to
# # be unique and constant for the object during its lifetime.
# # id() function is used to check whether the object is the same or not. If the id   
# # of two objects are same then it means both objects are same.


# WAP to find the avg of all the items from the list

l= [10, 20, 30, 40, 50]
total = sum(l)
count = len(l)
if count > 0:
    average = total / count
    print("Average of the list  is:", average)
else:
    print("The list is empty")


# WAP to print the sum of all the even items in a list 
l = [11, 20, 30, 45, 50, 69]
even_sum = 0
for i in l:
    if i % 2 == 0:
        even_sum += i
print("Sum of all even items in the list is:", even_sum)

# WAP to print the sum of all the odd items in a list 
l = [11, 20, 30, 45, 50, 45]
odd_sum = 0
for i in l:
    if i % 2 != 0:   
        odd_sum += i
print("Sum of all odd items in the list is:", odd_sum)
# wap 2nd max element in a list.
l = [10, 20, 30, 40, 50]
l.sort()
print("2nd max element in the list is:", l[-2])
# wap 3rd min element in a list.
l = [10, 20, 30, 40, 50]
l.sort()
print("3rd min element in the list is:", l[2])