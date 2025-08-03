# set 
'''
set is a collection of hetrogeneous data 
set is a collection of unique data 

set is unordered collection of unique elements
set in un index 
set is mutable
dose not allow duplicats 
set is create using curely brackets or the set() function 


'''
# # set creation
# s = {1, 2, 3, 4, 5,"jay "}
# print(s)
# print(type(s))

# # remove all duplicats without using loop
# s = [1, 2, 3, 4, 5,"jay ",1,2]
# s = list(set(s))
# res=set(s)
# print(res)
# print(s)


# # mutable 
# s=set()
# print(s)

# s.add(5)
# s.add(4)
# s.add(3)
# s.add(2)

# print(s)
# # remove element from set remove used to remove the element of specified values
   
# s.remove(2)
# print(s)

# # discard
# # discard is used to remove the element of specified values if it is present in the set if not
# # it will not raise any error
# s={1,2,3,4,5,6}
# s.discard(33)
# print(s)


# # s={1,2,3,4,5,6}
# # s.remove(33)
# # print(s)

# # pop methode
# # pop is used to remove the element from the set
# # it will remove the first element from the un ordered  set
# s={1,2,3,4,5,6}
# print (s)
# s.pop()
# print(s)

# # clear()
# # clear() is used to remove all the elements from the set
# #structure will remains there 
# s={1,2,3,4,5,6}
# print(s)
# s.clear()
# print(s)

# # del ()
# # del() is used to remove the set itsel prementaly 
# # s={1,2,3,4,5,6}
# # del s
# # print(s)

# # difference 
# # difference is used to return a new set with elements which are in the set but not in other
# # it will return un comman element form set1
# s1={1,2,3,4,5,6,7}
# s2={5,6,7,8}
# s=s1.difference(s2)
# print(s)

# # difference_update
# # difference_update is used to remove the element from the set which are in other set
# # it will remove the common element from set1
# #3 it will update the se1 with uique element of set1
# s1={1,2,35,4,5,6,7}
# s2={5,6,7}
# s1.difference_update(s2)
# print(s1)

# # symmetric diffrence 
# # symmetric diffrence is used to return a new set with element which are in set1 or set
# # it will return all the element of set1 and set2
# s1={1,2,3,4,5,6,7}
# s2={5,6,7,8}
# s=s1.symmetric_difference(s2)
# print(s) #{1, 2, 3, 4, 8}

# #  symmetric diffrence update
# # symmetric diffrence update is used to remove the element from the set which are in set1 or
# # it will remove the common element from set1 and set2
# # it will give the un comman element form the both set and update it set1 

# s1={1,2,3,4}
# s2={5,6,1,2}
# s1.symmetric_difference_update(s2)
# print(s1)

# # intersection 
# # intersection is used to return a new set with element which are in set1 and set2
# # it will return the common element from set1 and set2
# s1={1,2,3,4,5,6,7}
# s2={5,6,7,8}
# s=s1.intersection(s2)
# print(s)
# # intersection_update
# # intersection_update is used to remove the element from the set which are in set1 and set2
# # it will remove the common element from set1 and set2
# # it will update the set1 with common element of set1 and set2
# s1={1,2,3,4,5,6,7,8}
# s2={5,6,7,8}
# s1.intersection_update(s2)
# print(s1)


# # isdisjoint()
# # isdisjoint() is used to check if two sets are disjoint or not
# # disjoint means that there is no common element in both sets
# # its give the boolen value only true and flase 
# # if the no comman valeu in set1 and set2 they return True 
# # if the comman value in set1 and set2 they return False
# s1={1,2,3,4,5,6,7}
# s2={8,9,10}
# print(s1.isdisjoint(s2))

# # issubset 
# # subset means that all element of set1 are present in set2
# # its give the boolen value only true and flase
# # if all element of set1 are present in set2 they return True
# # if all element of set1 are not present in set2 they return False
# s1={1,2,3,4,5,6,7,10}
# s2={1,2,3,4,5,6,7,8,9}
# print(s1.issubset(s2))

# s1={1,2,3,4}
# s2={1,2,3,4,5,6,7,8,9}
# print(s1.issubset(s2))

# # superset
# # superset means that all element of set2 are present in set1
# # its give the boolen value only true and flase
# # if all element of set2 are present in set1 they return True
# # if all element of set2 are not present in set1 they return False
# s1={1,2,3,4,5,6,7,8,9}
# s2={1,2,3,4}
# print(s1.issuperset(s2))


# # update 
# # update is used to add the element from set2 to set1
# # it will add the element from set2 to set1
# # addition of sets
# s1={1,2,3,4,5,6,7,8,9,15}
# s2={10,11,12,13,14,15,16,17,18}
# s1.update(s2)
# print(s1)

# s={1,2,3,5}
# s.update((1,2,3,4,5,6,7,8,9))
# print(s)
# # union
# # union is used to add the element from set2 to set1
# # it will add the element from set2 to set1
# # addition of sets exclude the duplicats 
# s1={1,2,3,4,5,6,7,8,9}
# s2={10,11,12,13,14,15,16,17,18}
# s=s1.union(s2)
# print(s)



# 1.Create a set with the elements {2, 4, 6, 8, 10} and add the number 12 to it.
set1={2,4,6,8,10}
set1.add(12)
print(set1)

# 2.Remove the number 4 from a set {1, 2, 3, 4, 5} using an appropriate method.
set2= {1, 2, 3, 4, 5}
set2.remove(4)
print(set2)
# 3.Remove the number 5 from a set{1,2,3} using remove method, observe output.
# How is it different from discard()?
set3={1,2,3}
# set3.remove(5)
set3.discard(5)


# 4.Check whether the number 7 is present in the set {3, 5, 7, 9}.
set3={3,5,7,9}
print(7 in set3)


# 5.Find the union of two sets: {1, 3, 5} and {2, 4, 6}.
set4={1,3,5}
set5={2,4,6}
print(set4.union(set5))
# 6.Find the intersection of {1, 2, 3, 4} and {3, 4, 5, 6}.
se1={1,2,3,4}
se2={3,4,5,6}
print(se1.intersection(se2))

# 7.Find the difference of {10, 20, 30, 40} and {30, 40, 50, 60}.
set1={10,20,30,40}
se2={30,40,50,60}
s=set1.difference(se2)
print(s)
# 8.Find the symmetric difference between {"a", "b", "g"} and {"b", "c", "d"}.
s={"a", "b", "g"}
b={"b", "c", "d"}
a=s.symmetric_difference(b)
print(a)
# 9.Given a list [10, 20, 20, 30, 40, 40, 40, 50], remove duplicates using a set.
list1=[10, 20, 20, 30, 40, 40, 40, 50]
print(set(list1))
# 10.Given set1 = {1, 2, 3} and set2 = {1, 2, 3, 4, 5}, check if set1 is a subset of set2.
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
print(set1.issubset(set2))
# 11.Given setA = {5, 10, 15} and setB = {10, 20, 30}, update setA with elements from setB.
setA = {5, 10, 15}
setB = {10, 20, 30}
setA.update(setB)
print(setA)

# 12.Find the length of a set {10, 20, 30, 40, 50}. and Clear all elements from a set.
set1 = {10, 20, 30, 40, 50}
print(len(set1))

