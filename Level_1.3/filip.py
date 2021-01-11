
numbers = input()
no1,no2 = numbers.split(" ")

returnNo1 = ""
returnNo2 = ""

for i in range(len(no1)-1, -1, -1):
    returnNo1 += no1[i]

for j in range(len(no2)-1, -1, -1):
    returnNo2 += no2[j]


if int(returnNo1) > int(returnNo2):
    print(int(returnNo1))
else:
    print(int(returnNo2))
