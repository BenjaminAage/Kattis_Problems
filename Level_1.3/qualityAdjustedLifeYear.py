N = int(input())

count = 0.0
for i in range(N):
    qaly = input()
    num1, num2 = qaly.split(" ")
    count += float(num1) * float(num2)

print(count)