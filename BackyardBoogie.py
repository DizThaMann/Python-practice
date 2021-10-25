# Welcome to Backyard Boogie Barbershop Simulation
# Add a name for the barber
# health = 100
# print("my health", health)
# is_alive = True
# player1 = input("What is your name?: ")
# comp1 = input("Choose the barber's name: ")
# print("Welcome " + player1 + "!" " This is the Backyard Boogie Barbershop Simulation. ")
# print("Your goal is to get your hairline fixed, because your last appointment didn't go so well, but to do this,"
#       "you'll need to successfully win the backyard boogie dance off.")

# set up three scenarios and adjust the health variable
# based on users choices and check the health throughout the game.
def create_comp1():
    comp1 = input("Choose the barber's name: ")
    return comp1



def display_introduction(player1):
    """ Write and introduction describing the user's mission """
    print("\nWelcome " + player1 + " to Backyard Boogie Barbershop....")
    print("Trust me homie, this place is filled with nonsense and odd situations if you ")
    print("know what I mean, but no worries, I'm sure with your intellect, you'll see it through.\n")


def hairline_frustration(health):
    """ This is the first scenario """
    print("You wake up from a good night sleep, brush your teeth, and hair, and put on a fly outfit.")
    print("Fully dressed, you look in the mirror only to see that your hairline is like Lebron James receding hairline.")
    print("In fact, it's ten times worse. It's like the M in McDonalds.")
    print("Beyond upset, you decide to take the trip to your barber and demands that he fixes your hairline.")
    print("So you leave the house,visibly upset and get in your car, but realize that there isn't any gas.")
    print("Realizing this, you yell at the top of your lungs in the car, and decide to walk.")
    print("As you start your journey, you hear some music and cheering, you look and immediately called out to battle.")
    print("You know for a fact that you are an Okay dancer but not that good, but you contemplate.")
    player_choice = input("What's your decision(Dance or keep moving)? ")
    if player_choice == "Dance":
        print("You quickly accept the challenge, and give an incredible performance, and win after a long vote.")
        print("But that battle causes you to miss the bus, thus putting you in a bad spot.")
        print("Congratulations on winning the battle, but you lost 10 health points from your decision.")
        health = health - 40
    elif player_choice == "Keep moving":
        print("You decide that you need to keep moving, those guys are there all the time, and you can battle anytime.")
        print("As you move on, you make it to the bus stop right as the bus arrives, keeping you on schedule.")
        print("You have gained 9 health points for keeping up with your schedule.")
        health = health + 25
    else:
        print("Your command makes absolutely no sense, I'm speechless and utterly frustrated. So you are now lost.")
        print("You successfully lost 11 health points for being lost.")
        health = health - 29
    return health


# Now that the first scenario is done, it is time for the second scenario.
# Which has to do with awkward situations.


def busride_awkwardness(health):
    """ This is the second scenario """
    print("As your on the bus minding your own business, you start thinking about what you want to say to the barber.")
    print("As you make your way to the barbershop, you realize that you haven't ate breakfast and are hungry.")
    print("You are nearing your stop when you remember there is a Denny's across from the shop, so you decide to wait.")
    print("You notice a man staring at you." "Not sure what he wants, and feeling nervous, you decide to stare back.")
    print("So the whole bus ride, you're both staring at each other looking weird.")
    print("Finally, as the man is about to get off at his stop, he says," " Troubled water only goes under the bridge"
          " if that bridge leads to forgiveness.")
    print(" Feel every piece of that.")
    print("As he leaves you decide to stop him, and try to out weird him, and decide contemplate.")
    print("You can engage him or leave him be.")
    player_choice = input("What do you decide(Engage or leave)? ")
    if player_choice == "Engage":
        print("You decide to take him on with a series of just strange replies of your own.")

        print("Well you can throw change in a wishing well, but you can't go wishing for people to change.")

        print("The strange man, looks on shocked and replies," " "
              " Birds of a feather stay together, no matter the weather"
          " we getting cheddar, Forever! ")
        print("You then respond with," 
              " You know the only reason the woodchuck doesn't know how much wood he can chuck is" 
              " because the woodchuck lacks self confidence.")
        print("The strange man then leaves in disbelief, and confusion.")

        print("Great you successfully out weirded him, gained 8 health points, and outside the shop.")
        health = health + 16
    elif player_choice == "Leave":
        print("I see that you decided not to engage.")
        print("You lost 12 health points, now you're staring trying to make sense of what he said, "
              " making you look crazy.")
        health = health - 30
    else:
        print("Sir, your command sadly makes no sense, that was a terrible decision.")
        print("You just lost 13 health points.")
        health = health - 36
    return health


# Having completed this awkward mission/scenario, it's time to get down to business
# The player has finally made it to his destination.


