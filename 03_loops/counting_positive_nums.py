numbers = list(map(int, input("Enter numbers: ").split(",")))

count_positive_nums = 0

for num in numbers:
    if num > 0:
        count_positive_nums += 1

print("Positive numbers count:", count_positive_nums)


