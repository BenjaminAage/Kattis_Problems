
word = input()
length = len(word)

count = 0
confirm = "false"
for i in range(0, length - 1):
    if (word[count] == word[count + 1]) and (word[count] == "s"):
        print("hiss")
        confirm = "true"
        break
    count += 1

if confirm == "false":
    print("no hiss")
