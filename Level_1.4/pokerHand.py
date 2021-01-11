
cards = input().split(" ")
count = {"A": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0, "T": 0, "J": 0, "Q": 0, "K": 0}

for card in cards:
    for key,value in count.items():
        if key == card[0]:
            count[key] += 1

print(max(count.values()))
