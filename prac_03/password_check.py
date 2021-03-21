MINIMUM_LENGTH = 5
password = input("Password: ")
while len(password) < MINIMUM_LENGTH:
    print('Too short')
    password = input("Password: ")
else:
    len(password) >=MINIMUM_LENGTH
    print(len(password) * '*')