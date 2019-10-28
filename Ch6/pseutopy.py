hits = [0,2,3,4,5]
atBats = [5,4,3,2,1]



playerName = "_"
totalHits = 0
totalAtBats = 0
averageHits = 0.0
averageAtBats = 0.0
terminus="yes"


 # listName.insert(index,variable)

def getPlayerName():
        playerName = input("Write player name ")
        

def getHits():
        index = 1
        for index in range(5) :
                hitsPerGame = input("Player hits for game #" + str(index)+ ": ")
                hits.insert(index,hitsPerGame)
                index = index +1
                

def getAtBats():
        index = 1
        for index in range(5) :
                atBatsPerGame = input("At bats for game #" + str(index)+ ": ")
                atBats.insert(index,atBatsPerGame)
                index = index + 1

# for index, value in enumerate(test_list): 
#     print(index, value) 

# for index, index in enumerate(data):
#     hit_ratio = game[1] - game[0]
#     data[index].insert(2, hit_ratio)


def getTotalHits(totalHits):
        #index = 1
        for index, value in enumerate(hits) :
                #hits.insert(index,totalHits)
                #hits.insert(index,totalHits) # totalHits + hits[index]
                # totalHits = hits.count(index)
                # totalHits = totalHits + totalHits
                # index = index + 1 
                totalHits = hits[1]/5
                hits[index].insert(2,totalHits) # WTF! 
                print(totalHits) 
        
# def getTotalAtBats():

# def averageHits():

# def getBattingAverage():

# def printBBInfo():        

#terminus =  input("Start? Yes/No ")

while terminus == "yes" :
        #getPlayerName()
        #getHits()
        #getAtBats()
        getTotalHits(hits)
        getTotalAtBats()
        getAverageHits()
        getBattingAverage()
        printBBInfo()
        
        print(" Do you want run again?", terminus )
        