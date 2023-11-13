# Define the list of sandwich orders with 'pastrami' appearing at least three times
sandwich_orders = ["chicken", "pastrami", "egg", "grilled cheese", "pastrami", "roast beef", "ham", "pastrami","turkey"]

# Initialize an empty list for finished sandwiches
finished_sandwiches = []

# Check if 'pastrami' is in the initial sandwich_orders
if 'pastrami' in sandwich_orders:
    print("Sorry, the deli has run out of pastrami.")

    # Remove all occurrences of 'pastrami' using a while loop
    while 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')

# Loop through the sandwich orders
while sandwich_orders:
    current_order = sandwich_orders.pop(0)  
    
    # Skip 'pastrami' sandwiches
    if current_order == 'pastrami':
        continue

    print(f"I made your {current_order} sandwich.")
    finished_sandwiches.append(current_order)

# Display the finished sandwiches
print("\nFinished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich)
