# This program takes two numbers as input and calculates their sum using a function.

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))


def add_numbers(x, y):
    return x + y

result = add_numbers(a, b)
print(f"The sum of {a} and {b} is: {result}")