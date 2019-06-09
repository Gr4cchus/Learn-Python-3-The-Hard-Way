
class Room1():

    def enter():
        print("You enter room 1")


class Room2():

    def enter():
        print("You enter room 2")


class Map():

    def __init__(self, starting_room):
        self.starting_room = starting_room
        self.locations = {
            'room1': Room1(),
            'room2': Room2()
        }


class Engine():

    def __init__(self, map):
        self.map = map

    def getmap(self):
        
    def play(self):
        while True:
            print(self.map.locations.get(self.map.starting_room))
            self.map.locations.get(self.map.starting_room)
            

themap = Map('room1')
theengine = Engine(themap)
theengine.play()
