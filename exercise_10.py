import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print(set([x for x in a if x in b]))

print("Random lists")
a = random.sample(range(100), random.randint(20,40))
b = random.sample(range(100), random.randint(20,40))
print("a: " + str(a))
print("b: " + str(b))
print("Result: " + str([x for x in a if x in b]))