def money_issues(health, comp1, player1):
    """ This is the third scenario """
    print("You finally make it to the barbershop and spot the barber that messed up your hairline.")
    print("You walk up to the barber visibly angry and yell out," "Hey" + comp1 + "!")
    print("As he turns to face you, you angrily take off your hat to reveal your terrible hairline.")
    print("As you do so, you notice other customers start laughing, you then decide to tell him off.")
    print(" Look here " + comp1 + "!" " I demand you fix my hairline, "
                                  "I look like a chia pet, my head looks like a maze!")
    print("I had a date, and my date laughed all night, and I haven't talked to her since!")
    print("The barber, then replies, look," + player1 + "," 
                                                        " I gave you exactly what you wanted, it ain't free to fix.")
    print("WHAT!!?!  I paid 50 dollars for this!" "I don't have any money left over, what am I suppose to do?")
    print("Look," + player1 + "," "there is a way to get some money, there is this backyard boogie dance off.")
    print("Winner gets 100, all I ask is a percentage for pointing you in the right direction.")
    print("A PERCENTAGE??!!!" " We should just take this outside and settle it then!")
    print("Now look here," + player1 + "," " this ain't what you want, "
                                       " I was a pro boxer in my day, but it's up to you.")
    player_choice = input("What is do you chose(Fight or Dance)? ")
    if player_choice == "Fight":
        print("You put up a good fight, but your lack of boxing skills causes you to be open to an uppercut.")
        print("You are now on the ground seeing stars, thinking you're in heaven.")
        print("You just lost 30 health points from that beating.")
        health = health - 30
    elif player_choice == "Dance":
        print("You make your way to the dance off and enter the competition.")
        print("You easily beat two dancers until it's time to face the champ.")
        print("He immediately starts break-dancing, wooing the crowd, until it's your turn.")
        print("You amaze the crowd with your amazing krump and pop-locking skills, securing your win.")
        print("Congratulations, you won and have been rewarded 20 health points.")
        health = health + 29
    else:
        print("At this point, I don't even know why you're here.")
        print("You just lost 24 health points.")
        health = health - 24
    return health


# Now it's time for the final scenario
# This the end

def home_stretch(comp1, player1):
    """ This the final scenario """
    print("You make it back to the shop with your earnings, but very reluctant into giving partial.")
    print("You hesitantly give up your share, and " + comp1 + "begins to cut your hair.")
    print("He tries to make small talk but you ignore him, having completely blocked him out.")
    print("Alright " + player1 + "," "I'm all done hope you like it, take a look.")
    print("You get to the mirror and admire yourself, you look and feel like a new man.")
    print("You feel like you deserve to be on the cover of GQ magazine, you thank him and start making your way out.")
    print("But as you make your way out, you notice the dance champ, walking in, he greets " + comp1 + "so you wait.")
    print("You then see "  + comp1 +  "give a share of the money to the dance champ as they both laugh and shake hands.")
    print("It is then you realize that you have been played.")

def display_title():
    print("\n\n\t*** Welcome Backyard Boogie Barbershop ***\n")

# checking users health is important.

def check_user_health(health, is_alive):
    """
    If the user-health drops below 0 Health points during the game
    set the is_alive variable to False
    """
    print("\nYour current Health is " + str(health))
    if health <= 0:
        print("Well it's the afterlife for you my friend.")
        is_alive = False
    elif health >= 80:
        print("You're still in this, I believe in you, get back up.")
        is_alive = True
    else:
        print("You've clearly been through worse.")
        is_alive = True


def get_player_name():
    """ Get and return the player's name """
    player1 = input("What is your name?: ")
    return player1




def main():
    """ The main function is the best practice to start a program from."""
    """The main function should be the driver/control of the program"""
    is_alive = True
    health = 100
    play_again = True
    while play_again == True:
        display_title()
        player1 = get_player_name()
        display_introduction(player1)
        comp1 = create_comp1()
        health = hairline_frustration(health)
        check_user_health(health, is_alive)
        if is_alive == True:
            health = busride_awkwardness(health)
        check_user_health(health, is_alive)
        if is_alive == True:
            health = money_issues(health,comp1, player1)
        check_user_health(health, is_alive)
        if is_alive == True:
            home_stretch(comp1, player1)
        check_user_health(health, is_alive)
        if is_alive == True:
            print("You won  " + player1 + " and have been promoted to certified salmonella.")
        else:
            print("WOW, I did not expect that terrible ending, such a shame.")
        print("\n\t***Game Over***\n\n")
        # ask if player would like to play again.
        player_choice = input("\nWould you like to play again Sir? (y/n): ")
        # Evaluate the player's choice
        if player_choice == "y":
            var = play_again == True
            var = is_alive == True


        # if __name__ == "__main__":
        #     """This checks if there is a main function in this game
        #             If there is, then it starts with the main function."""
main()


















