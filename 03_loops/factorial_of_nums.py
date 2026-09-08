# This program calculates the factorial of a given number using a for loop.
nums = int(input("Enter a number to calculate its factorial: "))
factorial = 1

for i in range(1, nums + 1):
    factorial *= i

print(f"The factorial of {nums} is: {factorial}")