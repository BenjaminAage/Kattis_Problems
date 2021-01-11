
numberOfFaces = input()
n,m = numberOfFaces.split(" ")          # Two dices
outcomes = {}

# Create dictionary with possible outcomes of dices
for i in range(1, int(n) + int(m) + 1):
    nextNo = str(i)
    outcomes[nextNo] = 0

# Get the outcome of dices, and add to key values in dict
for j in range(1, int(n) + 1):
    for k in range(1, int(m) + 1):
        result = j + k

        for key,value in outcomes.items():
            if int(key) == result:
                outcomes[key] = value + 1

# Find the highest value(s) in dictionary, and output their keys
highestRate = 0
returnValues = []
for key,value in outcomes.items():
    if value > highestRate:
        highestRate = value
        returnValues = [int(key)]
    elif value == highestRate:
        returnValues.append(int(key))
    else:
        continue

for item in range(len(returnValues)):
    print(returnValues[item])
