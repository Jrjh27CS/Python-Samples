from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take?")

    choice = input("> ")
    how_much = int(choice)
    if how_much < 500:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy scum!")

def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        choice = input("> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through the door now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("You pushed the bear too far.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I have no idea what you mean....")

def dead(why):
    print(why, "Good job!")
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door by a single torch on the wall.")
    print("Would you like to enter?")

    choice = input("> ")
    if choice == "yes":
        bear_room()
    elif choice == "no":
        print("Maybe next time then!")
        exit(0)
    else:
        dead("It was a simple yes or no question dum dum...")

start()
