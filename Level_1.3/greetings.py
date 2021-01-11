
greeting = input()
returnGreeting = ""

count = 0
for i in greeting:
    if i == "e":
        returnGreeting += "ee"
    else:
        returnGreeting += i

print(returnGreeting)
