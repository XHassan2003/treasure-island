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
*******************************************************************************''')
print("Welcome to Treasure Island!")
print("Your mission is to find the tresure. Lets begin!")
choice1 = input("Your are in the middle of jungle. You have two options left/right. Where you want to go?\n ").lower()
if choice1 == "left" :
  print("Good Job!")
  choice2 = input("Now you come across an island there are two ways you either wait for the boat to come or swim across the lake. Type boat/swim:\n").lower()
  if choice2 == "boat":
    print("Great work!")
    choice3 = input("You are arrived at the island unharmed. Here are three doors one is red, one is yellow and one is blue. You have three options Red/Yellow/Blue:\n").lower()
    if choice3 == "yellow":
      print("Congrats. You won it!")
    elif choice3 == "red":
      print("Burned by fire. Game over!")
    elif choice3 == "blue":
      print("Eaten by beasts. Game over!")
    else:
      print("You choose a door that doesnt exist. Game over!")
  else:
    print("Eaten By sharks. Game over!")
else:
  print("You fall into the hole. Game over!")