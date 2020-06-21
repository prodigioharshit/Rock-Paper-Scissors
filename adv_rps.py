# advance rock_paper_scissors
from random import randint

print("Welcome to ...rock....paper.....scissors.....game")
p = input("Enter player1's choice: ").lower()
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
    else:
        print("Computer wins")
elif p == 'paper':
    if computer == 'rock':
        print("Player wins")
    else:
        print("Computer wins")
elif p == 'scissors':
    if computer == 'rock':
        print("Player wins")
    else:
        print("Computer wins")
else:
    print("Something went wrong.....enter a valid move")
