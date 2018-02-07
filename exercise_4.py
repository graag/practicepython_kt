number = int(input("Enter number: "))

print("Divisors of " +  str(number) + ":")
for x in range(1, number):
    if number % x == 0:
        print(x)
print(number)