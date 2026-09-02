num = int(input("Enter any number: "))

factorial = 1

for i in range(1, num + 1):
    factorial = factorial * i

print("The Factorial of the num is  =", factorial)