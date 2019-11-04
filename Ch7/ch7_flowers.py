# Flowers.py - This program reads names of flowers and whether they are grown in shade or sun from an input 
# file and prints the information to the user's screen. 
# Input:  flowers.dat.
# Output: Names of flowers and the words sun or shade.

# Open input file
flower = open("flowers.dat","r")
flowerData= None
growData= None

while True:
    flowerData = flower.readline().strip()
    growData = flower.readline().strip()
    if (flowerData == ""):
        break
    print(flowerData + " grows in the " + growData)

# Write while loop here
    # Print flower name using the following format
    # print(var + " grows in the " + var2)










# Opening Files and Performing File Input

# Summary
# In this lab, you open a file and read input from that file in a prewritten Python program. The program should read and print the names of flowers and whether they are grown in shade or sun. The data is stored in the input file named flowers.dat.

# Instructions
# Open the source code file named Flowers.py
# Write a while loop to read the input until EOF is reached.
# In the body of the loop, print the name of each flower and where it can be grown (sun or shade).
# Execute the program.