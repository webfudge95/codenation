def to_celcius(num):
    c = (num - 32) * (5 / 9)
    return c

def to_fahrenheit(num):
    f = (num * (9 / 5)) + 32
    return f

print(to_celcius(185))
print(to_fahrenheit(85))