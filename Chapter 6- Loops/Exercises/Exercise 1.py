toppings = []
while True:
    topping = input("Enter a pizza topping (or 'quit' to finish): ")
    if topping.lower() == 'quit':
        break
    print(f"You'll add {topping} to your pizza.")
    toppings.append(topping)

if toppings:
    print("Your pizza will have the following toppings:")
    for topping in toppings:
        print(topping)
else:
    print("You didn't choose any pizza toppings.")
