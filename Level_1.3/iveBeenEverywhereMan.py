
test_cases = int(input())

for i in range(test_cases):
    trips = int(input())
    print(len(set([input() for j in range(trips)])))
