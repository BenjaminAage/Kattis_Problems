
noOfQuestions = int(input())
score = 0
previousAnswer = ""

for i in range(noOfQuestions):
    nextCorrectAnswer = input()

    if nextCorrectAnswer == previousAnswer:
        score += 1
        previousAnswer = nextCorrectAnswer
    else:
        previousAnswer = nextCorrectAnswer

print(score)
