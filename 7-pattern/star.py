# star pattren 
'''
* * * * * *
* * * * * *
* * * * * *
* * * * * *
* * * * * *

i=5
j=6

'''
i=1
while i <= 5:
    print("*",end=" ")
    j=1
    while j <= 5:
        print("*", end=" ")
        j=j+1
    print("")
    i=i+1

'''
* * * * * * 
* * * * * * 
* * * * * * 
* * * * * * 
* * * * * *
'''

print("---------------")


i=1
while i <= 5:
    j=1
    while j <= 5:
        print("*",end=" ")
        j=j+1
    print("")
    i=i+1

'''
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 

'''
print("-------------")
i=5
for a in range(i):
    for j in range(i):
        print("*",end=" ")
    print("")    


print("-------------")

# trangle pattern 
# left incresing traingle 
'''
*
* *
* * *
* * * *
* * * * *
'''
i=1
while i <= 5 :
    j=1
    while j <= i:
        print("*",end=" ")
        j=j+1
    print("")
    i = i+1

print("-------------")

'''
*
* *
* * *
* * * *
* * * * *
'''
# 
i=6
for i in range(i):
    for j in range(i):
        print("*",end=" ")
    print("")    

print("-------------")

# left descring traingle 
i=1
while i <= 5:
    j=5
    while j >= i:
        print("*",end=" ")
        j=j-1
    print("")
    i=i+1    

print("-------------")

j=5
for i in range(i):
    for j in range(j):
        print("*",end=" ")
    print("")        

print("-------------")

'''
* * * * *
* * * *
* * *
* *
*

'''
# right incresing pattren 

i=1
while i <= 5:
    j=5
    while j >= i:
        print(" ",end=" ")
        j=j-1 
    k=1
    while k <= i:
        print("*",end=" ")
        k=k+1
    print("")
    i=i+1    

'''
          *
        * *
      * * *
    * * * *
  * * * * *

'''
print("-------------")
rows = 5
for i in range(1, rows + 1):
    # Print spaces
    for j in range(rows - i):
        print(" ", end=" ")

    # Print stars
    for k in range(i):
        print("*", end=" ")

    print()  # Move to next line

'''
          *
        * *
      * * *
    * * * *
  * * * * *

'''
print("-------------")


i=1
while i <= 5:
    j=1
    while j <= i:
        print("*",end=" ")
        j=j+1
    print("")
    i=i+1 
i=4
while i >= 1:
    j=1
    while j <= i :   
        print("*",end=" ")
        j=j+1
    print("")
    i=i-1 

'''
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
'''
print("-------------")

i=1
while i <= 5:
    j=5
    while j >= i:
        print(" ",end=" ")
        j=j-1 
    k=1
    while k <= i:
        print("*  ",end=" ")
        k=k+1
    print("")
    i=i+1

'''
          *
        *   *
      *   *   *
    *   *   *   *
  *   *   *   *   *

'''

print("-------------")


rows = 7
for i in range(1, rows + 1,2):
    for j in range(rows - i):
        print(" ", end=" ")
    for k in range(i):
        print("*  ", end=" ")

    print()

print("-------------")

for i in range(1,5):
    for j in range(1,8):
        if (j>=5-i and j<=3+i):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("")            

print("-------------")

'''
            *
        *   *   *
    *   *   *   *   *
*   *   *   *   *   *   *


      *
    * * *
  * * * * *
* * * * * * *

'''

for i in range(1,5):
    for j in range(1,8):
        if (j>=i and j<=8-i):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("")            


print("-------------")
'''
inverted piryamid

* * * * * * *
  * * * * *
    * * *
      *
'''

n = 4  # This controls the size (half height) of the diamond

# Upper half of the diamond
for i in range(n):
    print("  " * (n - i - 1) + "* " * (2 * i + 1))

# Lower half of the diamond
for i in range(n - 2, -1, -1):
    print("  " * (n - i - 1) + "* " * (2 * i + 1))


print("-------------")    


for i in range(1,5):
    for j in range(1,8):
        if (j>=5-i and j<=3+i):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("")    
for i in range(1,5):
    for j in range(1,7):
        if (j>=i+1 and j<=7-i):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("")            

