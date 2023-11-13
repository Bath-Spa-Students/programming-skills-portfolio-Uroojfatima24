'''Write a python program with if statement that assigns 20 to the variable y and assigns 40 to the 
variable z if the variable & is greater than 100.'''

# Assume variable & is defined somewhere in your code
# & = ampersand
ampersand = 120

# Check if & is greater than 100
if ampersand > 100:
    y = 20
    z = 40
    print("Variables y and z have been assigned values because & is greater than 100.")
else:
    print("No assignment made because & is not greater than 100.")

# Print the values of y and z (whether assigned or not)
print("Value of y:", y)
print("Value of z:", z)
