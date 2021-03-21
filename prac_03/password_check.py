def main():
    password = get_password()


def get_password():
    MINIMUM_LENGTH = 5
    password = input("Password: ")
    while len(password) < MINIMUM_LENGTH:
        print('Too short')
        password = input("Password: ")
    else:
        digit_count(MINIMUM_LENGTH, password)


def digit_count(MINIMUM_LENGTH, password):
    len(password) >= MINIMUM_LENGTH
    print(len(password) * '*')


main()