print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

first_turn = input("Which side want you turn? Just l or r as answer please").upper()

if first_turn == "R":
    print("you are lost because there was a lion")

elif first_turn == "L":
    action = input("concragt, you get rid of lion. now, you saw a see. do you want to swim or just wait? you can anser it as wait or swim").upper()
    if action == "SWIM":
        print ("you chocked, game over")
    elif action == "WAIT":
        door_choice = input("you saw 3 door around the forest, do you want go anyone or keep to wait").upper()
        if door_choice == "WAIT":
            print("unfortunately lion found you")

        else:
            which_door = input("from which door do you want to keep, you can answer it as r, l or m").upper()
            if which_door == "M":
                print("concragt, you win")
            else:
                print("the tiger ,which wait for you behind the door, hunted you.")

