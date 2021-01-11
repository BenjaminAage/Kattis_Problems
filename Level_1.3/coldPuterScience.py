
noOfTempCollected = int(input())
temps = input()
measuredTemps = temps.split()

count = 0
for m in measuredTemps:
    if int(m) < 0:
        count += 1

print(count)
    