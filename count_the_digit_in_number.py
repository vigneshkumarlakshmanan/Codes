#count the digit in given number

num = int(input("Enter a number: "))
print("The value you have entered =", num)
count =0
while num !=0:
    digit = num % 10
    remainder = num % 10 + digit
    num = num // 10
    count=count+1
print(count)

