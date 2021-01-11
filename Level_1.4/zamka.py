
minNo = int(input())        # L  --> (1 >= X <= 10000)
maxNo = int(input())        # D  --> (1 >= X <= 10000) && (L <= D) 
sumNo = int(input())        # X  --> (1 >= X <= 36)

N = maxNo   # min number in interval equal to X (sumNo)
M = minNo   # max number in interval equal to X (sumNo)

for i in range(minNo, maxNo + 1):
    listOfNo = []
    for j in str(i):
        listOfNo.append(j)
    
    # Check if sum of numbers in integer (i) is equal to X
    numSum = 0
    for j in listOfNo:
        numSum += int(j)

    # If sum of number in integer is equal to X, check if it is lower than N, or higher then M
    if numSum == sumNo:
        if i < N:
            N = i
        if i > M:
            M = i


print(N)
print(M)
