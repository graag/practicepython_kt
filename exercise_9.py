import random

takes = 0

print("Type 'exit' to end game.")
outer_loop_flag = True


while outer_loop_flag:
    #Generate number
    number = random.randint(1,9)
    print('Try to guess my number!')
    takes = 0
    while True:
        user_input = input("Type your guess: ")
        try:
            user_input = int(user_input)
        except ValueError:
            if user_input == 'exit':
                outer_loop_flag = False
                break
            else:
                print(user_input + " is not a valid input.")
        else:
            takes += 1
            if user_input > number:
                print("My number is lower.")
            elif user_input < number:
                print('My number is higher.')
            else:
                print('Congrats! You have guessed my number in ' + str(takes) +' takes! Let\'s do it again!')
                break
