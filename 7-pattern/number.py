
i=1
while i <= 5 :
    j=1
    while j <= i:
        print(i,end=" ")
        j=j+1
    print("")
    i = i+1

print("-------------")

i=6
for i in range(i):
    for j in range(i):
        print(i,end=" ")
    print("")  

'''
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 


'''
print("-------------")

i=1
while i <= 5 :
    j=1
    while j <= i:
        print(j,end=" ")
        j=j+1
    print("")
    i = i+1    
'''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

'''    
print("-------------")

i=1
while i <= 5:
    j=1
    while j <= i:
        print(j,end=" ")
        j=j+1
    print("")
    i=i+1 
i=4
while i >= 1:
    j=1
    while j <= i :   
        print(j,end=" ")
        j=j+1
    print("")
    i=i-1 

'''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1

'''
print("-------------")    
i=1
while i <= 5:
    j=5
    while j >= i:
        print(i,end=" ")
        j=j-1
    print("")
    i=i+1   

j=5
for i in range(i):
    for j in range(j):
        print(i,end=" ")
    print("")        

print("-------------")    


'''
1 1 1 1 1
2 2 2 2
3 3 3
4 4
5
0 0 0 0 0
1 1 1 1
2 2 2
3 3
4


'''
print("__________________________")
i=1
while i <= 5:
    j=5
    while j >= i:
        print(j,end=" ")
        j=j-1
    print("")
    i=i+1   


i=5
for i in range(i):
    for j in range(j):
        print(j,end=" ")
    print("") 

'''
5 4 3 2 1
5 4 3 2
5 4 3
5 4
5


0 1 2 3
0 1 2
0 1
0


'''
print("__________________________")

i=5
while i >= 1:
    j=1
    while j <= i:
        print(j,end=" ")
        j=j+1
    print("")
    i=i-1    
i=1
while i <= 5 :
    j=1
    while j <= i:
        print(j,end=" ")
        j=j+1
    print("")
    i = i+1

'''
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''
print("__________________________")

n = 5  # Number of rows
i = 1
num = 1

while i <= n:
    j = 0
    while j < i:
        print(num, end=" ")
        num += 2
        j += 1
    print()
    i += 1

n = 5  # Number of rows
num = 1

for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num += 2
    print()    

num=1
for i in range(1,6):
    for j in range(i):
        print(num,end=" ")
        num= num+2
    print("")


'''
1
3 5
7 9 11
13 15 17 19 
21 23 25 27 29 

'''
print("__________________________")
num=1
for i in range(1,6):
    for j in range(i):
        print(num,end=" ")
        num= num+1
    print("")


'''
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15

'''
print("__________________________")
i=5
for i in range(1,n+1):
    for spece in range(n-i):
         print(" ",end="")
    for a in range(1,i+1):
        print(a,end =" ")   
    print("")       
       
'''
    1
   1 2
  1 2 3
 1 2 3 4
1 2 3 4 5

'''          
