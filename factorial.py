# print the given number factorial
#n! = n * (n-1)!
n = int(input("Enter the number:  "))
n= n+1
sum=1
for i in range(1,n):
    sum = sum * i
    if (i == n-1):
       print(sum)