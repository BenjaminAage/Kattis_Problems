
tests = int(input())

for i in range(tests):
    count = 0
    growth = input().split(" ")

    while len(growth) != 1:
        if growth[0] == growth[1] and growth[0] == "1":
            growth.pop(0)
        else:
            if int(growth[1]) > (int(growth[0]) * 2):
                count += (int(growth[1]) - (int(growth[0]) * 2))
                growth.pop(0)
            else:
                growth.pop(0)
    print(count)
