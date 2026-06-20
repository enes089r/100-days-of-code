import random

# Get the range from the player
while True:
    try:
        min_num = int(input("Enter the lower bound of the range: "))
        max_num = int(input("Enter the upper bound of the range: "))
        if min_num >= max_num:
            print("The lower bound must be smaller than the upper bound. Try again.")
            continue
        break
    except ValueError:
        print("Please enter a valid number.")

secret_number = random.randint(min_num, max_num)
guessed_correctly = False
attempts_left = 0

while attempts_left == 0:
    difficulty = input("select the difficulty: easy, medium or hard? ")
    if difficulty == "easy":
        attempts_left += 10
    elif difficulty == "medium":
        attempts_left += 5
    elif difficulty == "hard":
        attempts_left += 3
    else:
        print("invalid input, please try again")

starting_attempts = attempts_left

print(f"\nI picked a number between {min_num} and {max_num}. Find it!\n")

while not guessed_correctly:
    guess = int(input(f"Guess a number ({min_num}-{max_num}): "))
    if guess == secret_number:
        print("You win")
        print("you found it in this many attempts: " + str(starting_attempts - attempts_left + 1))
        guessed_correctly = True
    else:
        print("Wrong guess")
        attempts_left -= 1
        if guess > secret_number:
            print("too high")
            print("attempts remaining: " + str(attempts_left))
        else:
            print("too low")
            print("attempts remaining: " + str(attempts_left))
    if attempts_left == 0:
        print("game over")
        print("secret number was " + str(secret_number))
        exit()
