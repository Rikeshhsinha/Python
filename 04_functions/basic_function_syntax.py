# This program calculates the square of a given number using a function.
num = int(input("Enter a number to calculate its square: "))


def square_of_num():
    return num * num

result = square_of_num()
print(f"The square of {num} is: {result}")
