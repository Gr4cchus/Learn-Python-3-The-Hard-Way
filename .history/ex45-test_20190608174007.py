
class Room1():

    def enter():
        print("You enter room 1")


class Room2():

    def enter():
        print("You enter room 2")


class Map():

    def __init__(self):
        # self.starting_room = starting_room
        self.locations = {
            'room1': Room1.enter(),
            'room2': Room2.enter()
        }

    def play(self):
        if True:
            print("success")
            print(self.locations.get(self.starting_room))

start = Map()
start.play()
