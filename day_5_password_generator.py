import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_letters = []
for _ in range(nr_letters):
    password_letters.append(random.choice(letters))

password_numbers = []
for _ in range(nr_numbers):
    password_numbers.append(random.choice(numbers))

password_symbols = []
for _ in range(nr_symbols):
    password_symbols.append(random.choice(symbols))

password_list = []
password_list.append(password_symbols)
password_list.append(password_letters)
password_list.append(password_numbers)

password_end = []

for _ in range(len(password_numbers) + len(password_symbols) + len(password_letters)):
    chosen_list = random.choice(password_list)

    if len(chosen_list) > 0:
        chosen_char = random.choice(chosen_list)
        password_end.append(chosen_char)
        chosen_list.remove(chosen_char)
    else:
        password_list.remove(chosen_list)

final_password = "".join(password_end)
print(f"Your password is: {final_password}")