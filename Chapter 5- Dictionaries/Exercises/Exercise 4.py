rivers = {
    'Mississippi': 'United States',
    'Amazon': 'Brazil',
    'Indus': 'Pakistan'
}

# Print a sentence about each river
for river, country in rivers.items():
    print(f"The {river} runs through {country}.")

# Print the name of each river
print("\nRivers:")
for river in rivers.keys():
    print(river)

# Print the name of each country
print("\nCountries:")
for country in rivers.values():
    print(country)
