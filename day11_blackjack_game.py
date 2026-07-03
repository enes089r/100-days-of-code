## bilmediğim bir oyun xd 14:20'de başlandı
import random
cards =[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
players_sum = 0
computers_sum = 0



n1 = random.choice(cards)
n2 = random.choice(cards)
computers_sum += (n1+n2)
print(f"Computer's first card is {n1}")

while computers_sum < 17:
    computers_sum += random.choice(cards)

z1 = random.choice(cards)
z2 = random.choice(cards)
players_sum += (z1 + z2)
print(f"Your cards are {z1} and {z2}")

playing = True
while playing and players_sum < 21:
    question = input("Do you want another card? Yes or No: ").lower()
    if question == "yes":
        new_card = random.choice(cards)
        players_sum += new_card
        print(f"New card: {new_card}, total: {players_sum}")
    elif question == "no":
        playing = False
    else:
        print("Invalid answer, please type Yes or No")

print(f"Computer's total is {computers_sum}")

if computers_sum == 21 and players_sum == 21:
    print("It's a draw!")
elif computers_sum == 21 and players_sum != 21:
    print("You lose!")
elif computers_sum != 21 and players_sum == 21:
    print("You win!")
elif computers_sum > 21 and players_sum < 21:
    print("You win!")
elif players_sum > 21 and computers_sum > 21:
    print("Bust! You lose!")
elif computers_sum < 21 and players_sum > 21:
    print("Bust! You lose!")
elif players_sum < 21 and computers_sum < 21:
    if players_sum > computers_sum:
        print("You win!")
    elif computers_sum > players_sum:
        print("You lose!")
    elif computers_sum == players_sum:
        print("It's a draw!")