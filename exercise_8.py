player1 = input("Player1 name: ")
player2 = input("Player2 name: ")
print("Type q to quit")

valid_values = ['ROCK', 'SCISSORS', 'PAPER']

while True:
    #Player1 turn
    player1_choice = input(player1 + "'s turn: ")
    if player1_choice == 'q':
        break
    # Player1 turn
    player2_choice = input(player2 + "'s turn: ")
    if player2_choice == 'q':
        break

    player1_choice = player1_choice.upper()
    player2_choice = player2_choice.upper()

    winner = ''

    if player1_choice not in valid_values or player2_choice not in valid_values:
        print("Invalid input!")
        continue
    else:
        if player1_choice == 'ROCK':
            if player2_choice == 'SCISSORS':
                winner = player1
            else:
                winner = player2
        elif player1_choice == 'SCISSORS':
            if player2_choice == 'PAPER':
                winner = player1
            else:
                winner = player2
        else:
            if player2_choice == 'ROCK':
                winner = player1
            else:
                winner = player2
        print(winner + " won!\nStarting next round.")
