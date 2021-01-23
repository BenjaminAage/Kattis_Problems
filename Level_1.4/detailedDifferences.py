
num = int(input())

for i in range(num):
    string1 = input()
    string2 = input()

    length = len(string1)
    output = ""
    
    for i in range(length):
        if string1[i] == string2[i]:
            output += "."
        else:
            output += "*"

    print(string1)
    print(string2)
    print(output)
