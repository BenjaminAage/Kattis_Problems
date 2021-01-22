
num = int(input())
bills = input().split(" ")

expenses = 0
for i in range(num):
    if int(bills[i]) < 0:
        expenses += abs(int(bills[i]))

print(expenses)
