# 4- Logical Operators     (and , or , not)
'''
AND 
The AND operator is a logical operator that returns True if both the conditions are met. It is d
 T AND T = T
 T AND F = F
 F AND T =F
 F AND F = F

 OR 
 The OR operator is a logical operator that returns True if either of the conditions is met. It is
  T OR T = T
  F OR T = T
  T OR F = T
  F OR F = F

NOT 
The NOT operator is a logical operator that returns True if the condition is not met. It is
# T NOT T = F
# T NOT F = T
# F NOT T = T
# F NOT F = F
 not(T) = False
not(F) = True


'''
a=3
b=2
print((a>b)and (a!=b)) # true
print((a!=b) and (a<b)) #flase 
print((a>=b) and (a==b)) #flase
print((a>b) and (a>=b)) #true

a=90
b=45
print((a>b) or (a<b)) #true
print((a!=b) or (a==b)) #true
print((a<b) or (a==b)) #flase


a=12
b=20
print(not(a>b)) # not(F) = true
print(not(a!=b)) # not(T) =Flase
print(not(a<b)) # not(T) =Flase

