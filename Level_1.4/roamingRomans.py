
englishMile = 5280
romanMile = 4854

num = float(input())

conversion = (englishMile / romanMile) * num
conversion = round(conversion * 1000, 0)
conversion = int(conversion)

print(conversion)
