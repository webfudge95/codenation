time = range(0, 24)

home = "I'm at Home"
commuting = "I'm commuting"
work = "I'm at work"

for i in time:
    if i == 8 or i == 18:
        print("{}:00, {}".format(i, commuting))
    elif 9 <= i <= 17:
        print("{}:00, {}".format(i, work))
    else:
        print("{}:00, {}".format(i, home))