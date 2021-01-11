
characters = input()

ballCup = 1
for i in range(len(characters)):
    if characters[i] == "A" and ballCup == 1:
        ballCup = 2
    elif characters[i] == "A" and ballCup == 2:
        ballCup = 1
    elif characters[i] == "B" and ballCup == 2:
        ballCup = 3
    elif characters[i] == "B" and ballCup == 3:
        ballCup = 2
    elif characters[i] == "C" and ballCup == 1:
        ballCup = 3
    elif characters[i] == "C" and ballCup == 3:
        ballCup = 1

print(ballCup)
