from math import *

measure = input().split(" ")

height = int(measure[0])
angle = int(measure[1])

print(int(ceil(height / sin(radians(angle)))))
