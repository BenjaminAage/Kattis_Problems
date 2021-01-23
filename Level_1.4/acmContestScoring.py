
correct = {}
incorrect = {}
problem = ""
solved = 0
time = 0

while problem != "-1":
    problem = input()
    if len(problem) < 3:
        break

    problem = problem.split(" ")
    key = problem[1]

    if problem[2] == "right":
        solved += 1

        if key in incorrect:
            value = incorrect.get(key)
            correct[key] = value
            correct[key] += int(problem[0])
        else:
            correct[key] = int(problem[0])
        
    else:
        if key in incorrect:
            incorrect[key] += 20
        else:
            incorrect[key] = 20

for key,value in correct.items():
    time += value

print(str(solved) + " " + str(time))
