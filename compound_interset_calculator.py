# compound interest calculator

# A=p(1+r/n)^nt

# p - payment , r - rate of interest , n -  periods , t - time

p = float(input("Enter the principal amount: "))
r = float(input("Enter the rate of interest: "))
n = int(input("Enter the number of periods: "))
t = int(input("Enter the total number of years: "))


rate =r/100
y = (n * t)
x = (1+rate/n)

A = p * pow(x,y)

print(A)
