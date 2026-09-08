# Program to find the first non-repeated character in a string.
string = input("Enter a string: ")

for char in string:
    if string.count(char) == 1:
        print("First non-repeated character:", char)
        break
else:
    print("No non-repeated character found.")