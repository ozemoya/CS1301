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

#Write your code below this line 👇
import random 
print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
user_input = int(input())
computer_input = random.randint(0, 2)
if user_input == 0:
    print(rock)
elif user_input == 1:
    print(paper)
elif user_input == 2:
    print(scissors)

if computer_input == 0:
    print(rock)
elif computer_input == 1:
    print(paper)
elif computer_input == 2:
    print(scissors)

if user_input == computer_input:
    print("It's a draw")
elif user_input == 0 and computer_input == 1:
    print("You lose")
elif user_input == 0 and computer_input == 2:
    print("You win")
elif user_input == 1 and computer_input == 0:
    print("You win")
elif user_input == 1 and computer_input == 2:
    print("You lose")
elif user_input == 2 and computer_input == 0:
    print("You lose")
elif user_input == 2 and computer_input == 1:
    print("You win")    