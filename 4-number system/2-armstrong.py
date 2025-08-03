# armstrong number

'''
153
1^3 + 5^3 + 3^3 = 153
 total number of digits=3
 1**3 + 5**3 + 3**3 =153
 the sum of the dititd each ret to the power of the total number of it digits equla to the digits


'''
num = int(input("Enter a number: "))
# Count the number of digits
power = len(str(num))
# Calculate the sum of each digit raised to the power
total = sum(int(digit) ** power for digit in str(num))
# Check if the sum equals the original number
if total == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")

# num=int(input("entr the number"))

# temp=num
# s=0
# power=len(str(num))
# while temp !=0:
#     digit=temp%10
#     s=s+digit**power
#     temp=temp//10   
# if s==num:
#     print(num,"is an armstrong number")
# else:   
#   print(num,"is not an armstrong number")

start=int(input("enter the number "))
end=int(input("enter the number "))

while start<=end:
    temp=start 
    s=0
    power=len(str(start))
    while temp!=0:
        digit=temp%10
        s += digit ** power
        temp=temp//10
    if s == start:
      print(start,end=" ")
    start=start+1     


start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
while start <= end:
    temp = start
    s = 0
    power = len(str(start))
    while temp != 0:
        digit = temp % 10
        s += digit ** power
        temp = temp // 10
    if s == start:
        print(start, end=" ")
    start += 1
