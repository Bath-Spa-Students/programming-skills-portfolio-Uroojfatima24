# List of invitees
people_to_invite = ["Aisha", "Suriya", "Amna"]

# Define a function to send invitations
def send_invitation(person):
    return f"Dear {person},\nYou are cordially invited to dinner at my place. Please join me on Friday at 6 PM.\nBest Regards, Urooj Fatima"

# Loop through the list and send invitations
for person in people_to_invite:
    invitation = send_invitation(person)
    print(invitation)
    print("\n")



