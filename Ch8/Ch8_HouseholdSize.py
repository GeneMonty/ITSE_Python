"""
HouseholdSize.py - This program uses a bubble sort to arrange household sizes
                    in descending order and then prints the mean and median
                    household size.
Input:  Interactive.
Output:  Mean and median household size.
"""

# Initialize variables.
householdSizes = []  # Array used to store household sizes.
numSizes = 0
total = 0.0
mean = 0.0
median = 0.0

# Input household size
householdSizeString = input("Enter household size or 999 to quit: ")
householdSize = int(householdSizeString)
# This is the work done in the fillArray() function
while (householdSize != 999):
    # Place value in array.
    householdSizes.append(householdSize)
    # Calculate total of household sizes

    numSizes += 1  # We have one more house
    householdSizeString = input("Enter household size or 999 to quit: ")
    householdSize = int(householdSizeString)

# Find the mean

# This is the work done in the sortArray() function

# This is the work done in the displayArray() function

# Find the median


#Using a Bubble Sort in Python
# Summary
# In this lab, you will complete a Python program that uses a list to store data for the village of Marengo.

# The village of Marengo conducted a census and collected records that contain household data, including the number of occupants in each household. The exact number of household records has not yet been determined, but you know that Marengo has fewer than 300 households.

# The program is described in Chapter 8, Exercise 5, in Programming Logic and Design. The program should allow the user to enter each household size and determine the mean and median household size in Marengo. The program should output the mean and median household size in Marengo. The file provided for this lab contains the necessary variable declarations and input statements. You need to write the code that sorts the household sizes in ascending order using a bubble sort, and then prints the mean and median household size in Marengo. Comments in the code tell you where to write your statements.

# Instructions
# Make sure that the file HouseholdSize.py is selected and open.
# Write the bubble sort.
# Calculate the total of the household size.
# Output the mean and median household size in Marengo.
# Execute the program by clicking the Run button and the bottom of the screen.
# Enter the following input, and ensure the output is correct. Household sizes: 4, 1, 2, 4, 3, 3, 2, 2, 2, 4, 5, 6 followed by 999 to exit the program.