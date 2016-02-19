# racquetBallSim2.py

import time
from random import random


def main():
    t0 = time.time()

    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB)

    t1 = time.time()
    total = t1 - t0
    print("\n", total)


def printIntro():
    print("This program simulates a game of raquetball between two")
    print("players called 'A' and 'B'.  The abilitys of each player")
    print("is indicated by a probability (a number between 0 and 1) that")
    print("the player wins the point when serving.  Player A always")
    print("has the first serve")

def getInputs():
    # returns the three simulation paparmeters
    a = eval(input("What is the prob, player A wins a serve?"))
    b = eval(input("What is the prob, player B wins a serve?"))
    n = eval(input("How many games to simulate? "))
    return a, b, n

def simNGames(n, probA, probB):
    # Simulates n games of racqueteball between players whose
    #   ablilites are represented by the probability of winning a serve.
    # Returns number of wins for A and B 
    winsA = winsB = 0
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB:
            winsA = winsA + 1
        else:
            winsB = winsB + 1
    return winsA, winsB


def simOneGame(probA, probB):
    # simulates a single game of racquetball between players whose
    #   ablilites are represented by the probability of winning a serve.
    # Returns final scores for A and B 
    serving = "A"
    scoreA = scoreB = 0
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random() < probA:
                scoreA = scoreA + 1
            else:
                serving = "B"
        else:
            if random() < probB:
                scoreB = scoreB + 1
            else:
                serving = "A"
    return scoreA, scoreB

def gameOver(a, b):
    # a and b represent scores for racquetball game
    # Returns True if the game is over, Fale if otherwise.
    return a == 15 or b == 15

def printSummary(winsA, winsB):
    # Prints a summary of wins for each player.
    n = winsA + winsB
    print("\nGames Simulated:", n)
    print("Wins for A: {0} ({1:0.1%})".format(winsA, winsA / n))
    print("Wins for B: {0} ({1:0.1%})".format(winsB, winsB / n))
    
if __name__ == '__main__': main()
                
            
    
