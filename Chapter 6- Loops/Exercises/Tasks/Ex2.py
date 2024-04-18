while True:
    age = int(input("Enter your age: "))

    if age < 3:
        print(" Great! Your ticket is free")
    elif 3 <= age <= 12:
        print("Your ticket costs $10.")
    elif age > 12:
        print("Damm! Your ticket costs $15.")
    else:
        print("Invalid age. Please enter a valid age.")