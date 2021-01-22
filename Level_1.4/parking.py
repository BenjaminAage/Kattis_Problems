
tests = int(input())

for i in range(tests):
    stores = int(input())
    distance = [int(x) for x in input().split(" ")]

    print((max(distance) - min(distance)) * 2)