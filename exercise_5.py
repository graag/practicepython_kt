import random
#Generating first list a
a = []
for x in range(random.randint(15, 30)):
    a.append(random.randint(1, 100))
print(a)

#Generating seconf list b
b = []
for x in range(random.randint(15, 30)):
    b.append(random.randint(1, 100))
print(b)

common = [x for x in a if x in b]
print("Common elements: ")
print(common)
