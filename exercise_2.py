number = int(input("Type a number: "))

if number % 4 == 0:
    print("Your number is even and dividable by 4.")
elif number % 2 == 0:
    print("Your number is even.")
else:
    print("Your number is odd.")

number1 = int(input("First number: "))
number2 = int(input("Second number: "))
try:
    if number1 % number2 == 0:
        print(str(number1) + " is divisible by " + str(number2) + ".")
    else:
        print(str(number1) + " is not divisible by " + str(number2) + ".")
except ZeroDivisionError:
    print("You can't divide by 0!")