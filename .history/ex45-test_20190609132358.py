
class Map():

    

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
