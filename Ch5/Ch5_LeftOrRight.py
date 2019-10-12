# """
# LeftOrRight.py - This program calculates the total number of left-handed and
#                    right-handed students in a class.
# Input:  L for left-handed; R for right handed; X to quit.
# Output: Prints the number of left-handed students and the number of right-handed students.
# """

rightTotal = 0  # Number of right-handed students.
leftTotal = 0  # Number of left-handed students.

leftOrRight = input("Enter | L (Left-Handed) | R (Right-Handed) | X (Quit to results) |\n")

while True:
        if leftOrRight == "L" or leftOrRight== "l":
                leftTotal +=1
                leftOrRight = input("| L (Left-Handed) | R (Right-Handed) | X (Quit to results) |\n")

        elif leftOrRight == "R" or leftOrRight =="r":
                rightTotal += 1
                leftOrRight = input("| L (Left-Handed) | R (Right-Handed) | X (Quit to results) |\n")

        elif leftOrRight == "X" or leftOrRight == "x":
                print("--YOUR RESULTS ARE --\n")
                print("Number of left-handed students: " + str(leftTotal))
                print("Number of right-handed students: " + str(rightTotal)) 
                print("Goodbye! :)")
                break
        else:
                print("WOOPS! Wrong Input! :( ")
                leftOrRight = input("| L (Left-Handed) | R (Right-Handed) | X (Quit to results) |\n")



# Output number of left or right-handed students.
# print("Number of left-handed students: " + str(leftTotal))
# print("Number of right-handed students: " + str(rightTotal))


# Summary
        # In this lab, you add a loop and the statements that make up the loop body to a Python program. When completed, the program should calculate two totals: the number of left-handed people and the number of right-handed people in your class. Your loop should execute until the user enters the character X instead of a L for left-handed or a R for right-handed.

        # The inputs for this program are as follows: R, R, R, L, L, L, R, L, R, R, L, X.

        # Note that variables have been assigned for you, and the input and output statements have been written for you.

# Instructions
        # Make sure the file LeftOrRight.py is selected and open.
        # Write a loop and a loop body that allows you to calculate a total of left-handed and a total of right-handed people in your class.
        # Execute the program using the Run bottom at the bottom of the screen. Input the data listed above and verify that the output is correct.
# Grading
# When you have completed your program, click the Submit button to record your score.