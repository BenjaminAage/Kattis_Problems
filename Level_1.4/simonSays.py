
num = int(input())

for i in range(num):
    sentence = input()

    if sentence[:11] == "Simon says ":
        print(sentence[11:])
        