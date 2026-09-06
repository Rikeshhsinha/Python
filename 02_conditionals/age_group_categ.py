age = int(input("Enter your age: "))

if age < 13 and age >= 0:
    print("You are a child.")   
elif age < 19:
    print("You are a teenager.")            
elif age <= 59:
    print("You are an adult.")
elif age >= 60:
    print("You are a senior citizen.")  
else:
    print("Invalid age entered.")