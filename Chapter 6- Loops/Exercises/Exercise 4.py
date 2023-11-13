sandwich_orders = ['chicken','egg','grilled cheese','roast beef','ham','turkey']
finished_sandwiches = []

print("Sandwich Orders:") 
for sandwich in sandwich_orders:
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

print("\nFinished Sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)


# Define the list of sandwich orders
sandwich_orders = ["turkey", "ham and cheese", "vegetarian", "tuna", "chicken"]

# Initialize an empty list for finished sandwiches
finished_sandwiches = []

# Loop through the sandwich orders
while sandwich_orders:
    current_order = sandwich_orders.pop(0)  # Take the first sandwich order
    print(f"I made your {current_order} sandwich.")
    finished_sandwiches.append(current_order)

# Display the finished sandwiches
print("\nFinished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)
