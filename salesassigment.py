#Eugenio Montealegre
#Sepetember 1, 2019

#This program requests to the user an input of type float then proceeds to provide the totals for
# the sales tax, total gratuities from the amount and the tax on the gratuities. 

#Start

#Delcare Constants
SALES_TAX = 0.10
GRATU_AMOUNT = 0.08
GRATU_TAX = 0.12

#Declare variables
restaurantSales = int(input("Enter your amount in Sales:$ ")) 

#Calculations

taxTotal = float(restaurantSales) * float(SALES_TAX)
gratuAmountTotal = float(restaurantSales) * float(GRATU_AMOUNT)
gratuTaxTotal = float(gratuAmountTotal) * float(GRATU_TAX)

#Prints the results for the user.

print("Your Sales: $",restaurantSales ,"Dollars")
print("Sales Tax: $",taxTotal ,"Dollars")
print("Gratuities Total: $",gratuAmountTotal, "Dollars")
print("Tax on Gratuities: $",gratuTaxTotal, "Dollars")

#stop


#print("Your Sales: $",round(restaurantSales, 2) ,"Dollars")
#print("Sales Tax: $",round(taxTotal, 2) ,"Dollars")
#print("Gratuities Total: $",round(GRATU_AMOUNT, 2), "Dollars")
#print("Tax on Gratuities: $",round(GRATU_TAX, 2) , "Dollars")




