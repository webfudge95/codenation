'''
first_name = input("What is your first name?: ")
second_name = input("What is your second name?: ")
age = int(input("How old are you? "));
color = input("What is your favourite color: ")

print(f"Your name is {first_name} {second_name}, you are {age} years old, and your favourite colour is {color}")
'''

'''
def user_input():
    breakfast = input("What did you have for breakfast: ")
    dinner = input("What did you have for dinner: ")
    tea = input("What did you have for tea: ")
    return breakfast, dinner, tea

menu = user_input()

print("You had {} for breakfast, {} for dinner and {} for tea".format(menu[0], menu[1], menu[2]))
print("What will you have tomorrow")

menu = user_input()

print("You had {} for breakfast, {} for dinner and {} for tea".format(menu[0], menu[1], menu[2]))

'''

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


