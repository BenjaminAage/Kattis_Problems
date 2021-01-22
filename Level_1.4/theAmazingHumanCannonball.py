import math


numOfTestCases = int(input())

for i in range(numOfTestCases):
    testCase = input().split(" ")           # testCase[0] = ball's initial velocity in m/s
                                            # testCase[1] = angle given in degrees
                                            # testCase[2] = distance from cannon to the wall
                                            # testCase[3] = height of lower edge on wall
                                            # testCase[4] = height of upper edge on wall

    x = float(testCase[2]) / (float(testCase[0]) * math.cos(math.radians(float(testCase[1]))))
    y = float(testCase[0]) * x * math.sin(math.radians(float(testCase[1]))) - 0.5 * 9.81 * (pow(x,2))

    # vertical safety margin of 1 meter, both below and above the point 
    # where the ball's trajectory crosses the centerline of the wall
    if (y > (float(testCase[3]) + 1)) and (y < (float(testCase[4]) - 1)):
        print("Safe")
    else:
        print("Not Safe")
