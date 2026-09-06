
# Problem: Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).

marks = int(input("Enter Your Marks :"))

if marks < 0 or marks > 100:
    print("Invalid Marks")

elif marks >= 90:
    print("Your Grade is A")

elif marks >= 80:
    print("Your Grade is B")

elif marks >= 70:
    print("Your Grade is C")

elif marks >= 60:
    print("Your Grade is D")

else:
    print("Your Grade is F")