''' 
    Name: Snowball-Mania
    Author: Mateo Maldonado
    Date: 12/3/24
    Class: AP Computer Science Principles
    Python: 3.11.5
'''

import random
import time
t = 2

def main():
    # the main runner of the game
	  # welcome the player, gather names, and run the snowball fight!
    players = []
    playerHits = []
    print("Welcome to Snowball Mania!")
    name = input("what is your name? ")
    opponent = input("Great tp have you here, " + name + "! Who do you want to play against? ")
    nextPlayer = ""

    print(name+ " vs. " + opponent)
    players.append(name)
    playerHits.append(2)
    players.append(opponent)
    playerHits.append(2)

    while nextPlayer != "DONE":
        nextPlayer = input("Are there any other opponents? if not, type DONE ")
        players.append(nextPlayer)
        playerHits.append(2)
    players.remove("DONE")
    playerHits.remove(playerHits[-1])

    choice = input("Do you want to choose who you throw the snowball at or do you want it to be auto mode")

    gameplay(name, players, playerHits, choice)

def gameplay(name, players, playerHits, manual):
    while len(players) > 1:
        thrower = random.choice(players)
        if thrower == name:
            if manual == "yes": #Manual Mode
                target = input("You are up! Who do you want to throw the snowball at? ")
            elif manual == "no": #Auto mode
                target = random.choice(players)
                while target == thrower:
                    target = random.choice(players)
        else:
            target = random.choice(players)
            while target == thrower:
                target = random.choice(players)
        print(thrower + " is the thrower.")
        
        while target == thrower:
            target = random.choice(players)
        time.sleep(t)
        print(target + " is the target.")
            # print(target)
        print(thrower + " is throwing a snowball at " + target + "!")
        hitNum = random.randint(1, 2)
        success = hitResult(hitNum)

        if success == True:
            currentTargetIndex = players.index(target)
            playerHits[currentTargetIndex] += -1
            print(target + " was hit! ")
            if playerHits[currentTargetIndex] <= 0:
                print(target + " is down!")
                players.remove(target)
        else :
             print("Unfortunately, " + thrower + " has very bad aim and missed.")

    print(thrower + " has won the snowball fight.")


def hitResult(hitNum):
    # based on the number that is passed in, return True or False 
    # indicating if this was a hit or a miss
    if hitNum == 2:
        return True
    return False

main()
