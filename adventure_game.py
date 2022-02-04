# This is a funny game that I made to learn how to use if statements and elif statements.
# In this game, you have to choose between two paths MATCH or FLASHLIGHT
print("Welcome to the Adventure Game!")
print("You are in a dark room.")
print("There is a door to your right and left.")
print("Which one do you take? ")
print ("MATCH 'left' or 'FLASHLIGHT 'right'?")
match = input("Match or flashlight? ")
match = match.lower()
# This is the first if statement.
if match == "match":
    print("You have chosen the match.")
    print("You pick up the match and strike it, and for an instant, the forest around you is illuminated. You see a large grizzly bear, and then the match burns out. Do you want to RUN, or HIDE behind a tree?")
    run = input("Run or hide? ")
    run = run.lower()
    if run == "run":
        print("You run, and the bear catches up to you. You are dead.")
    elif run == "hide":
        print("You hide behind a tree, and the bear is still there. You are dead.")
    else:
        print("You have chosen an invalid option. You are dead.")
# This is the second if statement.
elif match == "flashlight":
    print("You have chosen the flashlight.")
    print("You pick up the flashlight and turn it on. You see the pathway lit up in front of you, but you thought you also heard something off to the side. Do you want to FOLLOW the path or LOOK in the trees for the thing that made the noise?")
    follow = input("Follow or look? ")
    follow = follow.lower()
    if follow == "follow":
        print("You follow and you are saved. You win!")
    elif follow == "look":
        print("You look and your eyes are blinded by the trees. You are dead.")
    else:
        print("You have chosen an invalid option. You are dead.")
print("The End.")
print(" ")

# This is the end of the program.
# I hope you enjoyed it!
# If you have any questions, please contact me at: rudyravelin@gmailcom
# Thank you!
# Rudy
# This part I made for funny purposes.
print("Thanks for playing!")
print(" ")
print("Created by: Rudy Ravelin")
print("Date: 02/04/2022")
print("Version: 1.0")
print("Copyright (c) 2022 Rudy Ravelin")
print("All rights reserved.")
print(" ")
print("This game is not for sale.")
print("This game is not for resale.")
print("Game created for educational purposes only.")
print("This game is not for profit.")
print("rudyravelin@gmail.com for more information.")

