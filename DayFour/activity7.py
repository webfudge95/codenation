'''
A simple equasion to find prime numbers
'''


id = 1

def is_prime(num):
    for i in range(2, num):
        if (num % i) == 0 and i != num:
            return False
    return True

while id < 101:
    if is_prime(id) or id == 1:
        print(f"{id} is Prime")
    id += 1
    
