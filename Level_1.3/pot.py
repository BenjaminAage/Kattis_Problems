N = int(input())

count = 0
for i in range(N):
    num = input()
    real_num = num[0:-1]
    power = num[-1]

    count += int(real_num)**int(power)

print(count)