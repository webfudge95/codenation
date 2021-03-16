num = int(input("Please type a number: "))

if (num % 3) == 0 and (num % 7) == 0:
    print("Fizz Buzz")
else:
    if (num % 3) == 0:
        print("Fizz")
    elif (num % 7) == 0:
        print("Buzz")
    else:
        print("He's dead Jim!", num)