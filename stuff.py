# Prints out 0,1,2,3,4

# count = 0
# while True:
#     print(count)
#     count += 1
#     if count >= 5:
#         break

# # Prints out only odd numbers - 1,3,5,7,9
# for x in range(10):
#     # Check if x is even
#     if x % 2 == 0:
#         continue
#     print(x)

# def square(x):
#         return x*x

# def sum (x,y):
#         return x+y

# z = sum(5,10)
# x = sum(2,4)
# y = sum(8,8)
# i = square(x+z+y)

# print(x)
# print(z)
# print(y)

# print("Square: ",i)
        
# x = [0,5,10]
# senti= 1
# while senti < 20:

#         for index, i in enumerate(x): 
#                 x[index] +=1

#         print (x)
#         senti +=1
 

# def add_5(some_list):
#     new_list = []
#     for i in some_list:
#         new_list.append(i + 5)
#     return new_list 

# i= 1
# while i < 10 :

#To insert value at specific location
# insert(arrayindex,variable)

#to inser value at end of list use .append(variableName)



# MAX_AVG = 8
# avg=[]

# for i in range(MAX_AVG):
#         avgString = input("add number ")
#         battAvg = float(avgString)
#         avg.insert(i,battAvg)
#         print(avg)
#         #avg.append(battAvg)
#         # avg[i] = battAvg #the non python way
#         # i += 1
        
        
        
# degrees = 0       
# convertToRadians(2)

# def convertToRadians():
#         degree = input("Blabla number 1-360")
#         radians = degrees / 57.2957
#         return radians


degrees = 0
radians = 0.0
radDegree = 57.2957
start = "y"

def getRadians(degrees):
        radians = degrees / radDegree
        result = radians
        print(degrees,"degrees =", round(result,2) , "Radians")
        #return result
        #round(number[result, 2])

start = input("Wanto to Start?")
while start == "y" :

        print ("Hello, this dumb ass shit will calculate your radians from Degrees")
        
        degrees =  int(input())

        getRadians(degrees)
        
        start = input("Wanto to continue?")


        