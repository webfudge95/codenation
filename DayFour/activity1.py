'''
Functions to convert Celcius to Fahrenheit and vice versa
'''

def to_celcius(num):
    c = (num - 32) * (5 / 9)
    return c

def to_fahrenheit(num):
    f = (num * (9 / 5)) + 32
    return f

celcius = int(input("Type in Fahrenheit to Celcius: "))
fahrenheit = int(input("Type in Celcius to Fahrenheit: "))

print("Farenheit to Celcius {}".format(to_celcius(fahrenheit)))
print("Celcius to Farenheit {}".format(to_fahrenheit(celcius)))
