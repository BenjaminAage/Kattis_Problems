
cards = input()
T = 0
C = 0
G = 0

for i in range(len(cards)):
    if cards[i] == "T":
        T += 1
    elif cards[i] == "C":
        C += 1
    else:
        G += 1

score = (T**2) + (C**2) + (G**2)

while T > 0 and C > 0 and G > 0:
    score += 7
    T -= 1
    C -= 1
    G -= 1

print(score)
