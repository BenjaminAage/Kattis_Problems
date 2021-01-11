
h_items = []
v_items = []

for i in range(3):
    point = input()
    h,v = point.split()

    if h in h_items:
        h_items.remove(h)
    else:
        h_items.append(h)

    if v in v_items:
        v_items.remove(v)
    else:
        v_items.append(v)

print(h_items[0], v_items[0])
