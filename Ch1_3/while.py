"""
Multiply.py - This program prints the numbers 0 through 10 along
              with these values multiplied by 2 and by 10.
Input:  None.
Output: Prints the numbers 0 through 10 along with their values multiplied by
        2 and by 10.
"""


head1 = "Number: "
head2 = "Multiplied by 2: "
head3 = "Multiplied by 10:  "
NUM_LOOPS = 10  # Constant used to control loop.

print("0 through 10 multiplied by 2 and by 10" + "\n")

# Initialize loop control variable.
# Write your counter controlled while loop here
    # Multiply by 10.
    # Multiply by 2.
numberCounter = -1
byTwo = numberCounter * 2
byTen = numberCounter * 10
    
while numberCounter < 10 :
    numberCounter = numberCounter + 1
    byTwo = numberCounter * 2
    byTen = numberCounter * 10
    print(head1 + str(numberCounter))
    print(head2 + str(byTwo))
    print(head3 + str(byTen))
    # Next number.
