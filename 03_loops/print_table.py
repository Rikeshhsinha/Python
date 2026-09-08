# Program to print multiplication table of a number but skip the 5th iteration.

num = int(input("Enter a number: "))

for i in range(1, 11):
    if i == 5:
        continue
    print(f"{num} x {i} = {num * i}")