'''
Simple while loop to generate a random number between 1 and 30 6 times
'''

from random import randint

i = 0

def divisable(num):
    if (num % 7) == 0:
        return True
    else:
        return False

while i < 6:
    rand = randint(1,30)
    if divisable(rand) == True:
        print(f"{rand} is divisable by 7")
    else:
        print(f"{rand} is not divisable by 7")
    i += 1
