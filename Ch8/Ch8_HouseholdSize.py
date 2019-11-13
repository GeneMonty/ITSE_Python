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
    total += householdSize
    # Place value in array.
    householdSizes.append(householdSize)
    # Calculate total of household sizes

    numSizes += 1  # We have one more house
    householdSizeString = input("Enter household size or 999 to quit: ")
    householdSize = int(householdSizeString)

# Find the mean (list values + list / number of items)
mean = total / numSizes

# This is the work done in the sortArray() function
for i in range(numSizes):
    for i in range(numSizes-1):
        if householdSizes[i] > householdSizes[i+1]:
            temp = householdSizes[i]
            householdSizes [i] = householdSizes [i+1]
            householdSizes[i+1]= temp
            
# This is the work done in the displayArray() function
for item in householdSizes:
    print(item)
# Find the median
if numSizes % 2 == 0:
    index1 = int(numSizes/2)-1
    index2 = int(numSizes/2)
    median = int((householdSizes[index1]+householdSizes[index2])/2)
if numSizes % 2 != 0:
    median = householdSizes[int(numSizes/2)]
print("The mean is: ", mean)
print("The median is: ", median)












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