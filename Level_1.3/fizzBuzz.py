
numbers = input()
x,y,n = numbers.split(" ")

for i in range(1, int(n) + 1):
    if (i / int(x)).is_integer() and (i / int(y)).is_integer():
        print("FizzBuzz")
    elif (i / int(x)).is_integer():
        print("Fizz")
    elif (i / int(y)).is_integer():
        print("Buzz")
    else:
        print(i)
    