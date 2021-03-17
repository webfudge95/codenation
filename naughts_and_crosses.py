from os import system
from random import randint

def is_section(num):
    if(num % 4) == 0:
        return True
    else:
        return False

grid = range(1, 12)
squares = [" "," "," "," "," "," "," "," "," "]

start = True

def clear():
    system("clear")

vertical = "   {}   |   {}   |   {}   "
horizontal = "-------|-------|-------"
    

def drawGrid():
    for item in grid:
        if (is_section(item)) == True:
            print(horizontal)
        else:
            if item == 2:
                print(vertical.format(squares[0],squares[1],squares[2]))
            elif item == 6:
                print(vertical.format(squares[3],squares[4],squares[5]))
            elif item == 10:
                print(vertical.format(squares[6],squares[7],squares[8]))
            else:
                print(vertical.format(" "," "," "))

def checkHorzontal():
    number = [0, 1, 2]
    for item in range (0, 3):
        if squares[number[0]] == "x" and squares[number[1]] == "x" and squares[number[2]] == "x":
            return True
        elif squares[number[0]] == "o" and squares[number[1]] == "o" and squares[number[2]] == "o":
            return True
        else:
            number = [x + 1 for x in number]

def checkVertical():
    number = [0, 3, 6]
    for item in range (0, 3):
        if squares[number[0]] == "x" and squares[number[1]] == "x" and squares[number[2]] == "x":
            return True
        elif squares[number[0]] == "o" and squares[number[1]] == "o" and squares[number[2]] == "o":
            return True
        else:
            number = [x + 1 for x in number]

def checkStalemale():
    if " " in squares:
        return False
    else:
        return True

def checkWin():
    check1 = checkHorzontal()
    check2 = checkVertical()

    sm = checkStalemale()
    if sm == True:
        print("No winners!")
        exit()

    if check1 == True or check2 == True:
        return True
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
        userplace = int(input("Choose a number between 1 and 9: ")) - 1

        if userplace > 9 or userplace < :
            print("Please choose an appropriate number!")
        elif squares[userplace] == " ":
            squares[userplace] = "x"
            check = False
        else:
            clear()
            drawGrid()
            print("Spot Occupied!")

def game():
    win = False
    print("Welcome to naughts and Crosses")
    drawGrid()
    while win != True:
        userPlace()
        clear()
        drawGrid()
        win = checkWin()
        if win != True:
            computerPlace()
            drawGrid()
            win = checkWin()
    print("Winner")
    exit()

game()