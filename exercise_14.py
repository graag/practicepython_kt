def list_with_loop(values):
    result = []
    for x in values:
        if x not in result:
            result.append(x)
    return result


def list_with_set(values):
    return list(set(values))


a = [1, 1, 1, 2, 2, 2, 3, 4, 5, 6, 7, 7, 7, 8, 8]
print("Initial values: ")
print(a)

print("With loop:")
print(list_with_loop(a))

print("With set:")
print(list_with_set(a))
