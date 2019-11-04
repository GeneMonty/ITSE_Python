#Accumulating Totals in Single-Level Control Break Programs in Python
# SuperMarket.py - This program creates a report that lists weekly hours worked 
# by employees of a supermarket. The report lists total hours for 
# each day of one week. 
# Input:  Interactive
# Output: Report. 

# Declare variables.
HEAD1 = "WEEKLY HOURS WORKED"
DAY_FOOTER = "Day Total "
SENTINEL = "done"   # Named constant for sentinel value
hoursWorked = 0     # Current record hours
hoursTotal = 0      # Hours total for a day
prevDay = ""        # Previous day of week
notDone = True      # loop control

# Print two blank lines.
print("\n\n")
# Print heading.
print("\t" + HEAD1)
# Print two blank lines.
print("\n\n")


# Read first record 
dayOfWeek = input("Enter day of week or done to quit: ")
if dayOfWeek  == SENTINEL:
    notDone = False
else:
    hoursWorked = input("Enter hours worked: ")
    prevDay = dayOfWeek
    hoursTotal += int(hoursWorked)
    print("\t" + DAY_FOOTER + str(hoursTotal))

while notDone == True:
    # Implement control break logic here
    dayOfWeek = input("Enter day of week or done to quit: ")
    if dayOfWeek  == SENTINEL:
        break
    # Include work done in the dayChange() function
    if prevDay != dayOfWeek:
        hoursTotal = 0
    hoursWorked = input("Enter hours worked: ")
    prevDay = dayOfWeek
    hoursTotal += int(hoursWorked)    
    print("\t" + DAY_FOOTER + str(hoursTotal))







# Summary
# In this lab, you will use what you have learned about accumulating totals in a single-level control break program to complete a Python program.

# The program should produce a report for a supermarket manager to help her keep track of hours worked by her part-time employees. The report should include the day of the week and the number of hours worked for each employee for each day of the week and the total hours for the day of the week.

# The student file provided for this lab includes the necessary variable declarations and input and output statements. You need to implement the code that recognizes when a control break should occur. You also need to complete the control break code. Be sure to accumulate the daily totals for all days in the week.

# Comments in the code tell you where to write your code.

# Instructions
# Study the prewritten code to understand what has already been done.
# Write the control break code
# Execute the program using the following input values:
# Monday
# 6
# Tuesday
# 2
# Tuesday
# 3
# Wednesday
# 5
# Wednesday
# 3
# Thursday
# 6
# Friday
# 3
# Friday
# 5
# Saturday
# 7
# Saturday
# 7
# Saturday
# 7
# Sunday
# 0
# done
# Here is an example of what the program output should look like:

#     WEEKLY HOURS WORKED

# Enter day of week or done to quit: Thursday
# Enter hours worked: 6
# Enter a day of week or done to quit: done
#     Day Total 6