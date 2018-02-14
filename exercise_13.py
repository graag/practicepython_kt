def get_integer():
    while True:
        try:
            value = int(input("Enter integer value: "))
        except ValueError:
            print("Invalid input!")
        else:
            return value


def fibonacci(count):

    if count <= 0:
        return []
    elif count == 1:
        return [1]
    elif count == 2:
        return [1, 1]
    else:
        fib = [1, 1]
        for x in range(0, count-2):
            fib.append(fib[x] + fib[x+1])
        return fib


print(fibonacci(get_integer()))
