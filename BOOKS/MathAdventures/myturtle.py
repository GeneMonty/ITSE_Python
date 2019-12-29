from turtle import *

import turtle
import random
import time

bgcolor("black")
color('red','blue')
# shape('arrow')
i=1
x=0
#turtle.tracer(1,1)
turtle.tracer(3,3)
#turtle.tracer(0,0)
#for i in range(100):
# while i < 300:
#      rt(90)
#      fd(1+(2*i))
#      left(x-i)
#      i+=1
#      x=180
          

# while True:
#      while i < 100: # Star
#           rt(15)
#           fd(300+(x+i))
#           rt(180)
#           i+=1
#           x=x+1

# for i in range(400):
#      fd(i)
#      left(91)
     
     

# pendown()
# for angle in range(0,360,20):
#      setheading(angle)
#      forward(100)
#      write(str(angle) + '*')
#      backward(100)

colors = ['purple', 'blue','skyblue', 'red', 'orange']

colors_2 = ['blue', 'red', 'skyblue', 'navy', 'crimson','skyblue']
colors_3 =  ['dimgray','gray','darkgrey','silver','gainsboro','whitesmoke']
colors_4 = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']

pendown()
for x in range(360):
     width(5)
     rt(61)
     fd(10)#(10+(x/0.5))
     pencolor(colors_4[1])
     y=x
     for x in range(6):
          pencolor(colors_3[x % 6])
          width(1)#(1+(x/800))#(x/5+1)
          # forward(x)
          # left(15)
          # forward(-x)
          # rt(180)
          fd(50.1+(x*1))
          rt(46)
          i=i+1
          pencolor(colors_4[y%6])



done()
turtle.update()
turtle.sleep()



# for x in range(24):
#      width(5)
#      rt(46)
#      #fd(10+(x/0.5))
     
#      for x in range(6):
#           pencolor(colors_2[x % 6])
#           width(1)#(1+(x/800))#(x/5+1)
#           # forward(x)
#           # left(15)
#           # forward(-x)
#           # rt(180)
#           fd(10.1+(x*1))
#           rt(46)
#           i=i+1

#      for x in range(6):
#           pencolor(colors_4[x % 6])
#           width(1)#(1+(x/800))#(x/5+1)
#           # forward(x)
#           # left(15)
#           # forward(-x)
#           # rt(180)
#           fd(50.1+(x*1))
#           lt(16)
#           i=i+1

