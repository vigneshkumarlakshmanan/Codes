#create the multiplication table for given value

value= int(input("Enter the Table number:  "))
limit = int(input("Enter the limit:  "))

limit = limit+1
for i in range(1,limit):
    print (f"{i} * {value} = {i*value}")
