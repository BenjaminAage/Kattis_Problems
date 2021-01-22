
output = []
for i in range(10):
    num = int(input())
    output.append(num % 42)

output = set(output)
print(len(output))
