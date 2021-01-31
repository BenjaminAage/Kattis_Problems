
num = ""
theSet = set()
count = 1

while num != 0:
    num = int(input())

    if num == 0:
        break
    
    for i in range(num):
        name = input()
        theSet.add(name)

    print("SET", count)
    
    for j in theSet:
        print(j)

    count += 1
