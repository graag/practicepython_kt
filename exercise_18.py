import random

class GameHistory():

    def __init__(self):
        self.history=[]

    def add(self, cows, bulls, guess):
        self.history.append((guess, cows, bulls))

    def __str__(self):
        pattern = '{:6}{:6}{:6}{:6}\n'
        result = pattern.format('No.','Input','Cows','Bulls')
        guess_number = 0
        for data in self.history:
            guess_number += 1
            result += pattern.format(str(guess_number), data[0], str(data[1]), str(data[2]))
        return result


def generate_cows_bulls_counter(number):
    #This function return generated function.
    def count_cows_bulls(guess):
        #This function returns tuple of cows&bulls (cows, bulls).
        bulls = 0
        cows = 0
        for i in range(0,4):
            if guess[i] in number:
                if guess[i] == number[i]:
                    cows += 1
                else:
                    bulls +=1
        #Return tuple.
        return (cows, bulls)
    #Return function.
    return count_cows_bulls    


def validate_input(number):
    try:
        int(number)
    except ValueError:
        return False
    else:
        return len(number) == 4 and number[0] != '0' and len(set(number)) == 4


def generate_4digit_random_number():
    return_value = ''
    while len(return_value) < 4:
        random_value = str(random.randint(0, 9))
        if random_value in return_value or (random_value == '0' and len(return_value) == 0):
            continue
        else:
            return_value += random_value
    return return_value


if __name__=='__main__':
    print("Welcome to the Cows and Bulls Game! Type in 'hist' to see conveniently formatted game history and 'exit' to stop the game.")
    print("Try to guess a number: ")

    random_number = generate_4digit_random_number()
    counter = generate_cows_bulls_counter(random_number)
    tries = 0
    game_history = GameHistory()
    #main loop
    while True:
        user_input = input("")

        if user_input.upper() == 'HIST':
            print(game_history)
            continue
        elif user_input.upper() == 'EXIT':
            print('exiting')
            break

        while not validate_input(user_input):
            user_input = input("Error! Remember to type 4-digit number with unique digits!\n")

        tries += 1
        #check
        cows,bulls = counter(user_input)
        game_history.add(cows, bulls, user_input)
        if(cows == 4):
            print("You won! It took you " + str(tries) + " tries!")
            print(game_history)
            break
        else:
            print(str(cows) + " cows and " + str(bulls) + " bulls.")