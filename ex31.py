print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?Hmmm, interesting...there seems to be
door #3?""")

doors = input("> ")

if doors == "1":
    print("Theres a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")

elif doors == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")
elif doors == "3":
    print("You have been teleported to a strange black monolith that seems to be nested on the moon orbitting Earth. Oddly you are also now in a space suit. You hear a loud distressing noise, and you see a flashing red alert on your visor.")
    print("Which do you check first?")
    print("1# The noise.")
    print("2# The flashing red alert.")
    
    alert = input("> ")

    if alert == "1":
        print("You check the noise and for a few seconds everything goes whisper quiet. Seconds later your ears start to bleed and you begin to hear the wailings of trillions of sentient beings. You lose consciousness")
    elif alert == "2":
        print("You check the alert which the computer visior begins to elaborate on. You are mystified as the computer has identified a time incongruity suggesting that the time is 2427. Your heart begins to race and you notice the reflection of yourself in your visor. Your skin is withered away, looking more closely to a skull than flesh. Your bones collapase and you lose consciousness")
    else:
        print(f"It looks like you choose {alert}. That was probably smart except you're stranded on a black monolith on another celestial object with no recollection of how you got there. Good luck astronaut.")

else:
    print("You stumble around and fall on a knife and die. Good job!")