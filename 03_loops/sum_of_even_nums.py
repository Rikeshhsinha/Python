# sum of even positive numbers 
numbers = list(map(int, input("Enter numbers: ").split(",")))

sum_even_nums = 0

for num in numbers:
    if num % 2 == 0 and num > 0:
        sum_even_nums += num

print("Sum of even positive numbers:", sum_even_nums)        