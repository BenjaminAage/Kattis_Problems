
problems = input()
seperated = problems.split(";")

count = 0
for i in range(0, len(seperated)):
    if seperated[i].find("-") != -1:
        begin,end = seperated[i].split("-")
        count += (int(end) - int(begin)) + 1
    else:
        count += 1

print(count)