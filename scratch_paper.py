
# xLine = 0
# yCol= 0

# even = [0,2,4,6]
# odd = [1,3,5,7]

# asterisk = "*"
# space = " "
# x=0

# while x < 5:
#         xLine=0
#         if xLine == odd:
#                 print(asterisk * 2 + space)
#         else:
#                 if xline == even:
#                         print(asterisk + space)
#         x += 1

# for i in range(1,6):
#         if i% 2 !=0 :
#                 print("**"+" ")
                
#         else:
#                 print("*"+" ")
                
                
#Arrays (aka lists in python)

#myArray = [1,2,3,4,5,6]

my_empty_box = []
my_box = [1,2,3,4,]
my_mixed_box = [1,"gatopardo","box",2*3]
my_nested_box = ["Mouse",[8,7,6],['a']]

print(my_empty_box)
print(my_box)
print(my_mixed_box)
print(my_nested_box)


#select elements from a list
print("\n---Selected Elements---\n")

#Select Elemento 0 and element 3
print("Select Elements 0 and 3:\n",my_box[0],my_box[2])

#select element from nest
print("Select Elements 2 sub 1:\n",my_nested_box[1][0])

#select char from string on list
print(my_nested_box[0], my_nested_box[0][3])
#select negative index
print(my_nested_box[0], my_nested_box[0][-3])
#select range from list
print(my_mixed_box[1][:]) # the whole range
print(my_mixed_box[1][0:5]) #range 0 to 5
print(my_mixed_box[1][:7]) # elem 7 to start
print(my_mixed_box[1][5:]) # elem 5 onward