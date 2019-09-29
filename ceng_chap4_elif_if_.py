# LargeSmall.py - This program calculates the largest and smallest of three integer values. 
# Declare and initialize variables here
firstNumber = -50;
secondNumber = 53;
thirdNumber = 78;

a = -50
b = 53
c = 78

largest = 0 
smallest = 0 

# Write assignment, if, or if else statements here as appropriate

# if thirdNumber > secondNumber:
#     largest = thirdNumber
# elif thirdNumber > firstNumber:
#     largest = thirdNumber

#WOrking Code

if c > b:
        largest = c
elif c > a :
        largest = c
elif b > c:
        largest = b
elif b > a:
        largest = b
elif a > c:
        largest = a
elif a > b:
        largest = a

if a < b:
        smallest = a
elif a < c :
        smallest = a
elif b < a:
        smallest = b
elif b < c:
        smallest = b
elif c < a:
        smallest = a
elif c < b:
        smallest = a



# Output largest and smallest number. 
print("The largest value is " + str(largest))
print("The smallest value is " + str(smallest))