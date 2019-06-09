
class Map():

    def __init__(self, starting_room):
        self.starting_room = starting_room
        # self.locations = {
        #     'room1': Room1(),
        #     'room2': Room2()
        # }

    def room1(self):

        def enter():
            print("You enter room 1")

    def room2(self):

        def enter():
            print("You enter room 2")

    # def locations(self):

    #     dict_locations = {
    #         'room1': room1(),
    #         'room2': room2()
    #     }
    #     return dict_locations
    dict_locations = {
            'room1': room1(),
            'room2': room2()
        }


class Engine():

    def __init__(self, map):
        self.map = map

    def play(self):
        while True:
            print(self.map.dict_locations)


themap = Map('room1')
theengine = Engine(themap)
theengine.play()
