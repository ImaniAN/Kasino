### ------- Game States ------- ###

class GameState():
    def __init__(self):
        self.prep = True
            #for dealing out cards at the beginning of the game
            #and the beginning of each hand
            #should always go to either waitGM or waitCM next
            #(depending on who is the dealer)

        self.waitP = False
            #right before going to the prep state
        
        self.gettingMove = False
            #waiting for user input from the human player
            #to determine what their move is going to be
            #if the human isn't the dealer, the next state
            #should always be waitCM, otherwise on the last
            #turn of each hand it should go to waitP or last
        
        self.waitGM = False
            #right before gettingMove
        
        self.computerMove = False
            #where the computer's next move is determined
            #and all of the involved cards are highlighted
            #(move not executed yet, goes on to waitCM2
        
        self.waitCM = False
            #right before computerMove
        
        self.displayCM = False
            #in this state the highlighted cards get shown
            #then we actually execute the move (UI and logic)
            #if the computer isn't the dealer, the next state
            #should always be waitCM, otherwise on the last
            #turn of each hand it should go to waitP or last
            
        self.waitCM2 = False
            #right before displayCM
        
        self.last = False
            #when the game is over and the last cards are assigned
            #goes to waitGO
        
        self.gameOver = False
            #displaying the score from this game
            #should go to prep next, resetting the hands and stuff
        
        self.waitGO = False
            #right before gameOver

        self.newGame = False
            #after gameOver, to switch dealers and clear hands before a new game

        self.roundOver = False
            #once a player reaches 21 points, to display the final score

        self.waitRO = False
            #right before roundOver
        
    def clear(self):
        self.prep = False
        self.waitP = False
        self.gettingMove = False
        self.waitGM = False
        self.computerMove = False
        self.waitCM = False
        self.displayCM = False
        self.waitCM2 = False
        self.last = False
        self.gameOver = False
        self.waitGO = False
        self.newGame = False
        self.roundOver = False
        self.waitRO = False
