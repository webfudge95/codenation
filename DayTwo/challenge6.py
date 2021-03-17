
def is_even(num):
    if (num % 2) == 0:
        return True
    else:
        return False

def addition(num1, num2):
    num3 = num1 + num2
    return num3

num1 = int(input("What's the first number: "))
num2 = int(input("What's the second number: "))
num3 = addition(num1, num2)

print("The sum of {} and {} is {}".format(num1, num2, num3))

if is_even(num3):
    print("And that number is even.")
else:
    print("And that number is odd.")