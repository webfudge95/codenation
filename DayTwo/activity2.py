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