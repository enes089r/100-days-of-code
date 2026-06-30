a = 1
auction_dict = {}

while a == 1:
    answer = input("Is anyone else joining? Answer yes or no: ")
    if answer == "yes":
        name = input("What is your name? ")
        given_money = input("How much money are you bidding? ")
        print("\n" * 100)
        auction_dict[name] = int(given_money)
    elif answer == "no":
        a -= 1
        print(auction_dict)
        winner = max(auction_dict, key=auction_dict.get)
        print(f"Winner: {winner}, Amount given: {auction_dict[winner]}")