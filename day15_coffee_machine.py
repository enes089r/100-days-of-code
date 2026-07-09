def money_conversion():
    added_penny = int(input("How many pennies are you inserting? "))
    added_nickel = int(input("How many nickels are you inserting? "))
    added_dime = int(input("How many dimes are you inserting? "))
    added_quarter = int(input("How many quarters are you inserting? "))
    added_dollar = added_penny * 0.01 + added_nickel * 0.05 + added_dime * 0.10 + added_quarter * 0.25
    return added_dollar


def base_material():
    base_coffee = int(input("How much coffee to load into the machine? "))
    base_water = int(input("How much water to load into the machine? "))
    base_milk = int(input("How much milk to load into the machine? "))
    base_money = int(input("How much starting money to load into the machine? "))
    return base_coffee, base_water, base_milk, base_money


def price_calculator(coffee_choice):
    if coffee_choice == "espresso":
        price = 1.5
    elif coffee_choice == "latte":
        price = 2.5
    elif coffee_choice == "cappuccino":
        price = 3.0
    return price

def get_needed(coffee_choice):
    if coffee_choice == "espresso":
        return 50, 18, 0
    elif coffee_choice == "latte":
        return 200, 24, 150
    elif coffee_choice == "cappuccino":
        return 250, 24, 100

def can_you_buy_coffee(added_dollar, price):
    if added_dollar >= price:
        enough_money = True
    else:
        enough_money = False
    return enough_money


def needed_material_and_final_material(coffee_choice, base_coffee, base_water, base_milk):
    if coffee_choice == "espresso":
        needed_water = 50
        needed_coffee = 18
        needed_milk = 0
    elif coffee_choice == "latte":
        needed_water = 200
        needed_coffee = 24
        needed_milk = 150
    elif coffee_choice == "cappuccino":
        needed_water = 250
        needed_coffee = 24
        needed_milk = 100

    base_coffee -= needed_coffee
    base_water -= needed_water
    base_milk -= needed_milk
    return base_coffee, base_water, base_milk


def current_money_calculator(price, base_money):
    current_money = base_money + price
    return current_money

def remainder_of_money_calculator(price, added_dollar):
    remainder_of_money = added_dollar - price
    return remainder_of_money

base_coffee, base_water, base_milk, base_money = base_material()

while True:
    coffee_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if coffee_choice == "off":
        break

    elif coffee_choice == "report":
        print(f"Water: {base_water}ml")
        print(f"Milk: {base_milk}ml")
        print(f"Coffee: {base_coffee}gr")
        print(f"Money: {base_money} dollar")
        continue

    else:
        price = price_calculator(coffee_choice)
        needed_water, needed_coffee, needed_milk = get_needed(coffee_choice)

        if base_water < needed_water or base_milk < needed_milk or base_coffee < needed_coffee:
            print("Sorry there is not enough material in machine")
            continue

        added_dollar = money_conversion()
        enough_money = can_you_buy_coffee(added_dollar, price)
        if not enough_money:
            print("Sorry that's not enough money. Money refunded.")
            continue

        base_coffee, base_water, base_milk = needed_material_and_final_material(coffee_choice, base_coffee, base_water,
                                                                                base_milk)
        base_money = current_money_calculator(price, base_money)
        remainder = round(remainder_of_money_calculator(price, added_dollar), 2)
        print(f"Here is your {coffee_choice}. Enjoy! Change: {remainder} dollar")