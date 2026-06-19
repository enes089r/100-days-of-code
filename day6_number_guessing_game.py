import random

secret_number = random.randint(0, 100)
guessed_correctly = False

attempts_left = 0

while attempts_left == 0:
    difficulty = input("select the difficulty: easy, medium or hard?")

    if difficulty == "easy":
        attempts_left += 10
    elif difficulty == "medium":
        attempts_left += 5
    elif difficulty == "hard":
        attempts_left += 3
    else:
        print("invalid input, please try again")

starting_attempts = attempts_left

while not guessed_correctly:
    guess = int(input("Guess a number: "))
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
