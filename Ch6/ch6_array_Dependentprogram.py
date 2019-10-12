
dep = 0
counts=[0,0,0,0,0,0]
closeProgram = 999

# def getReady():
#         print("Hello, enter dep or ", closeProgram, "to quit")
#         dep = input()
# def countDeps():
#         counts[dep] = counts[dep]+1
#         print("Enter Deps or" ,closeProgram,"to quit")
#         dep = input()
# def finishUp():
#         print(" Dependents Count")
#         dep = 0
#         while dep < 6:
#                 print (dep , counts[dep])
#                 dep = dep + 1

# getReady()
# while dep != closeProgram:
#         countDeps()
# finishUp()


print("Hello, enter dep or ", closeProgram, "to quit") 
dep = input()

# while dep != closeProgram:
#         counts[0] += 1
#         print(counts)
#         print("Hello, enter dep or ", closeProgram, "to quit")
#         dep = input()
# else :
#         dep1 = 0
#         print(" Dependents - Count")
#         while dep1 < 6:
#                 print(dep1, counts[:])
#                 dep1 = dep1 + 1


while True:
        if dep != closeProgram:
                counts[0] += 1
                print(counts)
                print("Hello, enter dep or ", closeProgram, "to quit")
                dep = input()
        else: 
                dep1 = 0
                print(" Dependents - Count")
                while dep1 < 6:
                        print(dep1, counts[:])
                        dep1 = dep1 + 1