
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

    def returnit(self):
        print(self.locations.get(self.starting_room))
        return self.locations.get(self.starting_room)


class Engine():

    def __init__(self, map):
        self.map = map

    def play(self):
        while True:
            print(self.map.returnit)


themap = Map('room1')
# theengine = Engine(themap)
# theengine.play()
print