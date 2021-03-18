'''
A simple equasion to find prime numbers to a given value
'''

def is_prime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True

id = 1

while id < 101:
    if is_prime(id) or id == 1:
        print(f"{id} is Prime")
    id += 1
    
