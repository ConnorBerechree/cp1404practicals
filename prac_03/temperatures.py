def main():

    MENU = menu()
    choice_decision(MENU)


def choice_decision(MENU):
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            Celsius()
        elif choice == "F":
            Fahrenheit()
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def Fahrenheit():
    fahrenheit = float(input("Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5 / 9
    print("Result: {:.2f} C".format(celsius))


def Celsius():
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    print("Result: {:.2f} F".format(fahrenheit))


def menu():
    MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(MENU)
    return MENU


main()