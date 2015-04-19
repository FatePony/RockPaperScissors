# A rock paper scissors simulator
# Extreme RPS simulation action
def RPS():
    '''Contains outer loop and start'''
    print('\nWelcome to Rock, Paper, Scissors\n')
    from random import choice
    wins = 0
    losses = 0
    ties = 0
    total_played = 0
    while True:
        menu = input('Choose (p)lay, (s)tats or (quit):\n  ')
        if menu == 'p':
            total_played += 1
            player = input('Choose (r)ock, (p)aper, or (s)cissors:\n    ')
            computer = choice(['r','p','s'])
            print('Computer chooses',computer)
            if player == 'r':
                if computer == 'r':
                    print('It is a tie')
                    ties += 1
                elif computer == 'p':
                    print('Computer wins')
                    losses += 1
                elif computer == 's':
                    print('You win!')
                    wins += 1
            elif player == 'p':
                if computer == 'r':
                    print('You Win!')
                    wins += 1
                elif computer == 'p':
                    print('It is a tie')
                    ties += 1
                elif computer == 's':
                    print('Computer wins')
                    losses += 1
            elif player == 's':
                if computer == 'r':
                    print('Computer wins')
                    losses += 1
                elif computer == 'p':
                    print('You win!')
                    wins += 1
                elif computer == 's':
                    print('It is a tie')
                    ties += 1
            else:
                print('Choice not recognized')
        elif menu == 's':
            print('Current Stats:\nTotal games played: {}\nWins: {}\nLosses: {}\nTies: {}'.format(total_played,wins,losses,ties))
        elif menu == 'q':
            print('Final stats:\nTotal games played: {}\nWins: {}\nLosses: {}\nTies: {}'.format(total_played,wins,losses,ties))
            break
        else:
            print('Invalid command, try again.')

RPS() #Runs the game
