pieces = input().split(" ")
pieces_int = [int(i) for i in pieces]
missing_pieces = []

for index, value in enumerate(pieces_int):
  if index == 0:
    value1 = 1 - value
    missing_pieces.append(value1)
  elif index == 1:
    value2 = 1 - value
    missing_pieces.append(value2)
  elif index == 2:
    value3 = 2 - value
    missing_pieces.append(value3)
  elif index == 3:
    value4 = 2 - value
    missing_pieces.append(value4)
  elif index == 4:
    value5 = 2 - value
    missing_pieces.append(value5)
  elif index == 5:
    value6 = 8 - value
    missing_pieces.append(value6)

print(" ".join(str(i) for i in missing_pieces))

