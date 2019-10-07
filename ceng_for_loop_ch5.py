# NewMultiply.py - This program prints the numbers 0 through 10 along
# with these values multiplied by 2 and by 10.
# Input:  None
# Output: Prints the numbers 0 through 10 along with their values multiplied by 2 and by 10. 

head1 = "Number: "
head2 = "Multiplied by 2: "
head3 = "Multiplied by 10: "

NUM_LOOP_START = 0  # Constant used to control loop
NUM_LOOP_END = 10 # Constant used to control loop

print("0 through 10 multiplied by 2 and by 10.")

# Write your for loop here
for x in range(NUM_LOOP_START,NUM_LOOP_END):
    
    print(head1, x ,head2, x * 2 , head3, x * 10)
    