#Using Multidimensional Lists

# Declare two dimensional list here
rates = [30.00,60.00,88.00,115.00,140.00],[26.00,52.00,70.00,96.00,120.00],[24.00,46.00,67.00,89.00,110.00],[22.00,40.00,60.00,75.00,88.00],[20.00,35.00,50.00,66.00,84.00]
# Declare other variables
QUIT = 99


age = 0#int(input("Enter the age of the child or 99 to quit: "))
days = 0
# Perform a priming read to get the age of the child
while age != QUIT:

    # Ask the user to enter the number of days
    days = 1#int(input("Enter the number of days: "))
    
    # Print the weekly rate
    print("Weekly rate is: ", rates[age][days-1])
    
    # Ask the user to enter the next child's age
    
    age = int(input("Enter the age of the child or 99 to quit: "))
print("End of program")






# Summary
# In this lab, you will complete a Python program that uses a two-dimensional list to store data for the Building Block Day Care Center.

# The day care center charges varying weekly rates depending on the age of the child and the number of days per week the child attends. The program should allow the user to enter the age of the child and the number of days per week the child will be at the day care center. The program should output the appropriate weekly rate.

# The file provided for this lab contains all of the necessary variable declarations, except the two-dimensional list. You need to write the input statements and the code that initializes the two-dimensional list, determines the weekly rate, and prints the weekly rate.

# Comments in the code tell you where to write your statements. Weekly rates can be found in the provided table: info> Note: Click and drag the right side of the instructions pane to view the entire table.

# Age:	1	2	3	4	5
# 0	30.00	60.00	88.00	115.00	140.00
# 1	26.00	52.00	70.00	96.00	120.00
# 2	24.00	46.00	67.00	89.00	110.00
# 3	22.00	40.00	60.00	75.00	88.00
# 4 +	20.00	35.00	50.00	66.00	84.00
# Instructions
# Declare and initialize the two-dimensional list.
# Write the Python statements that retrieve the age of the child and the number of days the child will be at the day care center.
# Determine and print the weekly rate.
# Execute the program and verify that the output is correct.