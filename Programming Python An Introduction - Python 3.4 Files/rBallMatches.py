# rBallMatches.py

from random import random


def main():
    printIntro()
    probA, probB, matches, gamesInMatch = getInputs()
    matchWinsA, matchWinsB = matchWins(probA, probB, matches, gamesInMatch)
    printSummary(matchWinsA, matchWinsB)

def printIntro():
    print("This program simulates a games of raquetball between two")
    print("players called 'A' and 'B'.  The abilitys of each player")
    print("is indicated by a probability (a number between 0 and 1) that")
    print("the player wins the point when serving.  Player A always")
    print("has the first serve.")
    print("This program will also simulate the winner of X game matches.")

def getInputs():
    # returns the four simulation paparmeters
    a = eval(input("What is the prob, player A wins a serve?"))
    b = eval(input("What is the prob, player B wins a serve?"))
    gamesInMatch = eval(input("How many games are in a match?"))
    matches = eval(input("How many matches to simulate? "))
    return a, b, matches, gamesInMatch

def matchWins(probA, probB, matches, gamesInMatch):
    # Simulates X number of matches and returns match wins
    matchWinsA = matchWinsB = 0
    for i in range(matches):
        winsA = winsB = 0
        # while not matchOver(winsA, winsB, gamesInMatch):
        winsA, winsB = simNGames(gamesInMatch, probA, probB)
        print("===Match A:", winsA, "B:", winsB)
        if winsA > winsB: matchWinsA = matchWinsA + 1
        else: matchWinsB = matchWinsB + 1
        print("Running Total Match Wins: A:", matchWinsA, "B:", matchWinsB)
        
    return matchWinsA, matchWinsB

def simNGames(n, probA, probB):
    # Simulates n games of racqueteball between players whose
    #   ablilites are represented by the probability of winning a serve.
    # Returns number of wins for A and B 
    winsA = winsB = 0
    
    for i in range(n):
        while winsA < (n / 2) and winsB < (n / 2):
        # ends a match if one player has won half of the possible games.                                            # has won more than half the games in                                      
            scoreA, scoreB = simOneGame(probA, probB)
            if scoreA > scoreB: winsA = winsA + 1
            else: winsB = winsB + 1   
    return winsA, winsB

def simOneGame(probA, probB):
    # simulates a single game of racquetball between players whose
    #   ablilites are represented by the probability of winning a serve.
    # Returns final scores for A and B 
    serving = "A"
    scoreA = scoreB = 0

    if random() > .5: serving = "A" # randomize who serves first in any given game
    else: serving = "B"

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
    # print("Game A:", scoreA, "Game B:", scoreB)
    return scoreA, scoreB

def gameOver(a, b):
    # a and b represent scores for racquetball game
    # Returns True if the game is over, Fale if otherwise.
    return a == 15 or b == 15

def matchOver(a, b, n):
    # a and b represent wins in a match
    # returns True if match is over, Fales if otherwise.
    return (a >= (n / 2)) or (b >= (n / 2))

def printSummary(winsA, winsB):
    # Prints a summary of wins for each player.
    n = winsA + winsB
    print("\nMatches Simulated:", n)
    print("Match Wins for A: {0} ({1:0.1%})".format(winsA, winsA / n))
    print("Match Wins for B: {0} ({1:0.1%})".format(winsB, winsB / n))
    
if __name__ == '__main__': main()
                
            
    
