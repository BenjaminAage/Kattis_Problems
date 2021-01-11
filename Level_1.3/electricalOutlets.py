
noOfTestCases = int(input())

for i in range(noOfTestCases):
    description = input()

    strips = int(description[:2])       # First number in string is the number of power strips
    outlets = description[2:]           # Rest of numbers are the number of outlets in each strip
    outlets = outlets.split()           # Convert string to list of numbers (outlets)

    sumOfOutlets = 0
    for num in outlets:
        sumOfOutlets += int(num)

    print(sumOfOutlets - strips + 1)
