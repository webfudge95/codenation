def times(num1, num2):
    num3 = num1 * num2
    return num3

def times_table():
    num = int(input("Choose a number: "))
    for i in range(13):
        print(f"{num} x {i} = {num * i}")

yes = True

while yes == True:
    times_table()
    choice = input("Would you like to try another number Y/N: ")
    if choice.lower() == "n" or choice.lower() == "no":
        yes = False
    while choice.lower() != "y" and choice.lower() != "yes" and choice.lower() != "n" and choice.lower() != "no":
        print("Please answer yes or No")
        choice = input("Would you like to try another number Y/N: ")
