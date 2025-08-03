# Hollow Partten 
# square pattren 


for i in range (1,6):
    for j in range (1,6):
        print("*",end=" ")
    print("")    


'''
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 
'''    

print("___________________________")
for i in range (1,6):
    for j in range (1,6):
        if j==1 or j==5 or i==1 or i==5:
            print("*",end=" ")
        else:
            print(" ",end=" " )
    print("")         

'''
* * * * *
*       *
*       *
*       *
* * * * *

'''

print("___________________________")
 
for i in range (1,6):
    for j in range (1,6):
        if j==1 or j==i or i==5:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("")


'''
*
* *
*   *
*     *
* * * * *

'''    
print("___________________________")
 

for i in range(1,6):
    for j in range(1,6):
        if  j==0 or j==i:
         print("*",end=" ")
        else:
            print(" ",end=" ") 
        
    print("")        
'''
*
  *
    *
      *
        *

'''

print("___________________________")
for i in range(1,6):
    for j in range(1,6):
        if  i==1 or j==5 or j==i:
         print("*",end=" ")
        else:
            print(" ",end=" ") 
        
    print("")   


'''
* * * * *
  *     *
    *   *
      * *
        *

'''


print("___________________________")
for i in range(1,6):
    for j in range(1,6):
        if  i==3 or j==3 :
         print("*",end=" ")
        else:
            print(" ",end=" ") 
        
    print("")  


'''
    *
    *
* * * * *
    *
    *

'''    
 
for i in range(1,6):
    for j in range(1,6):
        if  j== 6 -i :
         print("*",end=" ")
        else:
            print(" ",end=" ") 
        
    print("")  

print("___________________________")

'''
       *
      *
    *
  *       
*

'''

for i in range(1,6):
    for j in range(1,6):
        if j==i or j== 6 -i :
         print("*",end=" ")
        else:
            print(" ",end=" ") 
        
    print("")  

'''
*       *
  *   *
    *
  *   *
*       *

'''