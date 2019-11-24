#Goers Per Day
d1 = 200
d2 = d1 + (d1 * .30)
d3 = d2 + (d2 * .25)
d4 = d3 - (d3 * .20)
#Money per day
t=2.10
totD1= d1*t
totD2= d2*t
totD3= d3*t
totD4= d4*t
#total Goers
totalGo = d1+d2+d3+d4
toGoIncome = totalGo * t
avGoIncome = toGoIncome / 4
#Average Goers
avGo = totalGo / 4

print("Value of Goers (ticket?): $",t)
print(
        "","Day 1",d1,"$",totD1,"\n",
        "Day 2",d2,"$",totD2,"\n",
        "Day 3",d3,"$",totD3,"\n",
        "Day 4",d4,"$",totD4,"\n",
        )
print("Expected Goers 4 in days ",totalGo)
print("Average Goers: ",avGo)
print("Average Income per Day $", avGoIncome)
print("Total Income: $",toGoIncome)



