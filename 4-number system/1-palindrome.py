# Palindroma number 
# is a number that looks same after the revers it 

num=int(input("enter the number "))
temp=num
rev=0
while temp !=0:
    rem=temp%10
    rev=rev*10+rem
    temp=temp//10
if num==rev:
    print(num,"is a palindrome number")
else:
   print(num,"is not a palindrome number")



# using slicing method 
num = int(input("Enter a number: "))
# Reverse the number
rev = int(str(num)[::-1])
print(rev)
# Check if the number is equal to its reverse
if num == rev:
    print(f"{num} is a palindrome number.")
else:
    print(f"{num} is not a palindrome number.")


# WAP to print that palindrom number who's sum is greater then 9
# input: 545
# output: this is palindrom number who's sum is greater then 9
# 
# WAP to print that palindrom number who's sum is greater then 9
# input: 123
# output: this is not palindrom number who's sum is greater then 9
# num=int(input("enter the number "))
# temp=num
# rev=0
# while temp !=0:
#     rem=temp%10
#     rev=rev*10+rem
#     temp=temp//10
#     if num==rev:
#         sum=0   
#         while num !=0:
#             rem=num%10
#             sum=sum+rem
#             num=num//10
#             if sum>9:
#                 print(num,"is a palindrom number who's sum is greater then 9")
#             else:
#                 print(num,"is not a palindrom number who's sum is greater then 9")

# Input number
num = int(input("Enter a number: "))

# Store original number for comparison
original = num
reverse = 0
digit_sum = 0
while num != 0:
    digit = num % 10 # last didit 
    reverse = reverse * 10 + digit #revers logic 
    digit_sum += digit
    num //= 10
if original == reverse and digit_sum > 9:
    print("This is palindrome number whose sum is greater than 9")
elif original == reverse:
    print("This is palindrome number but sum is not greater than 9")
else:
    print("This is not a palindrome number")



# well all see palindron number within specific range 
start=int(input("enter the number "))
end=int(input("enter the number "))
while start<=end:
    temp=start 
    rev=0
    while temp!=0:
        digit=temp%10
        rev=rev*10+digit
        temp=temp//10
    if rev==start:
        print(start,end=" ")
    start=start+1    