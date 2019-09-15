# this program can tell you how many hours you have left in a week
# after calculating the required hours of study, also tells you how many study hours per week you need have.
# ADHD requires spread hours accross weekdays

#Declare Constants
HOURS_DAY = 24
HOURS_SLEEP = 8
STUDY_PER_CREDIT_HOUR = 3
WEEK_DAYS = 7
HOURS_WEEK = HOURS_DAY * WEEK_DAYS
WORK_WEEK = 5 # 5 days a week

#Declare Variables
numberClasses = 4
creditHourPerClass = 3
foodHours = 3
gymHours = 1
showerHours = .5
commuteHours = 4
workHours = 4 
hoursInClassPerWeek = 3 * numberClasses 

print("Welcome to [PRODUCTIVE HOURS CALCULATOR]")

totalStudyTimePerClass = creditHourPerClass * STUDY_PER_CREDIT_HOUR #suffer ADHD add + 2 more hours 
totalStudyTimePerWeek =  totalStudyTimePerClass * numberClasses

productiveDay = HOURS_DAY - HOURS_SLEEP
productiveHoursDay = productiveDay - foodHours - gymHours - showerHours - commuteHours - workHours
productiveHoursWeek = (productiveHoursDay * WEEK_DAYS) - hoursInClassPerWeek
productiveHoursWorkWeek = (productiveHoursDay * WORK_WEEK) - hoursInClassPerWeek

print("Per day you have: ", HOURS_DAY, "hours - ", HOURS_SLEEP ,
         "hours of sleep,\nWith a total of",    
         str(productiveDay) , "productive hours per day. \n")

#Display resuls to the user
print("Per week you have left:\n",
        str(productiveHoursDay),"= Productive Study Hours/day\n",
        str(productiveHoursWorkWeek), "= productive Study hours/week (5days).\n",
        str(productiveHoursWeek),"= productive Study hours/week (7days).\n\n",
        
        "Your Current recomended study hours are: \n" ,
        str(totalStudyTimePerClass), "= Hours of Study Time Per Class\n",
        str(totalStudyTimePerWeek),"= Hours Study Time per Week\n",

        
        
        
        
        )



