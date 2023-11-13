'''Assume the lists numbers1 has 100 elements and numbers2 is an empty list. 
Write code that copies the values in numbers to numbers2'''

# Example list with 100 elements
numbers1 = [i for i in range(1, 101)]

# Create an empty list
numbers2 = []

# Copy values from numbers1 to numbers2
numbers2 = numbers1.copy()

# Alternatively, you can use slicing to copy the entire list
# numbers2 = numbers1[:]

# Print the copied list
print(numbers2)

