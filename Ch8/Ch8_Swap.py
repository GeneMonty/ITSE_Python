#Swapping Values in Python

# Swap.py - This program determines the minimum and maximum of three values input by 
# the user and performs necessary swaps.  
# Input: Three int values. 
# Output: The numbers in numerical order.

first = 0
second = 0
third = 0

# Get user input
first = -88#int(input("Enter first number: "))
second = 30#int(input("Enter second number: "))
third = -23#int(input("Enter third number: "))

# Test to see if the first number is greater than the second number
if first > second :
        temp = first
        first = second
        second = temp
# Test to see if the second number is greater than the third number
if second > third:
        temp = second
        second = third
        third = temp

# Test to see if the first number is greater than the second number again
if first > second :
        temp = first
        first = second
        second = temp

# Print numbers in numerical order
print("Smallest: " + str(first))
print("Next smallest: " + str(second))
print("Largest: " + str(third))




# Summary
# In this lab, you complete a Python program that swaps values stored in three variables and determines maximum and minimum values. The Python file provided for this lab contains the necessary input and output statements.

# You want to end up with the smallest value stored in the variable named first and the largest value stored in the variable named third. You need to write the statements that compare the values and swap them if appropriate.

# Comments included in the code tell you where to write your statements.

# Instructions
# Write the statements that test the first two integers, and swap them if necessary.
# Write the statements that test the second and third integer, and swap them if necessary.
# Write the statements that test the first and second integers again, and swap them if necessary.
# Execute the program using the following sets of input values, and record the output:
# 101 22 -23
# 630 1500 9
# 21 2 2