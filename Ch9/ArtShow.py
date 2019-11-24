"""
ArtShow.py - This program determines if an art show attendee gets a
                5% discount for preregistering.
Input: Interactive.
Output: A statement telling the user if they get a discount or no discount.
"""

# Write discount function here.
def discount ():
    print("You are pre-registered and qualify for a 5'%' discount.")

# Write noDiscount function here.
def noDiscount():
    print("Sorry, you did not pre-register and do not qualify for a 5% discount.")
    

if __name__ == '__main__':
    registerString = input("Did you preregister? Enter Y or N: ")

    # Test input here. If Y, call discount(), else call noDiscount().
    if registerString == 'Y':
        discount()
    elif registerString == 'N':
        noDiscount()
    else:
        registerString = input("Did you preregister? Enter Y or N: ")