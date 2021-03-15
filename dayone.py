'''
    A simple Python program which takes user input to output a grid from a given size.
'''

size = int(input("Please type in a number for the size of the grid: "))
section = (size // 3) - 1
height = section // 2
str = ""

'''
*   First the program gets user input using the input function contained in the size variable 
*   The section variable determines the size of the sections of the grid, it takes the size 
    variable and divides it by 3 taking away 1 for the "|" character.
*   To create a more equally sized grid the height variable is half of the section variable,
    the width is exactly the same so no seperate variable is defined.
*   When dividing // is used to divide the number to a interger rather than a floating point,
    which would happen if just one / was used.
*   An empty str is used to make sure join method works properly.
'''


def printHorizontal():
    line = ("-" * section, "|", "-" * section, "|", "-" * section)
    
    print(str.join(line))

def printVertical():

    line = (" " * section, "|", " " * section, "|", " " * section)
    i = 1
    print(str.join(line))
    
    while (i < height):
        print(str.join(line))
        i = i + 1
    
'''
*   Two functions are defined in this part which, when called, will output horizontal and 
    vertical lines respectively.
*   The printHorizontal function creates a string variable called line by combining output 
    from a bit of string manipulation:
        First it repeats "-" x the section variable.
        Then it inserts a "|".
        It then repeats this process twice creating the  ---|---|---  effect.
        A join method is used in the print function to join each of these parts into a single 
        string
*   The printVertical function works very similar to the printHorizontal function with two
    major differences, first instead of printing "-" in the line variable it prints " " instead.
    Secondly, the printVertical function must print multiple lines. To do this a while loop is 
    used to repeat the function until a certain condition is met.
*   The condition used is while: the variable i is less than height, repeat the function. i is
    defined at the start of the printVertical function as 1, and each time the function repeats
    it adds one to the i variable using i = i + 1, for example if height was 3 the loop would 
    continue twice before the condition is met.
'''
    
printVertical()
printHorizontal()
printVertical()
printHorizontal()
printVertical()

'''
*   This part uses the defined functions in order to print the grid to the terminal, first it
    creates the top lines, then prints a horizontal line, this repeats til the grid is drawn
'''
