# This program calculates your age in the year 2050.
# Input:  None
# Output: Your current age followed by your age in 2050

# Create your variables here
print("How old are you?")
myCurrentAge = int(input())
print("What year is it?")
currentYear = int(input())
print("Chose a year in the future to calculate")
futureYear = int(input())

myNewAge = myCurrentAge + (futureYear - currentYear)
ageLeft = myNewAge - myCurrentAge

print("My Current Age is " + str(myCurrentAge))
print("I will be " + str(myNewAge) + " in " + str(futureYear) + ".")
if myNewAge > 80 :
        print(" and... you are probably be dead.. :D \n"
        " enjoy your " +str(ageLeft) + " years of life left!!! ")
