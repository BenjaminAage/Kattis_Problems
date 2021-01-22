
num = int(input())
binary = bin(num)[2:]

new_binary = ""
for i in range(len(binary), 0, -1):
    new_binary += binary[i-1]

print(int(new_binary,2))
