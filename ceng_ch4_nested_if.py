
# EmployeeBonus.py - This program calculates an employee's productivity bonus.


# Initialize variables here.
BONUS_1 = 50.00
BONUS_2 = 75.00
BONUS_3 = 100.00
BONUS_4 = 200.00

employeeName = input("Enter employee's name: ")

shiftString = input("Enter number of shifts: ") 
transactString = input("Enter number of transactions: ")
dollarString = input("Enter transactions dollar value: ")

numShifts = float(shiftString)
numTransactions = float(transactString)
dollarValue = float(dollarString)

productivityScore = ( dollarValue / numTransactions ) / numShifts

# Write your code here

if productivityScore <= 30:
        bonus = BONUS_1
elif productivityScore <= 69:
        bonus = BONUS_2
elif productivityScore <= 199:
        bonus = BONUS_3
elif productivityScore >= 200:
        bonus = BONUS_4


# Output.
print("Employee Name: " + employeeName)
print("Employee Bonus: $" + str(bonus))

# Test With
# Employee’s name: Kim Smith 
# Number of Shifts: 25 
# Number of transactions: 75 
# Transaction dollar value: 40000.00

# Expected Output
# Employee Name: Kim Smith 
# Employee Bonus: $50.0