sentence = input()

whitespace = 0.0
lowercase = 0.0
uppercase = 0.0
symbols = 0.0

for i in sentence:
    if i == "_":
        whitespace += 1
    elif i.islower():
        lowercase += 1
    elif i.isupper():
        uppercase += 1
    else:
        symbols += 1


print(float(whitespace / len(sentence)))
print(float(lowercase / len(sentence)))
print(float(uppercase / len(sentence)))
print(float(symbols / len(sentence)))
