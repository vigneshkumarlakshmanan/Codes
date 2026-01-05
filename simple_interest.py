#--simple interest

# simple interest si=pnr/100
# p - payment
# n - number of years
# r - rate of interest


p= float(input("Enter the payment amount: "))
n= float(input("Enter the number of years: "))
r= float(input("Enter the rate of interest: "))

si= (p*n*r)/100

print (f"The interest amount is {si}")
print (f"The total payment is {si+p}")


