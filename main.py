import random

def raffle():
    list = ['rock', 'paper', 'scissors']
    return random.choice(list)

print('Hello! Welcome to Rock, Paper, and Scissors!')
playermode = input('What mode do you want to play in? (Computer or Player)\n')
if playermode.lower() == 'computer':
    while True:
        playermove = input('What is your choice? (rock, paper, scissors)\n')
        opponentmove = raffle()
        if opponentmove == 'rock':
            print('The opponent chose rock!')
        elif opponentmove == 'paper':
            print('The opponent chose paper!')
        elif opponentmove == 'scissors':
            print('The opponent chose scissors!')

        if opponentmove == playermove:
            print('You tied!')

        elif opponentmove == 'rock' and playermove == 'paper':
            print('You win!')

        elif opponentmove == 'rock' and playermove == 'scissors':
            print('You lose!')

        elif opponentmove == 'paper' and playermove == 'rock':
            print('You lose!')

        elif opponentmove == 'paper' and playermove == 'scissors':
            print('You win!')

        elif opponentmove == 'scissors' and playermove == 'rock':
            print('You win!')

        elif opponentmove == 'scissors' and playermove == 'paper':
            print('You lose!')


        repeat = input('Do you want to play again? (yes, no)\n')  
        if repeat.lower() == 'no':
            break




if playermode.upper() == 'PLAYER':
    while True:
        player1move = input('What is the first player choice? (rock, paper, scissors)\n')
        player2move = input('What is the second player choice? (rock, paper, scissors)\n')


        if player1move == player2move:
            print('You tied!')

        elif player1move == 'rock' and player2move == 'paper':
            print('Player 2 wins!')

        elif player1move == 'rock' and player2move == 'scissors':
            print('Player 1 wins!')

        elif player1move == 'paper' and player2move == 'rock':
            print('Player 1 wins')

        elif player1move == 'paper' and player2move == 'scissors':
            print('Player 2 wins!')

        elif player1move == 'scissors' and player2move == 'rock':
            print('Player 2 wins!')

        elif player1move == 'scissors' and player2move == 'paper':
            print('Player 1 wins')


        repeat = input('Do you want to play again? (yes, no)\n')  
        if repeat.lower() == 'no':
            break
