#This program will request the value of worked hours in a day, it will calculate the worked hours in 5 day week, and a 252 day work year.

#Declare constants
SLEEP_HOURS = 8
DAY_HOURS = 24
WORK_WEEK = 5
WORK_YEAR = 252
YEAR = 365

workHours = 8 #input()

weekHours = workHours * WORK_WEEK
yearHours = workHours * WORK_YEAR
totalHoursYear = DAY_HOURS * YEAR
leftHoursYear = DAY_HOURS * (YEAR - WORK_YEAR)
sleepingHours = SLEEP_HOURS * YEAR

print("You work: " + str(workHours) + " hours a day")
print("You work: " + str(weekHours) + " Hours a week.")
print("You work: " + str(yearHours) + " hours a year")
print("---------------------------------")
print("You have: " + str(totalHoursYear) + " hours per year")
print("You Sleep around " + str(sleepingHours)  + " hours a year ")

freeHours = totalHoursYear - sleepingHours - yearHours
print("You have " + str(freeHours) + " free hours")
