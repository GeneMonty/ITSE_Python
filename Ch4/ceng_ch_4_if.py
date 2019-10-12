"""
HouseSign.py - This program calculates prices for custom house signs.
"""

# Declare and initialize variables here.
    # Charge for this sign.
    # Number of characters.
    # Color of characters.
    # Type of wood.

charge = 35.0
numChars = 8
color = "gold"
woodType ="oak"

# Write assignment and if statements here as appropriate.

# numChars = int(input("Enter number of Characters: \n>"))
# color = input("Input Color: \n>")
# woodType = input("Enter Wood Type: \n>") 

if numChars > 5:
    charge = charge + (numChars - 5) * 4

    
if color == "gold":
    charge = charge + 15.00


if woodType == "oak":
    charge = charge + 20

# Output Charge for this sign.
print("The charge for this sign is $" + str(charge))
