def main():

    score = ask_score()
    score_decision(score)


def ask_score():
    score = float(input("Enter score: "))
    return score


def score_decision(score):
    if score < 50:
        print("Bad")
    elif score > 100:
        print("Invalid score")
    elif score > 50:
        print("Passable")
    elif score > 90:
        print("Excellent")
    else:
        print("Invalid Score")


main()
