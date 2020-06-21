# Basic version
print("Welcome to ...rock....paper.....scissors.....game")
p1 = input("Enter player1's choice: ")
print("***No Cheating***\n"*20)
p2 = input("Enter player2's choice: ")

print("SHOOT!")
if p1 == p2:
    print("Its a tie!")
elif p1 == 'rock':
    if p2 == 'scissors':
        print("Player 1 wins")
    elif p2 == 'paper':
        print("Player 2 wins")
elif p1 == 'paper':
    if p2 == 'rock':
        print("Player 1 wins")
    elif p2 == 'scissors':
        print("Player 2 wins")
elif p1 == 'scissors':
    if p2 == 'rock':
        print("Player 1 wins")
    elif p2 == 'paper':
        print("Player 2 wins")
else:
    print("Something went wrong")