# advance rock_paper_scissors
from random import randint

print("Welcome to ...rock....paper.....scissors.....game")
player_wins = 0
computer_wins = 0
while True:
    if player_wins == 5:
        print("Congrats...You won the game :)")
        print("Score: player: {} computer: {}".format(player_wins, computer_wins))
        break
    elif computer_wins == 5:
        print("Sorry...You lost...computer wins the game :(")
        print("Score: player: {} computer: {}".format(player_wins, computer_wins))
        break
    p = input("Enter player1's choice: ").lower()
    if p == 'quit' or p == 'q':
        print("You quit")
        break
    rand_num = randint(0, 2)
    if rand_num == 0:
        computer = 'rock'
    elif rand_num == 1:
        computer = 'paper'
    else:
        computer = 'scissors'
    print("Computer plays: {}".format(computer))

    if p == computer:
        print("Its a tie!")
    elif p == 'rock':
        if computer == 'scissors':
            print("Player wins")
            player_wins += 1
        else:
            print("Computer wins")
            computer_wins += 1
    elif p == 'paper':
        if computer == 'rock':
            print("Player wins")
            player_wins += 1
        else:
            print("Computer wins")
            computer_wins += 1
    elif p == 'scissors':
        if computer == 'rock':
            print("Computer wins")
            computer_wins += 1
        else:
            print("Player wins")
            player_wins += 1
    else:
        print("Something went wrong.....enter a valid move")
