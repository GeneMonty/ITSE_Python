#Eugenio Montealegre
#Sepetember 1, 2019

#This program requests to the user an input of type float then proceeds to provide the totals for
# the sales tax, total gratuities from the amount and the tax on the gratuities. 

#Start

#Declare variables
restauranSales = int(input("Enter your amount in Sales:$ ")) 

#Delcare Constants
salesTax = 0.10
gratuAmount= 0.08
gratuTax = 0.12

#Calculations

taxTotal = float(restauranSales) * float(salesTax)
gratuAmount = float(restauranSales) * float(gratuAmount)
gratuTax = float(gratuAmount) * float(gratuTax)

#Prints the results for the user.

print("Your Sales: $",restauranSales ,"Dollars")
print("Sales Tax: $",taxTotal ,"Dollars")
print("Gratuities Total: $",gratuAmount, "Dollars")
print("Tax on Gratuities: $",gratuTax, "Dollars")

#stop


#print("Your Sales: $",round(restauranSales, 2) ,"Dollars")
#print("Sales Tax: $",round(taxTotal, 2) ,"Dollars")
#print("Gratuities Total: $",round(gratuAmount, 2), "Dollars")
#print("Tax on Gratuities: $",round(gratuTax, 2) , "Dollars")




