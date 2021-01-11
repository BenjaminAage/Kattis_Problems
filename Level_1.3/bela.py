
dominant = {"A": 11, "K": 4, "Q": 3, "J": 20, "T": 10, "9": 14, "8": 0, "7":0}
notDominant = {"A": 11, "K": 4, "Q": 3, "J": 2, "T": 10, "9": 0, "8": 0, "7":0}

noOfHandsAndSort = input()                  # number of hands and dominant suit of cards
no,sort = noOfHandsAndSort.split(" ")       # split input into two seperate variables
no = int(no) * 4                            # total number of cards, no. of hands * 4

count = 0
totalPoints = 0         # output of game
while count < no:
    nextCard = input()
    
    # If sort is dominant, search that dict and add points to total tally
    if nextCard[1] == sort:
        for key,value in dominant.items():
            if key == nextCard[0]:
                totalPoints += value
    # Else, search the non-dominant dict and add value to total tally
    else:
        for key,value in notDominant.items():
            if key == nextCard[0]:
                totalPoints += value

    count += 1

print(totalPoints)
