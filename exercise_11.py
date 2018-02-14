def get_integer():
    while True:
        try:
            value = int(input("Enter integer value: "))
        except ValueError:
            print("Invalid input!")
        else:
            return value


def get_divisors(value):
    result = []
    for x in range(1, value+1):
        if value % x == 0:
            result.append(x)
    return result


number = get_integer()
if len(get_divisors(number)) == 2:
    print("It is a prime number.")
else:
    print("It is not a prime number.")
