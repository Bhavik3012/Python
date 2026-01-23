n = int(input("Enter a positive integer: "))
factorial = 1

while n != 1:
    factorial *= n
    n -= 1
print("Factorial is:", factorial)
