# Cornwall.py - This program computes hotel guest rates.
# Input:  Days in stay and meals included
# Output:  Hotel guest rate

# Write computeRate function here
# def computeRate(days):
#     rate = days * 99.99
#     return rate

# def computeRate(days,question,planQuestion):
    
#     if question == "Y" and planQuestion == "A":
#         rate = days * 169.00
#         return rate
#     elif question == "Y" and planQuestion == "C":
#         rate = days * 112.00
#         return rate
#     elif question =="N":
#         rate = days * 99.99
#         return rate

# third attempt
# def computeRate (days):
#     if question == 'N':
#         rate = days * 99.99
#         return rate
#     elif question == 'Y':
#          planQuestion = input("Do you want a meal plan A or C ? " ) # A or C
#          if planQuestion == 'A':
#             rate = days * 169.00
#             return rate
#          elif planQuestion == 'C':
#             rate = days *112.00
#             return rate
#          else:
#             planQuestion = input("Do you want a meal plan A or C ? " )
             
             
#THIS WORKS
# Cornwall.py - This program computes hotel guest rates.
# Input:  Days in stay and meals included
# Output:  Hotel guest rate

# Write computeRate function here

def computeRate(days,mealPlan='0'):
    if mealPlan == 'A':
        return days * 169.00
    elif mealPlan =='C':
        return days * 112.00
    else:
        return days * 99.99

if __name__ == '__main__':
    rate = 0.00
    dayString = input("How many days do you plan to stay? ")
    days = int(dayString)
    question = input("Do you want a meal plan? Y or N")
    if question == 'Y':
        mealPlan = input("A or C: ")
        rate =  computeRate(days,mealPlan)
    else:
        rate = computeRate(days)

    # Figure out which arguments to pass to the computeRate() function and 
    # then call the computeRate() function
    print("The rate for your stay is: ", rate )
    
    
    
#end program Works