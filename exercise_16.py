import random

codes = list(range(33, 94)) + list(range(97, 126))
length = int(input("Enter password's length: "))

password = ''

for x in range(0, length):
    password += chr(random.choice(codes))

print(password)
