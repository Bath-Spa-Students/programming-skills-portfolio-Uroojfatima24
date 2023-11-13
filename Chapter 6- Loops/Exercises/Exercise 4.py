# Create a list of sandwich orders
sandwich_orders = ["chicken", "egg", "grilled cheese", "roast beef", "ham" , "turkey"]

# Create an empty list for finished sandwiches
finished_sandwiches = []

# Loop through each sandwich order
while sandwich_orders:
    current_order = sandwich_orders.pop(0)  # Get the first order from the list
    print(f"I made your {current_order} sandwich.")
    finished_sandwiches.append(current_order)  # Move the finished sandwich to the list

# Print a message listing each finished sandwich
print("\nList of finished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)
