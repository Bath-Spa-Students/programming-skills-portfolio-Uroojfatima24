while True:
    age = input("Please enter your age (or 'quit' to exit): ")

    if age.lower() == 'quit':
        break

    age = int(age)

    if age < 3:
        print("Your movie ticket is free.")
    elif 3 <= age <= 12:
        print("Your movie ticket costs $10.")
    else:
        print("Your movie ticket costs $15.")

