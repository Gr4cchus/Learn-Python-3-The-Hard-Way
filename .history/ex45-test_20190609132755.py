
class Map():

    def __init__(self, starting_room):
        self.starting_room = starting_room
        # self.locations = {
        #     'room1': Room1(),
        #     'room2': Room2()
        # }

    def Room1(self):

        def enter():
            print("You enter room 1")

    def Room2(self):

        def enter():
            print("You enter room 2")

    def locations(self):

        locations = {
            'room1': Room1(),
            'room2': Room2()
        }


class Engine():

    def __init__(self, map):
        self.map = map

    def play(self):
        while True:
            print(self.map.locations)
            self.map.locations.get(star)

themap = Map('room1')
theengine = Engine(themap)
theengine.play()
