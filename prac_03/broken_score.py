score = float(input("Enter score: "))
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
