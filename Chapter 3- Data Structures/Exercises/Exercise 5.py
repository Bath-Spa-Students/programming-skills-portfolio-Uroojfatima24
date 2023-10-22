# Initial list of invitees
people_to_invite = ["Aisha", "Suriya", "Amna"]

# Announce the guest who can't make it
guest_cant_make_it = "Amna"
print(f"Unfortunately, {guest_cant_make_it} can't make it to the dinner.\n")

# Replace the name of the guest who can't make it with a new person
new_guest = "Zainab"
people_to_invite[people_to_invite.index(guest_cant_make_it)] = new_guest

# Print a second set of invitation messages
def send_invitation(person):
    return f"Dear {person},\nYou are cordially invited to dinner at my place. Please join me on Friday at 6 PM.\nBest Regards, Urooj Fatima"

for person in people_to_invite:
    invitation = send_invitation(person)
    print(invitation)
    print("\n")
