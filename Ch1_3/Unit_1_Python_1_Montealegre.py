#Eugenio Montealegre
#August 31, 2019
#This program will prompt the user for certain client and product information,
#then it will make a calculation and store it, and finally print out all the previous requested
#information plus the final calculation for the downpayment.

#Start

#Lets prompt the user for information.

customerName = input('Enter the customer name: ')
bikeName = input('Enter the name of the bike: ')
bikePrice = input('Enter the price of the bike: $')
downPayment = input('Enter the down payment for the bike: $')

#After gathering all the information, we now display it back to the user.

print('The customer\'s name is: ' + customerName)
print('The name of the bike is: ' + bikeName)
print('The price of the bike is: $' + bikePrice)
print('The down payment for the bike is: $' + downPayment)

#This part will calculate the final amout left to pay 

netCost = int(bikePrice) - int(downPayment)

print("There is a amount of $" + str(netCost) + " dollars left to pay for the bike.")

#End



