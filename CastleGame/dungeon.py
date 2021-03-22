from random import randint
from time import sleep
from os import system

squares = list(" " * 9)
grid = range(1, 12)

def is_section(num):
    if(num % 4) == 0:
        return True
    else:
        return False

vertical = "   {}   |   {}   |   {}   "
horizontal = "-------|-------|-------"    

def clear():
    system("clear")

def speach():
    print("In the dungeon you find a skeleton")
    sleep(2)
    print("The skeleton is sitting at a table in front of a sheet of paper")
    sleep(2)
    print("""Won't you sit with me and play a game?""")
    sleep(2)
    print("You sit at the table, the skeleton asks you to play Noughts and Crosses, it's a popular game amongst skeletons")
    sleep(2)
    print("But he warns you.. Losing may have deadly consequences!")
    sleep(2)
    print("To decide who goes first you play Rock, Paper, Scissors.")

def rps():
    choice = int(input("Type:\n 1. For Rock\n 2. For Paper\n 3. For Scissors\n"))
    compchoice = randint(1, 3)
    
    def getChoice(choice):
        if choice == 1:
            return "Rock"
        elif choice == 2:
            return "Paper"
        elif choice == 3:
            return "Scissors"
    
    if choice < 1 or choice > 3:
        print("Please choose 1, 2 or 3")
        rps()
    else:        
        if choice == compchoice:
            print(f"Player: {getChoice(choice)} .. Skeleton: {getChoice(compchoice)}")
            print("Draw, lets go again!")
            rps()
        elif choice == 1 and compchoice == 2:
            print(f"Player: {getChoice(choice)} .. Skeleton: {getChoice(compchoice)}")
            return False
        elif choice == 2 and compchoice == 3:
            print(f"Player: {getChoice(choice)} .. Skeleton: {getChoice(compchoice)}")
            return False
        elif choice == 3 and compchoice == 1:
            print(f"Player: {getChoice(choice)} .. Skeleton: {getChoice(compchoice)}")
            return False
        elif compchoice == 1 and choice == 2:
            print(f"Player: {getChoice(choice)} .. Skeleton: {getChoice(compchoice)}")
            return True
        elif compchoice == 2 and choice == 3:
            print(f"Player: {getChoice(choice)} .. Skeleton: {getChoice(compchoice)}")
            return True
        elif compchoice == 3 and choice == 1:
            print(f"Player: {getChoice(choice)} .. Skeleton: {getChoice(compchoice)}")
            return True
        

def drawGrid(squares):
    clear()
    nums = [1,2,3]
    for item in grid:
        if is_section(item) == True:
            print(horizontal)
        elif item == 3 or item == 7 or item == 11:
            a, b, c = nums
            print(vertical.format(a, b, c))
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
                drawGrid(squares)
                print("\nPlease choose an appropriate number!")

        if userplace > 9 or "-" in str(userplace):
            drawGrid(squares)
            print("\nPlease choose an appropriate number!")
        else:
            if squares[userplace] == " ":
                squares[userplace] = "x"
                check = False
            else:
                drawGrid(squares)
                print("\nSpot Occupied!")


def order():
    if rps() == True:
        return "player1"
    else:
        return "player2"

def nac():
    speach()
    player = order()
    drawGrid(squares)  
    
    if player == "player1":
        print("Player will go first")
    else:
        print("Skeleton will go first")

    while True:
        if player == "player1":
            userPlace()
            drawGrid(squares)
            if checkWin() == True:
                print("\nWinner is Player")
                return True
            else:
                computerPlace()
                drawGrid(squares)
                if checkWin() == True:
                    print("\nWinner is Computer")
                    return False
        else:
            computerPlace()
            drawGrid(squares)
            if checkWin() == True:
                print("\nWinner is Skeleton")
                return False
            else:
                userPlace()
                drawGrid(squares)
                if checkWin() == True:
                    print("\nWinner is Player")
                    return True
                
