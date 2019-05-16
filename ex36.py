from sys import exit, argv
import textwrap

script = argv

def start():
    print(f"""
    Welcome to the jungle.
    You are running {script}.
    Everything typed in input should be lowercase
    Theres a path leading Left, Right, and Forward.
    Which do you choose?
    """)

    choice = input('> ')

    if choice == 'left':
        left_river()
    elif choice == 'forward':
        forward_giant_tree()
    elif choice == 'right':
        right_endless_road()
    else:
        dead("You take the path less taken and stumble around aimlessly with the harsh loud and humid jungle beating you down with every footstep. If the jungle does not deter you, your mind does and you are swallowed by the jungle.")


def dead(why):
    print(why, "Nice try.")
    exit(0)


def did_not_understand_input():
    print("I did not understand your action.")


def left_river():
    print("Traveling down the left path leads you to a river. Water how refreshing.")
    print("After taking a gulp from the source you sit down on a log. Beneath your legs you find an inscription. Peace. ")

    while True:
        print("\nWhat do you want to do now?")
        print("Continue with your 'break' on the log or 'return' back to the start?", sep=' ')
        choice = input('> ')

        if choice == 'break':
            print("After one hour of rest your feel better.")
            continue
        elif choice == 'return':
            print("You get up and begin walking back to the crossroad.")
            start()
        else:
            did_not_understand_input()


def forward_giant_tree():
    """Using conditionals without a loop"""
    print("\nAfter some time you come to a clearing-atleast what the jungle permits-but soon realize it is one giant tree at the center of the clearing that has absorbed all surronding sun light.")
    print("What do you do?\n'Go back' or 'investigate' the mysterious tree?")
    tree_lever = False

    choice = input('> ')

    if choice == 'go back':
        start()
    elif choice == 'investigate':
        print("As you move closer to the center you notice an unusual silhouette near the trunk of the tree...Incredible, it appears to be a stone lever.\nDo you flip the switch? \n'y' or 'n'")
        lever_choice = input('> ')
        if lever_choice == 'y' and not tree_lever:
            tree_lever = True
            print("Nothing fantastic happens")
            forward_giant_tree()
        elif lever_choice == 'y' and tree_lever:
            print("You have already flipped the lever and it will not budge.")
            forward_giant_tree()
        elif lever_choice == 'n' and not tree_lever:
            print("I guess you will never know what this does...")
            forward_giant_tree()
        else:
            forward_giant_tree()
    else:
        did_not_understand_input()
        forward_giant_tree()


def right_endless_road():
    print("""
    \nTraveling down the right path leads to a series of winding trails.
    You seem to lose track of time or otherwise it seems to elapse ever so slowly.
    You wonder for how much more you must endure to reach what ever this destination
    is at the end.
    """)

    while True:
        print("\nWould you like to 'continue' down this trail or turn 'back'?")
        choice = input('> ')

        if choice == 'continue':
            print("Onward you go, not knowing how many steps lay ahead or what rests at the end of this god forsaken jungle.")
            continue
        elif choice == 'back':
            print("You turn back, quite possibly saving your life from this horrendous trail.")
            start()
        else:
            did_not_understand_input()
            continue


start()