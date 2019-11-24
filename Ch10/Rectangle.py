# Rectangle.py

class Rectangle(object):
    # Declare public methods here
    def __init__(self, length, width):
        self.length = length
        self.width = width
        # Set class instance variables here


    def calculateArea(self):
        return self.length * self.width
        # Write calculateArea here

    def calculatePerimeter(self):
        return 2 * self.length + 2 * self.width
        # Write calculatePerimeter here
