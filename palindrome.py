# Given number is palindrome or not

num = int(input("Enter a number: "))
val= num
reverse = 0
while num != 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
print("Reversed number =", reverse)
if reverse == val:
    print("The given number is palindrome")
else:
    print("The given number is not palindrome")