import random


def list_ends(values):
    return [values[0], values[-1]]


a = random.sample(range(100), random.randint(10, 100))
print(a)
print(list_ends(a))