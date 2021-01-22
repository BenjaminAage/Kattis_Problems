
sentence = input().split(" ")
sentence.sort()

while len(sentence) > 1:
    if sentence[0] == sentence[1]:
        print("no")
        break
    else:
        sentence.pop(0)

if len(sentence) == 1:
    print("yes")
