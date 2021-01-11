
tests = int(input())

for i in range(tests):
    output = 1
    num = int(input())

    for j in range(num):
        output += j * output

    if len(str(output)) == 1:
        print(output)
    else:
        output = str(output)
        print(output[-1])
