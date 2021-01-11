X = int(input())        # Megabytes per month
N = int(input())        # Number of months


count = 0
for i in range(N):
    P = int(input())
    count += P

print((X * N) - count + X)
