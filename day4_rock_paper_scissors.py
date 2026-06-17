rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
(rock)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
(paper)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
(scissors)
'''

import random

choice_list = [scissors, paper, rock]

computers_choice = random.choice(choice_list)

users_choice= input("Rock, paper or scissors? Type your choice: ").lower()

if users_choice == "rock":
    print("your choice" + rock)
elif users_choice == "paper":
    print("your choice" + paper)
elif users_choice == "scissors":
    print("your choice" + scissors)
else:
    print("Invalid choice! Maybe see you later :(")
    exit()

print("computer's choice" + computers_choice)

if computers_choice == scissors:
    if users_choice == "scissors":
        print("it's a draw")
    elif users_choice == "rock":
        print("you win")
    elif users_choice == "paper":
        print("you lost")
elif computers_choice == paper:
    if users_choice == "scissors":
        print("you win")
    elif users_choice == "rock":
        print("you lost")
    elif users_choice == "paper":
        print("it's a draw")
elif computers_choice == rock:
    if users_choice == "scissors":
        print("you lost")
    elif users_choice == "rock":
        print("it's a draw")
    elif users_choice == "paper":
        print("you win")



