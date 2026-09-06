 # Problem: Movie tickets are priced based on age: $12 for adults (18 and over),  $8 for children. Everyone gets a $2 discount on Wednesday.

age = int(input("Enter your Age : "))

price = 8 if age < 18 else 12

day = input("Enter the day of the week : ").strip().lower().replace(" ", "")
if  day == "wednesday":
    price -= 2
print(f"Your ticket price is ${price}.")