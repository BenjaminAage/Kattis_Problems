#  a building (symbol ‘#’)
# a parked car (symbol ‘X’) 
# a free parking space (symbol ‘.’)

square = input().split(" ")
row = int(square[0])
column = int(square[1])

for i in range(row):
    lot = input()