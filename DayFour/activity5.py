from random import randint

list = ["Hearts", "Diamonds", "Clubs", "Spades"]
card = ""
attempts = 0

def get_choice():
    choice = int(input("Choose a suit: \n1. Hearts \n2. Diamonds \n3. Clubs \n4. Spades \n"))
    while choice > 4 or choice < 1:
        print("Choose an appropriate number")
        choice = int(input("Choose a suit: \n1. Hearts \n2. Diamonds \n3. Clubs \n4. Spades \n"))
    return list[choice - 1]

def get_card():    
    return list[randint(0,3)]

choice = get_choice()

while choice != card:
    attempts += 1
    card = get_card()
    print(card)
    if choice == card:
        print(f"Took {attempts} attempts to complete")
