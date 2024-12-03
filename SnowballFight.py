''' 
    Name: Snowball-Mania
    Author: Mateo Maldonado
    Date: 12/3/24
    Class: AP Computer Science Principles
    Python: 3.11.5
'''

import random

def main():
    # the main runner of the game
	  # welcome the player, gather names, and run the snowball fight!
    players = []
    print("Welcome to Snowball Mania!")
    name = input("what is your name? ")
    opponent = input("Great tp have you here, " + name + "! Who do you want to play against? ")
    nextPlayer = ""

    print(name+ " vs. " + opponent)
    players.append(name)
    players.append(opponent)

    while nextPlayer != "DONE":
        nextplayer = input("Are there any other opponents? if not, type DONE")

    thrower = random.choice(players)
    print(thrower + " is the thrower.")
    target = random.choice(players)

    while target == thrower:
        target = random.choice(players)
    print(target + " is the target.")

    while len(players) > 1:
        thrower = random.choice(players)
        print(thrower + " is the thrower.")
        target = random.choice(players)

        while target == thrower:
            target = random.choice(players)
        print(target + " is the target.")
            # print(target)
        print(thrower + " is throwing a snowball at " + target + "!")
        hitNum = random.randint(1, 5)
        success = hitResult(hitNum)

        if success == True:
            print("It's a hit! " + target + "is down!")
            players.remove(target)
        else:
            print("Unfortunately, " + thrower + "has very bad aim and missed.")

    print(thrower + " has won the snowball fight.")


def hitResult(hitNum):
    # based on the number that is passed in, return True or False 
    # indicating if this was a hit or a miss
    if hitNum == 3:
        return True
    return False

main()
