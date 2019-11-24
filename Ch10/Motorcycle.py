class Motorcycle(object):
        def __init__(self, maxSpeed, speed, sidecar):
                self.sidecar = sidecar
                self.maxSpeed = maxSpeed
                self.speed = speed
        def accelerate (self, speed):
                if(self.speed > self.maxSpeed or speed + self.speed > self.maxSpeed):
                        print("This motorcycle cannot go that fast")
                else:
                        self.speed = self.speed + speed



"""
Using Inheritance to Create a Derived Class in Python

Summary
In this lab, you create a derived class from a base class, and then use the derived class in a Python program. The program should create two Motorcycle objects, and then set the Motorcycle’s speed, accelerate the Motorcycle object, and check its sidecar status.

Instructions
Open the file named Motorcycle.py.
Create the Motorcycle class by deriving it from the Vehicle class. Use a public derivation.
In the Motorcycle class, create an attribute named sidecar.
Write a public set method to set the value for sidecar.
Write a public get method to retrieve the value of sidecar.
Write a public accelerate method. This method overrides the accelerate method inherited from the Vehicle class. Change the message in the accelerate method so the following is displayed when the Motorcycle tries to accelerate beyond its maximum speed: "This motorcycle cannot go that fast".
Open the file named MyMotorcycleClassProgram.py.
In the MyMotorcycleClassProgram, there are two Motorcycle objects named motorcycleOne and motorcycleTwo.
Set the sidecar value of motorcycleOne to true and the sidecar value of motorcycleTwo to false.
Set motorcycleOne’s maximum speed to 90 and motorcycleTwo’s maximum speed to 85.
Set motorcycleOne’s current speed to 65 and motorcycleTwo’s current speed to 60.
Accelerate motorcycleOne by 30 mph, and accelerate motorcycleTwo by 20 mph.
Print the current speed of motorcycleOne and motorcycleTwo.
Determine if motorcycleOne and motorcycleTwo have sidecars. If yes, display the following: "This motorcycle has a sidecar". If not, display the following: "This motorcycle does not have a sidecar".
Execute the program.
"""