
words = input().split()

if words[0][-1] == "e":
    print(words[0] + "x" + words[1])
elif (words[0][-1] == "a") or (words[0][-1] == "i") or (words[0][-1] == "o") or (words[0][-1] == "u"):
    print(words[0][:-1] + "ex" + words[1])
elif words[0][-1] == "x" and words[0][-2] == "e":
    print(words[0] + words[1])
else:
    print(words[0] + "ex" + words[1])
    