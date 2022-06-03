# ROCK, PAPER , SCISSORS GAME
import random

options = ['R' , 'P' , 'S']

game_over = False
while not game_over:
    print("WELCOME TO THE ROCK, PAPER, SCISSORS GAME.")
    print("\n'R' stands for 'rock'\n'P' stands for 'paper'\n'S' stands for 'scissors'")
    
    # The while loop will keep running and asking the user to make a choice until the user enters a VALID option
    proceed = False
    while not proceed:
        player_choice = input("\nKindly select your choice (R / P / S): ").upper()
        if player_choice not in options:
            print("\nInvalid option. Make another choice!")
        else:
            proceed = True
            
    computer_choice = random.choice(options)
    print(f"\nPlayer: ({player_choice}) \nCPU: ({computer_choice})")
    

    result = ''
    # The code below compares the choices and picks a winner
    if player_choice == 'R' and computer_choice == 'S':
        result = 'Player'

    elif computer_choice == 'R' and player_choice == 'S':
        result = 'Computer'

    elif player_choice == 'P' and computer_choice == 'R':
        result = 'Player'

    elif computer_choice == 'P' and player_choice == 'R':
        result = 'Computer'

    elif player_choice == 'S' and computer_choice == 'P':
        result = 'Player'

    elif computer_choice == 'S' and player_choice == 'P':
        result = 'Computer'

    else:
        result = 'Tie'

    # The code below checks to see if result is a Tie and restarts the game if True or else the game ends.
    
    if result != 'Tie':
        print(f"\n{result} wins the game!")
        print('\nTHANK YOU FOR PLAYING THE GAME.')
        game_over = True
    else:
        print("TIE!! Game will be restarted.")
