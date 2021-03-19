from os import system
from random import randint
import drawgrid as dg

grid = range(1, 12)
squares = [" "," "," "," "," "," "," "," "," "]

def checkRange(cell1, cell2, cell3):
    if squares[cell1] ==  squares[cell2] and squares[cell2] == squares[cell3]:
        if ' ' in squares[cell1]:
            return False
        else:
            return True
    else:
        return False
        
def checkHorzontal():
    number = [0, 1, 2]
    for item in range (3):
        if checkRange(number[0], number[1], number[2]) == True:
            return True
        else:
            number = [x + 3 for x in number]

def checkVertical():
    number = [0, 3, 6]
    for item in range (3):
        if checkRange(number[0], number[1], number[2]) == True:
            return True
        else:
            number = [x + 1 for x in number]

def checkDiagonal():
    if checkRange(0, 4, 8) == True or checkRange(2, 4, 6) == True:
        return True

def checkStalemale():
    if " " in squares:
        return False
    else:
        return True

def checkWin():
    if checkHorzontal() == True or checkVertical() == True or checkDiagonal() == True:
        return True
    elif checkStalemale() == True:
        print("\nNo winners!")
        exit()
    else:
        return False

def computerPlace():
    check = True
    while check == True:
        compplace = randint(0, 8)
        if squares[compplace] == " ":
            squares[compplace] = "o"
            check = False

def userPlace():
    check = True
    while check == True:
        while True:
            try:
                userplace = int(input("\nChoose a number between 1 and 9: ")) - 1
                break
            except:
                dg.drawGrid(grid, squares)
                print("\nPlease choose an appropriate number!")

        if userplace > 9 or "-" in str(userplace):
            dg.drawGrid(grid, squares)
            print("\nPlease choose an appropriate number!")
        else:
            if squares[userplace] == " ":
                squares[userplace] = "x"
                check = False
            else:
                dg.drawGrid(grid, squares)
                print("\nSpot Occupied!")

def game():
    dg.drawGrid(grid, squares)
    player = 1
    computer = 2
    order = randint(1,2)
    print("{} will go first".format(order))

    while True:
        userPlace()
        dg.drawGrid(grid, squares)
        if checkWin() == True:
            print("\nWinner is Player")
            exit()
        computerPlace()
        dg.drawGrid(grid, squares)
        if checkWin() == True:
            print("\nWinner is Computer")
            exit()
    exit()

game()
