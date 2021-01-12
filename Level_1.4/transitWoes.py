
startTime,classTime,transitRoutes = input().split(" ")
startTime,classTime,transitRoutes = int(startTime), int(classTime), int(transitRoutes)

walkTime = input().split(" ")
busTime = input().split(" ")
intervalForBus = input().split(" ")

totalTime = startTime

for i in range(len(walkTime)):
    totalTime += int(walkTime[i])

for j in range(len(busTime)):
    totalTime += int(busTime[j])

for k in range(len(intervalForBus)):
    if int(intervalForBus[k]) > int(walkTime[k]):
        totalTime += (int(intervalForBus[k]) - int(walkTime[k]))


if totalTime <= classTime:
    print("yes")
else:
    print("no")
