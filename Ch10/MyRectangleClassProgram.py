# This program uses the programmer-defined Rectangle class.

# Do NOT modify this program. Write your code in Rectangle.py,
# then select this file and click "Run Code".

from Rectangle import Rectangle

rectangle1 = Rectangle(10.0, 5.0)
rectangle2 = Rectangle(7.0, 3.0)

print("Perimeter of rectangle1 is " + str(rectangle1.calculatePerimeter()))
print("Area of rectangle1 is " + str(rectangle1.calculateArea()))
print("Perimeter of rectangle2 is " + str(rectangle2.calculatePerimeter()))
print("Area of rectangle2 is " + str(rectangle2.calculateArea()))
