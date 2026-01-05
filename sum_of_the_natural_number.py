# print hte sum of the natural numbers
n = int(input("Enter the number:  "))
sum=0
for i in range(0,n):
    sum = sum + i
    if (i == n-1):
       print(sum)