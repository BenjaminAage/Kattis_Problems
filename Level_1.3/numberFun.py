
tests = int(input())

for i in range(tests):
    num = input().split(" ")

    if int(num[0]) + int(num[1]) == int(num[2]):
        print("Possible")
    elif int(num[1]) + int(num[0]) == int(num[2]):
        print("Possible")
    
    elif int(num[0]) - int(num[1]) == int(num[2]):
        print("Possible")
    elif int(num[1]) - int(num[0]) == int(num[2]):
        print("Possible")
    
    elif int(num[0]) * int(num[1]) == int(num[2]):
        print("Possible")
    
    elif int(num[0]) / int(num[1]) == int(num[2]):
        print("Possible")
    elif int(num[1]) / int(num[0]) == int(num[2]):
        print("Possible")
    
    else:
        print("Impossible")