
tints = [int(x) for x in input().split(" ")]

if tints[0] == tints[1] == 0:
    print("Not a moose")
elif tints[0] == tints[1]:
    print("Even " + str(tints[0] * 2))
else:
    if tints[0] > tints[1]:
        print("Odd " + str(tints[0] * 2))
    else:
        print("Odd " + str(tints[1] * 2))
        