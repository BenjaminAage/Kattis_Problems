
info = input().split(" ")
safety = int(info[0])
events = int(info[1])

denied = 0
noOfPeople = 0

for i in range(events):
    nextEvent = input().split(" ")

    if nextEvent[0] == "enter":
        if safety >= (noOfPeople + int(nextEvent[1])):
            noOfPeople += int(nextEvent[1])
        else:
            denied += 1

    elif nextEvent[0] == "leave":
        noOfPeople -= int(nextEvent[1])

print(denied)
