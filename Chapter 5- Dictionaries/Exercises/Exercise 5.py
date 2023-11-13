# List of dictionaries representing pets
pets = [
    {'kind': 'Turtle', 'owner': 'Millie'},
    {'kind': 'Cat', 'owner': 'Noah'},
    {'kind': 'Rabbit', 'owner': 'Finn'},
    {'kind': 'Dog', 'owner': 'Caleb'},
    {'kind': 'Horse', 'owner': 'Sadie'}
]

# Loop through the list and print information about each pet
for pet in pets:
    print(f"Kind of Animal: {pet['kind']}")
    print(f"Owner's Name: {pet['owner']}")
    print()  
