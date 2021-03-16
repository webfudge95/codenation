last = input("Type in a word: ")

if last[-1] == last[0]:
    print(f"Your word {last} is a match")
else:
    print(f"The letters of {last} do not match")