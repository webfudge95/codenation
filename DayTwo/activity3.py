def is_section(num):
    if(num % 4) == 0:
        return True
    else:
        return False

grid = [1,2,3,4,5,6,7,8,9,10,11]

vertical = " {} | {} | {} "
horizontal = "---|---|---"

for item in grid:
    if (is_section(item)) == True:
        print(horizontal)
    else:
        if item == 2:
            print(vertical.format("o","x"," "))
        elif item == 6:
            print(vertical.format("x","x"," "))
        elif item == 10:
            print(vertical.format("o"," "," "))
        else:
            print(vertical.format(" "," "," "))