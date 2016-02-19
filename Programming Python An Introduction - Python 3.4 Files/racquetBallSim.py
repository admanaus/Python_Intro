# racquetBallSim.py

#   This program will simulate a user defined number of Racquet Ball games.
#   It will utilize user defined probablities to simulate games.

from random import random

def main():
    playerA = eval(input("What is the prob. player A will win a serve? "))
    playerB = eval(input("What is the prob. player B will win a serve? "))
    games = eval(input("How many games would you like to simulate? "))
    
    Awin = 0
    Bwin = 0
    
    for i in range(games):

        Apoints = Bpoints = 0  # Reset the score for a new game.
        Aturn = True # determines whose turn it is
        
        while Apoints < 15 and Bpoints < 15: # simulation of one game
            if Aturn == True:
                if random() < playerA:
                    Apoints = Apoints + 1
                else:
                    Aturn = False    
            else:
                if random() < playerB:
                    Bpoints = Bpoints + 1
                else:
                    Aturn = True
                    
        if Apoints > Bpoints: # counting wins
            Awin = Awin + 1
        else:
            Bwin = Bwin + 1
   
    print("\nPlayer A wins: {0} ({1:0.1%})".format(Awin, Awin / games))
    print("Player B wins: {0} ({1:0.1%})".format(Bwin, Bwin / games))

if __name__ == "__main__":
    main()
    
            
                            
               
