author = str(input())
uppercase = ""

for letter in author:
  if letter.isupper():
    uppercase += letter

print(uppercase)