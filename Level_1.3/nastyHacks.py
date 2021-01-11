
num = int(input())

for i in range(num):
    costAnalysis = input()
    noAdvert,doAdvertRev,costOfAdvert = costAnalysis.split(" ")

    noAdvert = int(noAdvert)
    doAdvertRev = int(doAdvertRev)
    costOfAdvert = int(costOfAdvert)


    if noAdvert > (doAdvertRev - costOfAdvert):
        print("do not advertise")

    elif noAdvert < (doAdvertRev - costOfAdvert):
        print("advertise")

    elif noAdvert == (doAdvertRev - costOfAdvert):
        print("does not matter")
