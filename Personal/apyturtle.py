from turtle import *
import turtle


colors_2 = ['blue', 'red', 'skyblue', 'navy', 'crimson','skyblue']

wn = turtle.Screen()
tess = turtle.Turtle()
pendown()
def draw(x, y): # x, y are mouse position arguments passed by onclick()
        
        pencolor(colors_2[1])
        tess.clear() # Clear out the drawing (if any)
        tess.reset() # Reset the turtle to original position
        tess.hideturtle()
        pencolor(colors_2[1])

        tess.left(0)
        tess.forward(100)
        for a in range(7):
                tess.left(45)
                tess.forward(100)
        tess.right(0) # to go to original place

draw(0, 0) # Draw the first time

wn.onclick(draw) # Register function draw to the event mouse_click
wn.onkey(wn.bye, "q") # Register function exit to event key_press "q"

wn.listen() # Begin listening to events like key_press & mouse_clicks
wn.mainloop()
