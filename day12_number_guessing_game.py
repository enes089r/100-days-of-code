import random

easy_guesses = 10
medium_guesses = 7
hard_guesses = 5


def set_difficulty():
    choice = input("Choose a difficulty (easy/medium/hard): ").lower()
    if choice == "easy":
        return easy_guesses
    elif choice == "medium":
        return medium_guesses
    else:
        return hard_guesses


def check_guess(guess, answer):
    if guess > answer:
        print("Too high.")
        return False
    elif guess < answer:
        print("Too low.")
        return False
    else:
        return True


computer_number = random.randint(1, 100)
attempts_left = set_difficulty()
is_correct = False

while not is_correct and attempts_left > 0:
    print(f"You have {attempts_left} attempts remaining.")
    guess = int(input("Make a guess: "))
    is_correct = check_guess(guess, computer_number)
    attempts_left -= 1

if is_correct:
    print(f"You won! The number was {computer_number}.")
else:
    print(f"You lost. The number was {computer_number}.")