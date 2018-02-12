import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print("Set: " + str(set([x for x in a if x in b])))


myList = []
for x in a:
    if x in b and x not in myList:
        myList.append(x)
print("For-in: " + str(myList))

print("Random lists")
a = [random.randint(0,100) for x in range(0, random.randint(20,40))]
b = [random.randint(0,100) for x in range(0, random.randint(20,40))]
print("a: " + str(a))
print("b: " + str(b))
print("Set: " + str(set([x for x in a if x in b])))

myList = []
for x in a:
    if x in b and x not in myList:
        myList.append(x)
print("For-in: " + str(myList))
