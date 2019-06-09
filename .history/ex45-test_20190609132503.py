
class Map():
    locations = {
                'room1': Room1(),
                'room2': Room2()
    }
    def __init__(self, starting_room):
        self.starting_room = starting_room
        self.locations = {
            'room1': Room1(),
            'room2': Room2()
        }

    def Room1():

        def enter():
            print("You enter room 1")

    def Room2():

        def enter():
            print("You enter room 2")


class Engine():

    def __init__(self, map):
        self.map = map

    def play(self):
        while True:
            print(self.map.locations)

themap = Map('room1')
theengine = Engine(themap)
theengine.play()
