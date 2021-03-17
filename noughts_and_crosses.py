from os import system
from random import randint

def is_section(num):
    if(num % 4) == 0:
        return True
    else:
        return False

grid = range(1, 12)
squares = [" "," "," "," "," "," "," "," "," "]

def clear():
    system("clear")

vertical = "   {}   |   {}   |   {}   "
horizontal = "-------|-------|-------"    

def drawGrid():
    print("Simple Noughts and Crosses Game\n")
    for item in grid:
        if (is_section(item)) == True:
            print(horizontal)
        else:
            if item == 3:
                print(vertical.format(1,2,3))
            elif item == 2:
                print(vertical.format(squares[0],squares[1],squares[2]))
            elif item == 7:
                print(vertical.format(4,5,6))
            elif item == 6:
                print(vertical.format(squares[3],squares[4],squares[5]))
            elif item == 11:
                print(vertical.format(7,8,9))
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

def checkDiagonal():
    for item in range (0, 3):
        if squares[0] == "x" and squares[4] == "x" and squares[8] == "x":
            return True
        if squares[2] == "x" and squares[4] == "x" and squares[6] == "x":
            return True
        if squares[0] == "o" and squares[4] == "o" and squares[8] == "o":
            return True
        if squares[2] == "o" and squares[4] == "o" and squares[6] == "o":
            return True

def checkStalemale():
    if " " in squares:
        return False
    else:
        return True

def checkWin():
    check1 = checkHorzontal()
    check2 = checkVertical()
    check3 = checkDiagonal()

    sm = checkStalemale()
    if sm == True:
        print("\nNo winners!")
        exit()

    if check1 == True or check2 == True or check3 == True:
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
        while True:
            try:
                userplace = int(input("\nChoose a number between 1 and 9: ")) - 1
                break
            except:
                clear()
                drawGrid()
                print("\nPlease choose an appropriate number!")

        if userplace > 9 or "-" in str(userplace):
            clear()
            drawGrid()
            print("\nPlease choose an appropriate number!")
        else:
            if squares[userplace] == " ":
                squares[userplace] = "x"
                check = False
            else:
                clear()
                drawGrid()
                print("Spot Occupied!")

def game():
    win = False
    clear()
    drawGrid()
    while win != True:
        userPlace()
        clear()
        drawGrid()
        win = checkWin()
        if win != True:
            computerPlace()
            clear()
            drawGrid()
            win = checkWin()
            if win == True:
                winner = "Computer"
        elif win == True:
            winner = "Player"
    print("\nWinner is {}".format(winner))
    exit()

game()