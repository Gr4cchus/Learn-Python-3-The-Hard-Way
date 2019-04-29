print("What is your favorite genre of music?", end=' ')
your_music_genre = input()

print("What is your favorite artist?\n")    # this doesnt work as you may see
your_artist = input()

print(f"""
Your favorite genre: {your_music_genre}.\n
Your favorite artist: {your_artist}.\n
""")    # Weird formatting

print("On a scale of 1 - 5 with 1 being best how would you rate mozart?")
mozart_rating = int(input())    # make input an integer

print(f"You said mozart is a {mozart_rating}?!")