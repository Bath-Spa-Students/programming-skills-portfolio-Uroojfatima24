'''Write a python program that takes an input 5 from user and then type cast those values to string, int 
and float in the separate variables. Print all the variables.'''

# Take input from the user
user_input = input("Enter a number: ")

# Typecast the input to string, int, and float
input_as_string = str(user_input)
input_as_int = int(user_input)
input_as_float = float(user_input)

# Print the variables
print("string:", input_as_string)
print("int:", input_as_int)
print("float:", input_as_float)
