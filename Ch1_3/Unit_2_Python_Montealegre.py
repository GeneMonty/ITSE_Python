#Eugenio Montealegre
#Sepetember 1, 2019

# I need to fix the variable names to go with the Pseudocode

#This program requests to the user an input of type int then proceeds to provide the totals for
# the sales tax, total gratuities from the amount and the tax on the gratuities. 

#Start

#Delcare Constants
salesTax = 0.10
gratuAmount = 0.08
gratuTax = 0.12

#Declare variables
restaurantSales = int(input("Enter your amount in Sales:$ ")) 

#Calculations

taxTotal = float(restaurantSales) * float(salesTax)
gratuAmountTotal = float(restaurantSales) * float(gratuAmount)
gratuTaxTotal = float(gratuAmountTotal) * float(gratuTax)

#Prints the results for the user.

print("Your Sales: $",restaurantSales ,"Dollars")
print("Sales Tax: $",taxTotal ,"Dollars")
print("Gratuities Total: $",gratuAmountTotal, "Dollars")
print("Tax on Gratuities: $",gratuTaxTotal, "Dollars")

#stop



#print("Your Sales: $",round(restaurantSales, 2) ,"Dollars")
#print("Sales Tax: $",round(taxTotal, 2) ,"Dollars")
#print("Gratuities Total: $",round(gratuAmount, 2), "Dollars")
#print("Tax on Gratuities: $",round(gratuTax, 2) , "Dollars")



