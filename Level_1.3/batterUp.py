N = int(input())
bat = input()
game = bat.split(" ")

count = 0
total = 0
for i in game:
    if int(i) >= 0:
        count += 1
        total += int(i)

print(total / count)
