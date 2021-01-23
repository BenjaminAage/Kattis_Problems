
num = int(input())
junk = input().split(" ")
day = num
lowest = 100000

for i in range(num):
    if int(junk[i]) < lowest:
        day = i
        lowest = int(junk[i])

print(day)
