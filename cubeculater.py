#This program calculates the the area of the side of a cube
#the area of a cube and its volume using the measure of one edge.

print ("What is the measure of the cube Edge in meters?")
cubeEdge = 5#int(input())

#Calculations

squareArea = cubeEdge ** 2
cubeArea = 6 * squareArea
cubeVolume = cubeEdge ** 3 
spaceDiagonal = (3 ** 1/2) * cubeEdge

# space diagonal is d ≈ sqrt(3) * a


print ("Your edge measures",str(cubeEdge), "meters, therefore: ")
print ("Side Surface Area: ", str(squareArea),"m^2")
print("Cube Surface Area: ", str(cubeArea),"m^2")
print("Cube Volume: ", str(cubeVolume),"m^3")
print("The diagonal space ≈ ", str(spaceDiagonal),"units.")


