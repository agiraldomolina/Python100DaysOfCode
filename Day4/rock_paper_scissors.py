# The traditional rock paper scissors game 😉
import random
import os
os.system('cls')
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
play_images=[rock, paper, scissors]
options = ['rock', 'paper','scissors']
player = int(input('What do you choose? 1 for rock, 2 for paper, 3 for scissors: '))
if player !=1 or player !=2 or player!=3:
    print('Please choose a number between 1 and 3')
    exit()
print(f"You chose: {options[player-1]}")
print(play_images[player-1])
player = options[player-1]
computer = random.randint(1, 3)
print(f"Computer chose: {options[computer-1]}")
print(play_images[computer-1])
computer = options[computer-1]
if player == 'rock':
    if computer =='scissors':
        print('You win!')
    elif computer == 'paper':
        print('You lose!')
    else:
        print('Draw!')
elif player == 'paper':
    if computer == 'rock':
        print('You win!')
    elif computer =='scissors':
        print('You lose!')
    else:
        print('Draw!')

elif player =='scissors':
    if computer == 'paper':
        print('You win!')
    elif computer == 'rock':
        print('You lose!')
    else:
        print('Draw!')

