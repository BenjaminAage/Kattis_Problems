matches = input()
N, W, H = matches.split(" ")

capacity = (int(W)**2 + int(H)**2)
result = capacity**0.5

for i in range (int(N)):
    match_length = int(input())

    if result >= match_length:
        print("DA")
    else:
        print("NE")