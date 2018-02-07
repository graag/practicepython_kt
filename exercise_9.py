import random

wins = 0

print("Type 'exit' to end game.")
outer_loop_flag = True


while outer_loop_flag:
    #Generate number
    number = random.randint(1,9)
    print('Try to guess my number!')

    while True:
        user_input = input("Type your guess: ")
        try:
            user_input = int(user_input)
        except ValueError:
            if user_input == 'exit':
                print("You guessed " + str(wins) + " numbers.")
                outer_loop_flag = False
                break
            else:
                print(user_input + " is not a valid input.")
        else:
            if user_input > number:
                print("My number is lower.")
            elif user_input < number:
                print('My number is higher.')
            else:
                print('Congrats! You have guessed my number! Let\' do it again!')
                wins += 1
                break
