import random
from game_data import data

def value_of(account):
    name = account["name"]
    follower = account["follower_count"]
    return name, follower

def compare_a_and_b(choice, follower_of_a, follower_of_b):
    if follower_of_a > follower_of_b:
        if choice == "a":
            print("That's correct!")
            return True
        else:
            print("That's wrong.")
            return False
    else:
        if choice == "a":
            print("That's wrong.")
            return False
        else:
            print("That's correct!")
            return True


game_still_continue = True
account_a = random.choice(data)
account_b = random.choice(data)

while account_a == account_b:
    account_b = random.choice(data)

while game_still_continue:
    name_of_a, follower_of_a = value_of(account_a)
    name_of_b, follower_of_b = value_of(account_b)

    choice = input(f"What's your choice, {name_of_a}(A) or {name_of_b}(B)? Select a or b: ").lower()
    is_correct = compare_a_and_b(choice, follower_of_a, follower_of_b)

    if not is_correct:
        game_still_continue = False
    else:
        if follower_of_a > follower_of_b:
            account_a = account_a
        else:
            account_a = account_b

        account_b = random.choice(data)
        while account_a == account_b:
            account_b = random.choice(data)
