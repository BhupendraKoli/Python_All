# 6- Identity Operators    (is, is not)
a=2
b=3
c=a
# is operator checks if both the variables have the same id or not
print(a is b)  # False
print(a is  c)  # True

print(id(a))
print(id(b))
print(id(c))
# id() function returns the “identity” of the object memeroy location

#is not 
print(a is not b)  # True
print(a is not c)  # False

print(id(a))
print(id(b))
print(id(c))