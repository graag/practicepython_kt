import random

print("Welcome to the Cows and Bulls Game!")
print("Try to guess a number: ")

random_number = str(random.randint(1000, 9999))

#main loop
tries = 0
while True:
    user_input = input("")
    tries += 1
    #check every digit
    bulls = 0
    cows = 0
    if user_input == random_number:
        print("Correct! It took you " + str(tries) + " tries.")
        break;
    else:
        for i in range(0,4):
            if user_input[i] in random_number:
                if user_input[i] == random_number[i]:
                    cows += 1
                else:
                    bulls +=1
        print(str(cows) + " cows and " + str(bulls) + " bulls")