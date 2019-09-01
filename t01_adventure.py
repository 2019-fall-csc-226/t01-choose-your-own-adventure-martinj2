######################################################################
# Author: Scott Heggen       TODO: Change this to your names
# Username: heggens               TODO: Change this to your usernames
#
# Assignment: T01: Choose Your Own Adventure
#
# Purpose: To create a choose-your-own-adventure style game.
# Each "twist" in the story is from a different group. The resulting story
# will either be incoherently random, or entertainingly "Mad Lib" like.
# Either way, it should be fun!
######################################################################
# Acknowledgements:
#   Original Author: Dr. Scott Heggen
#
#   Inspired by https://www.cs.hmc.edu/twiki/bin/view/CS5/Week0ChoiceProblem
######################################################################
from time import sleep

 
delay = 1.0          # change to 0.0 for testing/speed runs; larger for dramatic effect!
dead = False         # You start out not dead, which is good.

# Asks the user to input their name.
username = input("What do they call you, unworthy adversary? ")

#########################################################################################################
# The following is the first part of the story. Don't change this section.
print()
print("Welcome,", username, ", to the labyrinth.")
sleep(delay)
print("Before you lies two paths. One path leads to treasures of unimaginable worth.")
print("The other, certain death. Choose wisely.")
print()
sleep(delay * 2)
print("You are in a dark cave. You can see nothing.")
print("Staying here is certainly not wise. You must find your way out.")
print("\n")
sleep(delay)

#########################################################################################################
# This is an example chapter. Your story will follow a similar structure.
# You will learn more by NOT copy and pasting this section. Write your section on your own, and when you get stuck,
# refer to this code to help you get unstuck. Of course, raise your hand if you get really stuck.

direction = input("Which direction would you like to go? [North/South/East/West]")

if direction == "North":
    # Good choice!
    print("You are still trapped in the dark, but someone else is there with you now! I hope they're friendly...")
    sleep(delay)
elif direction == "South":
    # Oh... Bad choice
    print("You hear a growl. Not a stomach growl. More like a big nasty animal growl.")
    sleep(delay)
    print("Oops. Turns out the cave was home to a nasty grizzly bear. ")
    print("Running seems like a good idea now. But... it's really, really dark.")
    print("You turn and run like hell. The bear wakes up to the sound of your head bouncing off a low stalactite. ")
    print("He eats you. You are delicious.")
    dead = True
else:
    # Neutral choice
    print("You're in another part of the cave. It is equally dark, and equally uninteresting. Please get me out of here!")
    sleep(delay)

if dead == True:
    print("Oh no! You died. Better luck next time! Try again by hitting the green play button. ")
    quit()

#########################################################################################################
print("You see a dim light glowing behind a loose boulder. Do you choose to "
      "investigate?")
Choice=input("[Yes/no/leave]")
sleep(delay)

if Choice == "Yes":
    print ("You place your hand against the boulder and it dissipates into the air like fine mist. Behind it you see "
           "a giant sword bigger than most men.")
    sleep(delay)
    print("A giant humanoid creature enters your view and begins to grab the sword.")
    sleep(delay*2)
    print("He swings the sword in your direction causing the timid ceiling to collapse in between you saving yourself "
          "from the giant beast. ")
    print("You are safe for now, and you begin to search for a way out..")
    #
    #
    sleep(delay)
elif Choice == "no":
    print("You choose to hastily run away from the boulder and you begin to lose your footing.")
    sleep(delay)
    print("You trip and fall forward breaking your neck in the most boring possible fashion")
    dead = True
else:
    print("You decide against your gut and move away from the glowing boulder.")
    sleep(delay)
    print("You leave the cave by following the sounds of wilderness outside. You begin to hear some disgruntled shuffling in the cave as you leave.")
    if dead == True:
        print("You Died! Try again.")
    quit()



#########################################################################################################

# The following is the end of the story. Don't change this section, unless you really want to
# (though it may not be used in the final story. Or will it...)
print("Look at that! You made it to the end of the story without dying! ")
print("Congratulations... now go play again and find an interesting way to perish. ")
print("Try again by hitting the green play button.")
