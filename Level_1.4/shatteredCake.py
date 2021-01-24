
widthOfCake = int(input())
numberOfPieces = int(input())

totalSizeOfEachPiece = 0

for i in range(numberOfPieces):
    pieceOfCake = input().split(" ")
    totalSizeOfEachPiece += (int(pieceOfCake[0]) * int(pieceOfCake[1]))

lengthOfCake = int(totalSizeOfEachPiece / widthOfCake)
print(lengthOfCake)
