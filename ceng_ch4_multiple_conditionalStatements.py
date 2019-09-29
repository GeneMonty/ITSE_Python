# EmployeeBonus2.py - This program calculates an employee's yearly bonus. 

# Declare and initialize variables here
BONUS_1 = 0.25
BONUS_2 = 0.15
BONUS_3 = 0.1
NO_BONUS = 0

RATING_1 = 1
RATING_2 = 2
RATING_3 = 3

employeeFirstName = "Juan" #input("Enter employee's first name: ")
employeeLastName = "Sim"#input("Enter employee's last name: ")
employeeSalary = 70000 #float(input("Enter the employee's yearly salary: "))
employeeRating = 2 #int(input("Enter employee's performance rating: "))

# Write your code here

if employeeRating == 1:
        bonus = employeeSalary * BONUS_1
elif employeeRating == 2:
        bonus = employeeSalary * BONUS_2
elif employeeRating == 3:
        bonus = employeeSalary * BONUS_3
elif employeeRating >= 4:
        bonus = NO_BONUS

# Output bonus here
print("Employee Name: " + employeeFirstName + " " + employeeLastName)
print("Employee Bonus: $" + str(bonus))


# test with 
# Jeanne Hanson
# 70000.00
# 2

# Expected Output

# Employee Name: Jeanne Hanson
# Employee Bonus: $10500