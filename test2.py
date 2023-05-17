def swapcase():
    first = int(input("Enter first number: "))
    second = int(input("Enter second number: "))
    temp = first
    first = second
    second = temp
    print(first, second)
swapcase()
print(swapcase())