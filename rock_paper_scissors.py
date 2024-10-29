import random

#Introduces the game
print('===================\nRock Paper Scissors\n=================== \n1) ✊\n2) ✋\n3) ✌️\n')

#Assigns values to player and computer variables
player = int(input('Select a  number between 1 and 3: '))
computer = random.randint(1,3)

#Tells player what they chose
if player == 1:
    print('You chose: ✊')
elif player == 2:
    print('You chose: ✋')
elif player == 3:
    print('You chose: ✌️')

#Tells player what CPU chose
if computer == 1:
    print('CPU chose: ✊')
elif computer == 2:
    print('CPU chose: ✋')
elif computer == 3:
    print('CPU chose: ✌️')

#Decides either win, loss or draw
if player == 1 and computer == 1:
    print('It is a draw! You both chose Rock.')
elif player == 2 and computer == 2:
    print('It is a draw! You both chose Paper.')
elif player == 3 and computer == 3:
    print('It is a draw! You both chose Scissors.')
elif player == 1 and computer == 2:
    print('You lose! The computer chose Paper.')
elif player == 1 and computer == 3:
    print('You win! The computer chose Scissors.')
elif player == 2 and computer == 1:
    print('You win! The computer chose Rock.')
elif player == 2 and computer == 3:
    print('You lose! The computer chose Scissors.')
elif player == 3 and computer == 1:
    print('You lose! The computer chose Rock.')
elif player == 3 and computer == 2:
    print('You win! The computer chose Paper.')
else:
    print('Choose a number between 1 and 3')
