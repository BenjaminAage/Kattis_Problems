
highNo = int(input())
harshadNo = highNo

found = "false"
while found == "false":
    strNo = str(harshadNo)
    total = 0

    for i in strNo:
        total += int(i)

    checkNo = harshadNo / total
    if checkNo.is_integer() == True:            # if isinstance(checkNo,int):
        found = "true"
    else:
        harshadNo = harshadNo + 1


print(harshadNo)
