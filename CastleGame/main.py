from os import system
from time import sleep
from dungeon import nac

#   Defining rooms

rooms = [
    "The Armoury",
    "The Bed Chambers",
    "The Dungeon",
    "The Royal Garden",
    "The Grand Gallery",
    "The Guard Tower",
    "The Throne Room (Requires 3 Keys)"
]

#   Defining Variables

locked = [0,0,0,0,0,0,1]
lives = 3
keys = 0

'''
    Our individual room logic go here.
    Room function must return True or False depending if the user passes or fails the room.
'''

def dungeon():
    return nac()
def armoury():
    print("You're in the Armoury")
    return True
def gallery():
    print("You're in the Grand Gallery")
    return True
def tower():
    print("You're in the Guard Tower")
    return True
def garden():
    print("You're in the Royal Garden")
    return True
def bedchambers():
    print("You're in the Bed Chambers")
    return True

#   Key functions

def clear():
    system("clear")

def failCheck(function):
    if function == True:
        return True
    else:
        return False
    
def printPadlock(num):
    if num == 1:
        return "🔒"
    else:
        return ""

def checkLocked(choice, locked):
    if locked[choice - 1] == 1 and choice != 7:
        return True
    else:
        return False

#   Defining Room logic

def enterRoom(choice, keys, locked):
    if choice == 1:
        cond = failCheck(armoury())
        locked[choice - 1] = 1
        return cond, locked
    elif choice == 2:
        cond = failCheck(bedchambers())
        locked[choice - 1] = 1
        return cond, locked
    elif choice == 3:
        cond = failCheck(dungeon())
        locked[choice - 1] = 1
        return cond, locked
    elif choice == 4:
        cond = failCheck(garden())
        locked[choice - 1] = 1
        return cond, locked
    elif choice == 5:
        cond = failCheck(gallery())
        locked[choice - 1] = 1
        return cond, locked
    elif choice == 6:
        cond = failCheck(tower())
        locked[choice - 1] = 1
        return cond, locked
    elif choice == 7:
        if keys >= 3:
            return 2, locked
        else:
            return 3, locked

#   Getting user input

def getChoice(locked):
    choice = int(input("Which room will you enter? (Type Number): "))
    while choice < 1 or choice > 7:
        print("Please enter a number between 1 and 7")
        choice = int(input("Which room will you enter? (Type Number): "))
    check = checkLocked(choice, locked)
    while check == True:
        choice = int(input("That room is locked!"
",Which room will you enter? (Type Number): "))
        check = checkLocked(choice, locked)
    return choice

#   Defining user hub (Grand Hall)

def grandHall(lives, keys, locked):
    print("Lives: "," ","♥ " * lives)
    print("Keys: "," ","🔑" * keys)
    print("You are in the grand hall, 6 Doors lie in front of you.")
    for room in range(7):
        print(f"{room + 1}. {rooms[room]} {printPadlock(locked[room])}")

#    Main game logic

def game(lives, keys, locked):
    print("Welcome to Dracula's Castle")
    print("The door creeks as you enter the Grand Hall")
    door = "closed"
    while door == "closed":
        grandHall(lives, keys, locked)
        room, locked = enterRoom(getChoice(locked), keys, locked)
        if room == 1:
            print("You gained a key")
            keys += 1
            sleep(3)
        elif room == 2:
            print("You unlock the door, it creaks open slowly")
            door = "open"
        elif room == 3:
            print("You haven't enough keys!")
            sleep(3)
        else:
            print("You Lost a life")
            lives = lives - 1
            sleep(3)
        if lives == 0:
            print("You have died..")
            exit()    
        clear()
    print("You enter the final room and find the treasure 💰💰💰")

game(lives, keys, locked)
    
