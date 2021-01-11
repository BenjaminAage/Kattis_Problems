
costOfSeed = input()
numberOfLawns = input()


sizeOfLawns = 0
count = 0
while count < int(numberOfLawns):
    size = input()
    num = size.split(" ")
    
    sizeOfLawns += float(num[0]) * float(num[1])
    count += 1


costOfLawnSeeding = float(costOfSeed) * sizeOfLawns
print(costOfLawnSeeding)
