salary = float(input())
numDependents = float(input())

# Calculate stateTax here.
stateTax = salary * 0.065
print("State Tax: $" + str(stateTax))

# Calculate federalTax here.
federalTax = salary * 0.28
print("Federal Tax: $" + str(federalTax))

# Calculate dependantDeduction here.
dependentDeduction = numDependents * (salary * 0.025)
print("Dependents: $" + str(dependentDeduction))

# Calculate totalWithholding here.
totalWithholding = stateTax + federalTax + dependentDeduction
# Calculate takeHomePay here.
takeHomePay = salary - totalWithholding

print("Salary: $" + str(salary))
print("Take Home Pay: $" + str(takeHomePay))