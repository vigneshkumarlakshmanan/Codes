unit=input("Enter the unit you want to convert: ")
temp =float(input("Enter the temperature you want to convert: "))

if unit == "C":
    temp=(temp - 32)*5/9
    print (f"The temperature is: {temp}")
elif unit == "F":
    temp=temp*9/5+32
    print (f"The temperature is: {temp}")
else:
    print ("the unit is not valid")