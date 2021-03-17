password = 1234
balance = "1899"
withdrawing = True

def checkpass(pin, real):
    if pin == real:
        return True


def security():
    userpass = int(input("Please type the password: "))

    check = checkpass(userpass, password)
    if check == True:
        return True
    else:
        print("Incorrect password")
        exit()
    
while withdrawing == True:
    secure = security()
    if secure == True:
        print("Your balance is {}".format(balance))

