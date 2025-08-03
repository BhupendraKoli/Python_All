# AlPHABET PATTREN 
 # ASCII value 
'''
(65 to 90 ) upper case english alphabet (A to Z)

( 97 to 122) lower case english alphabet (a to z)

( 91 to 96) numbric (0 to 9)

'''
# in python there is inbuilt function chr()
# it will connvert number to char 

print(chr(65))
'''
A
'''

for i in range(65,70):
    print(chr(i),end=" ")

'''
A B C D E
'''
for i in range(65,70):
    print(i,":",chr(i))

'''
65 : A
66 : B
67 : C
68 : D
69 : E

'''    

print("__________________________")
for i in range(65,70):
    for j in range (65,i+1):
        print(chr(j),end=" ")
    print("")    

'''
A
A B
A B C
A B C D
A B C D E

'''


print("__________________________")

for i in range(5,0,-1):
    for j in range(i):
        print (chr(65+j),end=" ")
    print("")    

'''
A B C D E
A B C D
A B C
A B
A

'''
print("__________________________")
for i in range(65,70):
    for j in range (65,i+1):
        print(chr(i),end=" ")
    print("")    

'''
A
B B
C C C
D D D D
E E E E E

'''
print("__________________________")
for i in range(65,69):
    for j in range (65,69):
        print(chr(i),end=" ")
    print("") 

'''
A A A A
B B B B
C C C C
D D D D
'''    

print("__________________________")
for i in range(65,69):
    for j in range (65,69):
        print(chr(j),end=" ")
    print("") 

'''
A B C D
A B C D
A B C D
A B C D


'''
print("__________________________")
n=65
for i in range(1,5):
    for j in range (i):
        print(chr(n),end=" ")
        n=n+1
    print("")    

'''
A
B C
D E F
G H I J

'''
print("__________________________")

for i in range(7,0,-1):
    for j in range(71, 71 - i, -1):
        print (chr(j),end=" ")
    print("")      

'''
G F E D C B A
G F E D C B
G F E D C
G F E D
G F E
G F
G

'''

print("__________________________")

for i in range(5):                    # Controls number of lines
    ch = chr(69 - i)                  # 69 = 'E', 68 = 'D', etc.
    for j in range(i + 1):            # Controls repetition per line
        print(ch, end=" ")             # Print character without newline
    print() 

'''
E
D D
C C C
B B B B
A A A A A

'''
print("__________________________")
k=97

for i in range(5):
    for j in range(i+1):
        if (k-97) % 2== 0:
            print (chr(k),end=" ")
        else:
            print(chr(k).upper(),end=" ")
        k=k+1
    print("")        
'''
a
B c
D e F
g H i J
k L m N o


'''
print("__________________________")