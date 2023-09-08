print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure")
choice1=input('you are at crossroad, where you want ot go? Type "left" or "right"').lower()
if choice1=="left":
    choice2=input('you have come to lake. There is an island in the middle of lake. Type "wait" to wait for boat. Type "swim" to swim across.').lower()
    if choice2=="wait":
        choice3=input('you arrive at the island unharmed. there is an house of 3 doors .One red, one yelllow, one blue.Which colour do you choose?').lower()
        if choice3=="red":
            print=("It is room full of fire. Game over.")
        elif choice3=="yellow":
            print("You found the treasure!. Game over.")
        elif choice3=="blue":
            print("You enter a room of beats. Game over")
        else:
            print("You chose a door which does not exist. Game over")
    else:
        print("you got attacked by an angry trout. Game over.")
else:
    print("you fell into hole. Game over")
