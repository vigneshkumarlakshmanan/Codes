# sum of the digits

num = int(input("Enter a number: "))
print("The value you have entered =", num)
sum=0
while num !=0:
    digit = num % 10
    remainder = num % 10 + digit
    num = num // 10
    sum = sum+digit
print(sum)