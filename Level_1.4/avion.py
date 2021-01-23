
locate = "FBI"
found = []

for i in range(1,6):
    blimp = input()

    while len(blimp) >= 3:
        if blimp[0:3] == locate:
            found.append(i)
        blimp = blimp[1:]


if found == []:
    print("HE GOT AWAY!")
else:
    for i in found:
        print(i, end=" ")
    