
contestant = 0
score = 0

for i in range(5):
    grades = [int(x) for x in input().split()]
    new_score = 0

    for j in grades:
        new_score += j

    if score < new_score:
        contestant = i + 1
        score = new_score

print(str(contestant) + " " + str(score))