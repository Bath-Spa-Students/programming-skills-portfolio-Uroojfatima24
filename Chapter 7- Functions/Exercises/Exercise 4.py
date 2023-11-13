def make_shirt(size="Large", message="I love Python"):
    #Prints a message about the size and message printed on a shirt.
    print(f"A {size} shirt will be printed with the message: {message}")

# Make a large shirt with the default message
make_shirt()

# Make a medium shirt with the default message
make_shirt(size="Medium")

# Make a custom-sized shirt with a different message
make_shirt(size="Small", message="Python is really fun.")
