time = input()
Hours, Minutes = time.split(" ")

if int(Minutes) <= 44:
    if int(Hours) != 0:
        Hours = int(Hours) - 1
        Minutes = int(Minutes) + 15
    else:
        Hours = 23
        Minutes = int(Minutes) + 15
else:
    Minutes = int(Minutes) - 45


print(str(Hours) + " " + str(Minutes))
