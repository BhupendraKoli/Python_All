# fibonacci sequence 

'''
its start with 0 and 1
first two number is  0 and 1
thw next ine is addition of previoues 2 number 
# will create the sequence of fibonacci of 5

'''
n = int(input("Enter the number of terms: "))
a, b = 0, 1
print("Fibonacci sequence:")
for _ in range(n):
    print(a, end=" \n")
    a, b = b, a + b


num=7
num1=0
num2=1
s=1
print(num1,num2,end=" ")
count=2
while  count<num:
    num3=num1+num2
    print(num3,end=" ")
    s=s+num3
    num1=num2
    num2=num3
    count+=1
print("the sum is ",s)    