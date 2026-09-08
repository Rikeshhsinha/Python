# Program to reverse a string using a for loop

name = input("Enter a string: ")

reversed_string = ""

for char in name:
    reversed_string = char + reversed_string
    

print("Reversed string:", reversed_string)