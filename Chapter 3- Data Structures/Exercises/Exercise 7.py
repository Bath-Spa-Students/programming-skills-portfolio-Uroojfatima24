# Store the locations in a list (not in alphabetical order)
places_to_visit = ["North Carolina", "Yokohama", "Islamabad", "Vancouver"]

# Print the list in its original order
print("Original list:", places_to_visit)

# Use sorted() to print the list in alphabetical order without modifying the original list
print("Sorted in alphabetical order:", sorted(places_to_visit))

# Show that the original list is still in its original order
print("Original list is still:", places_to_visit)

# Use sorted() to print the list in reverse alphabetical order without changing the original order
print("Sorted in reverse alphabetical order:", sorted(places_to_visit, reverse=True))

# Show that the original list is still in its original order
print("Original list is still:", places_to_visit)

# Use reverse() to change the order of your list
places_to_visit.reverse()
print("Reversed list:", places_to_visit)

# Use reverse() again to change the order back to its original state
places_to_visit.reverse()
print("Reversed list back to original order:", places_to_visit)

# Use sort() to change the list to alphabetical order
places_to_visit.sort()
print("Sorted in alphabetical order with sort():", places_to_visit)

# Use sort() to change the list to reverse alphabetical order
places_to_visit.sort(reverse=True)
print("Sorted in reverse alphabetical order with sort():", places_to_visit)
