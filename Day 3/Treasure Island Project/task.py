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
money = 60
print("Welcome to Treasure Island.")
print(f"Your mission is to find the treasure. You have K{money} (Kurkos) in spending money. Spend it wisely")

direction = input("Where would you like to go next? Left or right: ").lower()
if direction == "left":
    print("Good choice!\nAfter what seems like a long walk, you come to a weathered shore.")
    print("You've heard before that these waters contain mystical creatures. Dangerous or not, you do not know.")
    print("On the other hand, you know that boatmen sometimes parade the waters, but you have no idea when one might come by next.")
    get_across = input("What do you want to do now? Swim or wait: ")
    if get_across == "wait":
        print("You know better than to take silly risks, especially where the supernatural is concerned.")
        print("You wait for about 20 minutes and just as you are about to give up and swim, you see a little canoe approach.")
        print("You can barely make out their face as they draw near, a withered hand outstretched, expecting payment upfront.")
        pay_decision = (input("The fare to cross is K50 (Kurkos). Do you have enough to pay? Y or N: "))
        if pay_decision == "Y":
            money -= 50
            print(f"You grudgingly pay the hefty fee. Pocketing the remaining K{money} you have left, you get into the canoe.")
        else:
            money -= 60
            print(f"The boatperson snatches what money you did have in your hand, leaving you with nothing! They motion for you to get in.")
        print("On the other side of the marina, you get out of the canoe, your pocket a lot lighter than before. Hopefully you won't need to spend anything.")
        print("You walk north for about a mile when you come to an odd-looking tavern with 3 doors. It's not obvious which one is the main front door.")
        door_decision = input("Which door do you walk through? Red, blue or yellow: ").lower()
        if door_decision == "yellow":
            print("You walk through the yellow door. There is nothing there other than an old slots machine.")

    else:
        print("Mystical creatures? Probably an old wives' tale, you think to yourself. You lunge into the waters.")
        print("You swim for a few minutes when you see ripples in your peripheral vision.")
        print("Your breath catches. You hope you imagined it, but not long after you feel a sharp bite on your ankle!")
        print("You don't even get to the point of screaming before whatever creature attacked you begins to pull you beneath the waters.")
        print("Your life flashes before you and you know this is the end of the line.")
else:
    print("You walk on ahead after turning. You can swear there are eyes watching you but you can't be too sure.")
    print("As you look behind you, you don't notice that you've stepped into a carefully hidden trap!")
    print("3 heavily built men with face tattoos appear beside you holding spears. They don't look too friendly.")
    print("Your whole leg is stuck. They tie you up easily. You know in your heart, this is the end.")