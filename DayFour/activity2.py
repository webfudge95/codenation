'''
Example of a for loop
'''

films = ["Lord of the rings", "Ghostbusters", "Back to the future", "The Hobbit"]

def check_film(film):
    if film.lower() == "ghostbusters":
        return True
    else:
        return False

for film in films:
    if check_film(film) == True and film == films[2]:
        print("Yay! GhostBusters")
    elif check_film(film) == True and film != films[2]:
        print("Yay! Ghostbusters, but not the right place")
    else:
        print("Boo! We want ghostbusters")
