'''
Cheak a password length
'''

password = input("Please type a password: ")

if len(password) < 8:
    print("Password too short")
else:
    print("Password is the correct length") 