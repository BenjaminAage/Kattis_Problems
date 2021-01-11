
numbers = input()

thickness = 4
n,h,v = numbers.split(" ")      # n = length of the sides on the cake 
                                # h = distance of the horizontal cut
                                # v = distance of the vertical cut

piece1 = int(v) * thickness * int(h)                                 # v * thickness * h
piece2 = int(v) * thickness * (int(n) - int(h))                      # v * thickness * (n - h)
piece3 = (int(n) - int(v)) * thickness * int(h)                           # (n - v) * thickness * h
piece4 = (int(n) - int(v)) * thickness * (int(n) - int(h))           # (n - v) * thickness * (n - h)

if (piece1 > piece2) and (piece1 > piece3) and (piece1 > piece4):
    print(piece1)
elif (piece2 > piece1) and (piece2 > piece3) and (piece2 > piece4):
    print(piece2)
elif (piece3 > piece1) and (piece3 > piece2) and (piece3 > piece4):
    print(piece3)
else:
    print(piece4)
