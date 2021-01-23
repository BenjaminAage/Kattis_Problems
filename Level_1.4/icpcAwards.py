
teams = int(input())
winners = {}

for i in range(teams):
    nextTeam = input().split(" ")
    found = False

    for key,value in winners.items():
        if key == nextTeam[0]:
            found = True
    
    if found == False:
        winners[nextTeam[0]] = nextTeam[1]

count = 0
for key,value in winners.items():
    if count < 12:
        print(key + " " + value)
        count += 1