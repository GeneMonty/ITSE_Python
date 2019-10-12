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

qNum=1
#(d*quadrantNumber*2)
x_even = (4*qNum)-1
x_odd = (4*qNum)+1
print("\nCoterminal Angles of 45° \nAccross 16 Quadrants in Radians\n")
while qNum < 5:
        qNum += 1
        print(str(x_even) + "π/4")
        print(str(x_odd) + "π/4")
        x_even = (4*qNum)-1
        x_odd = (4*qNum)+1
