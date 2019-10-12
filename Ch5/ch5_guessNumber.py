"""
GuessNumber.py - This program allows a user to guess a number
                  between 1 and 10.
Input:  User guesses numbers until they get it right.
Output: Tells users if they are right or wrong.
"""

import random

number = random.randint(1, 10)

# Prime the loop.
keepGoing = input("Do you want to guess a number? Enter Y or N ")

# Validate input.

# Enter loop if they want to play.
while keepGoing == "Y":
    # Get user's guess.
    stringNumber = input("I'm thinking of a number. .\nTry to guess by entering a number between 1 and 10 ")
    userNumber = int(stringNumber)
    # Validate input.


    # Test to see if the user guessed correctly.
    if userNumber == number:
        keepGoing = "N"
        print("You are a genius. That's correct!")
    else:
        keepGoing = input("That's not correct. Do you want to guess again? Enter Y or N ")
        # Validate input.
if keepGoing == "N":
    print("Goodbye")

#Validating User Input
# Summary
# In this lab, you will make additions to a Python program provided. The program is a guessing game. A random number between 1 and 10 is generated in the program. The user enters a number between 1 and 10, trying to guess the correct number.

# If the user guesses correctly, the program congratulates the user, and then the loop that controls guessing numbers exits; otherwise the program asks the user if he or she wants to guess again. If the user enters "Y", he or she can guess again. If the user enters "N", the loop exits. You can see that the "Y" or "N" is the sentinel value that controls the loop. Note that the entire program has been written for you.

# You need to add code that validates correct input, which is "Y" or "N" when the user is asked if he or she wants to guess a number, and a number in the range of 1 through 10 when the user is asked to guess a number.

# Instructions
# Make sure the file GuessNumber.py is selected and open.
# Write loops that validate input at all places in the code where the user is asked to provide input. Comments have been included in the code to help you identify where these loops should be written.
# Execute the program. See if you can guess the randomly generated number. Execute the program several times to see if the random number changes. Also, test the program to verify that incorrect input is handled correctly. On your best attempt, how many guesses did you have to take to guess the correct number?

