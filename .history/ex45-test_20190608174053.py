
class Room1():

    def enter():
        print("You enter room 1")


class Room2():

    def enter():
        print("You enter room 2")


class Map():

    locations = {
            'room1': Room1.enter(),
            'room2': Room2.enter()
        }
    def __init__(self, starting_room):
        self.starting_room = starting_room


    def play(self):
        if self.starting_room in self.locations:
            print("success")
            print(self.locations.get(self.starting_room))

start = Map('room1')
start.play()
