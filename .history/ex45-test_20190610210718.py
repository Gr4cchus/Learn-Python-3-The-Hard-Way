
class Map():

    def __init__(self, starting_room):
        self.starting_room = starting_room
        # self.locations = {
        #     'room1': Room1(),
        #     'room2': Room2()
        # }

    def room1(self):
        print("You enter room 1")

    def room2(self):
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

    def returnroom():
        return self.dict_locations(starting_room)


class Engine():

    def __init__(self, map):
        self.map = map

    def play(self):
        while True:
            # a = self.map.dict_locations
            print('yes')


themap = Map('room1')
theengine = Engine(themap)
theengine.play()
