
num = int(input())
numList = []

for i in range(num):
    nextNo = int(input())
    numList.append(nextNo)

for j in range(len(numList) - 1, -1, -1):
    print(numList[j])