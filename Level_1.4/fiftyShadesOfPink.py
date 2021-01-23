
num = int(input())
count = 0

for i in range(num):
    found = "False"
    package = input().lower()

    while found == "False":
        if package[0:4] == "rose" or package[0:4] == "pink":
            count += 1
            found = "True"
        else:
            package = package[1:]

            if package == "":
                found = "True"

if count > 0:
    print(count)
else:
    print("I must watch Star Wars with my daughter")
