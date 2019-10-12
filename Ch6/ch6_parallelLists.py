# JumpinJava.py - This program looks up and prints the names and prices of coffee orders.  
# Input:  Interactive
# Output:  Name and price of coffee orders or error message if add-in is not found 

# Declare variables.
NUM_ITEMS = 5 # Named constant

# Initialized list of add-ins
addIns = ["Cream", "Cinnamon", "Chocolate", "Amaretto", "Whiskey"]

# Initialized list of add-in prices
addInPrices = [.89, .25, .59, 1.50, 1.75]
foundIt = False # Flag variable
orderTotal = 2.00  # All orders start with a 2.00 charge
    
# Get user input
addIn = input("Enter coffee add-in or XXX to quit: ")

# Write the rest of the program here.


    
# Summary
#         In this lab, you use what you have learned about parallel lists to complete a partially completed Python program.

#         The program should either print the name and price for a coffee add-in from the Jumpin’ Jive Coffee Shop or it should print the message "Sorry, we do not carry that.".

#         Read the problem description carefully before you begin. The data file provided for this lab includes the necessary input statements. You need to write the part of the program that searches for the name of the coffee add-in(s) and either prints the name and price of the add-in or prints the error message if the add-in is not found. Comments in the code tell you where to write your statements.

# Instructions
#         Study the prewritten code to make sure you understand it.
#         Write the code that searches the list for the name of the add-in ordered by the customer.
#         Write the code that prints the name and price of the add-in or the error message, and then write the code that prints the cost of the total order.
# Execute the program using the following data and verify that the output is correct:
#         Cream
#         Caramel
#         Whiskey
#         chocolate
#         Chocolate
#         Cinnamon
#         Vanilla