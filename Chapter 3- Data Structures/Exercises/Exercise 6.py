# List of invitees
people_to_invite = ["Aisha", "Suriya", "Amna"]

# Define a function to send invitations
def send_invitation(person):
    return f"Dear {person},\nYou are cordially invited to dinner at my place. Please join me on Friday at 6 PM.\nBest Regards, Urooj Fatima"

# Announce the guest who can't make it
guest_cant_make_it = "Amna"
print(f"Unfortunately, {guest_cant_make_it} can't make it to the dinner.\n")

# Replace the name of the guest who can't make it with a new person
new_guest = "Zainab"
people_to_invite[people_to_invite.index(guest_cant_make_it)] = new_guest

# Print a second set of invitation messages
def send_invitation(person):
    return f"Dear {person},\nYou are cordially invited to dinner at my place. Please join me on Friday at 6 PM.\nBest Regards, Urooj Fatima"

#Ex 6
# Print a message that you can only invite two people
print("Due to a limited dinner table, I can only invite two people for dinner.")

# Use pop() to remove extra guests and send them messages
while len(people_to_invite) > 2:
    guest = people_to_invite.pop()
    print(f"Sorry, {guest}, I can't invite you to the dinner this time due to limited tables. Sorry for the inconvenience caused.")

# Print messages to the two remaining guests
for guest in people_to_invite:
    print(f"{guest}, you're still invited to the dinner!")

# Use del to remove the last two names
del people_to_invite[:]

# Print the empty list
print("Empty invitees list:", people_to_invite)





