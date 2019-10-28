import math


d=4 # 45 degrees
piQuad= 1
piNum = 1

n = (d-piNum)

num = str(piQuad) + "π"
#control (d*2)+1 q5

#405degree = 9pi/4
q5 =(d*3)-3
q5_2 =(d*2)+1

#495 degrees = 11pi/4
q6 = (d*3)-1
q6_2 = (d*2)+3

#585degree = 13pi/4
q7 = (d*3) + 1
q7_2 = (d*2) + 5

#675degree = 15pi/4
q8 = (d*4)-1
q8_2 = (d*2)+7

print("Quad 5:",str(q5)+"π/4","-", str(q5_2)+"π/4")
print("Quad 6:",str(q6)+"π/4","-", str(q6_2)+"π/4")
print("Quad 7:",str(q7)+"π/4","-", str(q7_2)+"π/4")
print("Quad 8:",str(q8)+"π/4","-", str(q8_2)+"π/4")

angle45 = str(n) + "/" + str(d)
print(angle45) 

angle135 = str(n) + "/" + str(d)
print(angle135)

qNum = 0
#(d*quadrantNumber*2)
x_even = (4*qNum)-1
x_odd = (4*qNum)+1
print("\nCoterminal Angles of 45° \nAccross 16 Quadrants in Radians\n")

#print(math.pi)

#  def getDegrees(n,d):
#           return (n  180) / d

# def getPies(n,d):
#         return str(((degree * 100)/180))+" π/"+str(d)


#Init Variables
# n=1
# d=4
# qNum = 1


# for qNum in range(4):
#         degree = getDegrees(n,d)
#         pies = getPies (n,d)
#         #print("Quadrant ", qNum+1 ,"\n", str(degree)+"°" ,"-->", pies)
#         print("\n", str(degree)+"°" ,"-->", pies)
        
#         #print(str(x_even) + "π/4"+ " -> " + str(degree)+"°")
#         n = n + 1
#         # x_odd = x_odd
                
# for qNum in range(4):
#         #qNum += 1
#         print("Quadrant " , qNum) # Still not working as required
#         degree = getDegrees(x_even,4)
#         print(str(x_even) + "π/4"+ " -> " + str(degree)+"°")
#         degree = getDegrees(x_odd,4)
#         print(str(x_odd) + "π/4"+ " -> " + str(degree)+"°"," \n")
#         x_even = (4*qNum)-1
#         x_odd = (4*qNum)+1

while 4> qNum : # pi/4
        qNum += 1
        #print("Quadrant " , qNum)
        #degree = getDegrees(x_even,4)
        print(str(x_even) + "π/4" )
        #degree = getDegrees(x_odd,4)
        print(str(x_odd) + "π/4" )
        x_even = (4*qNum)-1
        x_odd = (4*qNum)+1 

print("\n--\n ")



#4 is the denominator of the pi
#i is the numerator
#Qadrant 1 : n = d/d
#Quadran 2 : n = d-1
#OLD VERSION
# def get_x_even(i):
#         #even = (4*i)#-1      
#         even = (2*i)+1
#         odd = (4*i)+1 
#         return even, odd

# i=1

quads = 8
pi = 3.1428
#1 radian = 57.2957 degrees
radianDegree = 57.2957
#1pi/4 
#(1pi/4)* radianDegree

def get_pi_numerator(i): #Gets numerator
        num30 = (2*i)+1 #numerator = (2*i)+1 no working
        num45 = (2*i)+1 #numerator = (2*i)+1
        num60 = (2*i)+1 #numerator = (2*i)+1
        return num30,num45,num60

print("\nCoterminal Angles of 45° \nAccross " + str(quads) + " Quadrants in Radians\n")

for i in range(quads):
        #i += 1
        print("Quadrant: "+str(i+1))
        
        #print("[X] "+str(get_pi_numerator(i)[0])+ "π/6") #30
        print("[✓] "+str(get_pi_numerator(i)[1])+ "π/4" ,"--->" , 
              int((((get_pi_numerator(i)[1])*(pi))/4)*radianDegree),"° \n") #45
        #print("[X] "+str(get_pi_numerator(i)[2])+ "π/3") #60
        
        
        #print("",get_x_even(i)[0] , "π/4" ,"\n", get_x_even(i)[1] ,"π/4")
        i += 1
