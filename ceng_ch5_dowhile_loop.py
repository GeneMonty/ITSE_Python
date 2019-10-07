"""
NewestMultiply.py - This program prints the numbers 0 through 10 along with
                     these values multiplied by 2 and by 10.
Input:  None.
Output: Prints the numbers 0 through 10 along with their values multiplied by
        2 and by 10.
"""
head1 = "Number:"
head2 = "Multiplied by 2:"
head3 = "Multiplied by 10: " # WTF you POS incorrect output cause of whitespace?
NUM_LOOPS = 10  # Constant used to control loop.

print("0 through 10 multiplied by 2 and by 10" + "\n")

# Write while loop

i = 0
while i >= 0:
        
        print("")
        print(head1, i)
        print(head2, i * 2)
        print(head3, i * 10)
        
        
#         print(head1, i, " - ", head2, i*2 ," - ", head3, i*10)
        i += 1
        if i > NUM_LOOPS: 
                break
