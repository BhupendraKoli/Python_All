# harshad number 
# a number is which divisible by sum of its digits 


num = int(input("Enter a number: "))

# Calculate sum of digits
sum_of_digits = sum(int(digit) for digit in str(num))

# Check divisibility
if num % sum_of_digits == 0:
    print(f"{num} is a Harshad number.")
else:
    print(f"{num} is not a Harshad number.")





num=int(input("Enter the number"))
sum=0
temp=num
while temp !=0:
    digit=temp % 10
    sum=sum+digit
    temp=temp//10
if num % sum==0:
    print(num,"is a harshad number")
else:
   print(num,"is not a harshad number")