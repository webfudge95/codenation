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
    clear()
    print("Simple Noughts and Crosses Game, \n")
    nums = [1,2,3]
    for item in grid:
        if is_section(item) == True:
            print(horizontal)
        elif item == 3 or item == 7 or item == 11:
            a, b, c = nums
            print(vertical.format(a,b,c))
            nums = [x + 3 for x in nums]  
        else:
            if item == 2:
                print(vertical.format(squares[0],squares[1],squares[2]))
            elif item == 6:
                print(vertical.format(squares[3],squares[4],squares[5]))
            elif item == 10:
                print(vertical.format(squares[6],squares[7],squares[8]))
            else:
                print(vertical.format(" "," "," "))

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
    for item in range (1, 3):
        if checkRange(number[0], number[1], number[2]) == True:
            return True
        else:
            number = [x + 3 for x in number]

def checkVertical():
    number = [0, 3, 6]
    for item in range (1, 3):
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
                drawGrid()
                print("\nPlease choose an appropriate number!")

        if userplace > 9 or "-" in str(userplace):
            drawGrid()
            print("\nPlease choose an appropriate number!")
        else:
            if squares[userplace] == " ":
                squares[userplace] = "x"
                check = False
            else:
                drawGrid()
                print("\nSpot Occupied!")

def game():
    drawGrid()
    while True:
        userPlace()
        drawGrid()
        if checkWin() == True:
            print("\nWinner is Player")
            exit()
        computerPlace()
        drawGrid()
        if checkWin() == True:
            print("\nWinner is Computer")
            exit()
    exit()

game()
