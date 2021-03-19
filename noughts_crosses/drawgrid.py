from os import system
from random import randint

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

def drawGrid(squares):
    clear()
    print("Simple Noughts and Crosses Game, \n")
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
