class Song(object):

        def __init__(self, lyrics):
            self.lyrics = lyrics

        def sing_me_a_song(self):
            for line in self.lyrics:
                print(line)
        
        def print_len(self):
            print("This is how many list entries:", len(self.lyrics))

happy_bday = Song([
"Happy birthday to you",
"I don't want to get sued",
"So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
"With pockets full of shells"])

happy_bday.sing_me_a_song()
happy_bday.print_len()

bulls_on_parade.sing_me_a_song()
bulls_on_parade.print_len()


my_song = ["asd qwe", "zxc asd"]

# my_class = Song

# my_class(my_song).sing_me_a_song()

Song(my_song).sing_me_a_song()
Song(my_song).print_len()