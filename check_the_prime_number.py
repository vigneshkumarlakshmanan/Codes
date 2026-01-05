value = int(input("Enter the value: "))

for i in range(1, value + 1):
    if i <= 1:
        print(i, "is not prime")
    else:
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                print(i, "is not prime")
                break
        else:
            print(i, "is prime")
