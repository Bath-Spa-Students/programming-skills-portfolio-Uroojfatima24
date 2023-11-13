# Create a list of sandwich orders
sandwich_orders = ['chicken', 'egg', 'grilled cheese', 'ham', 'turkey', 'roast beef']

# Create an empty list for finished sandwiches
finished_sandwiches = []

# Loop through the sandwich orders
for order in sandwich_orders:
    # Display a message for each order
    print(f"I made your {order} sandwich.")
    
    # Move the sandwich to the list of finished sandwiches
    finished_sandwiches.append(order)

# Print a message listing each finished sandwich
print("\nList of finished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)
