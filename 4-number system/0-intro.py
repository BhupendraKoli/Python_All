# Number system
# # how to fetch digit from a number or hoe to break a number 
#  
num=123
while num!=0:
    digit=num%10 #3
    print(digit)
    num=num//10  # revemove last digit 
    '''
num      condition      print      updated 
123        3              3            123//10=12
12         2               2            12//10
1          1               1            1//10=0
0          0               0            0//10=0



    '''

# num=123
# while num!=0:
#     digit=num%10 #3
#     print(digit)
#     num=num//10  # remove the last disit and procseed the imtretation

# # wriye a program to sum of the digits of a given number 
# num=123
# sum=0
# while num!=0:
#     digit=num%10 #3
#     sum=sum+digit
#     num=num//10  # remove the last digit and proceed the iteration
#     print(sum)  # 6

# how to print reverse number 
num=123
num1=0
while num!=0:
    digit=num%10 #3
    num1=num1*10+digit # 3*10+2=32
    num=num//10  # remove the last digit and proceed the iteration
print(num1) #321

