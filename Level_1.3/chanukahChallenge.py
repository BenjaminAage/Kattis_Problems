
noOfDataSets = int(input())

for i in range(noOfDataSets):
    dataSet = input()
    dataSetNo,noOfDays = dataSet.split(" ")

    noOfCandels = int(noOfDays)
    for i in range(1, int(noOfDays) + 1):
        noOfCandels += i

    print(int(dataSetNo), noOfCandels)

