### -------- Interactive Functions (ex. knowing what card the player clicked on) ------- ###

from CasinoCardGraphics import cardSpots
from CasinoVariables import moveType, buildRankDict, buildChoicesSpots


def getCard(): #this gets called when you click enter - it returns a tuple with the move type and the card you want to play from your hand
    for spot in cardSpots[:4]:
        if spot.selected:
            return spot.card
    return None


def getTableCards(): #returns a list with all of the cards on the table that are currently selected (not including builds)
    selectedTableCards = []
    for spot in cardSpots[8:22]:
        if spot.selected:
            selectedTableCards.append(spot.card)
    return selectedTableCards


def getSelectedBuildRank(): #returns the rank of the build selected (you can't take two different builds in the same turn)
    if cardSpots[22].selected:
        return buildRankDict[0]
    elif cardSpots[32].selected:
        return buildRankDict[1]
    elif cardSpots[42].selected:
        return buildRankDict[2]
    elif cardSpots[52].selected:
        return buildRankDict[3]
    else:
        return 0


#buildChoicesSpots = {0: (24*33,24*25), 1: (24*35,24*25), 2: (24*37,24*25), 3: (24*39,24*25)}

def buildFromCoordinates(x, y): #tells you what rank the player clicked on to indicate that they want to build to that
    for build in buildChoicesSpots.keys():
        if (buildChoicesSpots[build][0] < x < buildChoicesSpots[build][0]+24*2) and (buildChoicesSpots[build][1] < y < buildChoicesSpots[build][0]+24):
            return build
    return None




