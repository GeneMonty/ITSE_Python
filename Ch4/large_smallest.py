# LargeSmall.py - This program calculates the largest and smallest of three integer values. 
# Declare and initialize variables here
a = -50;
b = 85;
c = 79;


largest = 0
smallest = 0
# Write assignment, if, or if else statements here as appropriate

# if c > b:
#         largest = c
# elif c > a :
#         largest = c
# elif b > c:
#         largest = b
# elif b > a:
#         largest = b
# elif a > c:
#         largest = a
# elif a > b:
#         largest = a

# if a < b:
#         smallest = a
# elif a < c :
#         smallest = a
# elif b < a:
#         smallest = b
# elif b < c:
#         smallest = b
# elif c < a:
#         smallest = a
# elif c < b:
#         smallest = a
def comparison(a,b,c):    
        if a<b:
                if a<c:
                        return(a)
        if b<a:
                if b < c:
                        return(b)
        if c<a:
                if c < b:
                        return(c)
        return 'none' 

comparison(a,b,c)

# Output largest and smallest number. 
print("The largest value is " + str(largest))
print("The smallest value is " + str(smallest))
