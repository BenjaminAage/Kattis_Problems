
num = int(input())

for i in range(num):
    bpm = input()

    b,p = bpm.split(" ")

    abpm = (60*int(b)) / float(p)
    diff = 60 / float(p)
    
    low = abpm - diff
    high = abpm + diff

    print(round(low,4))
    print(round(abpm,4))
    print(round(high,4))
