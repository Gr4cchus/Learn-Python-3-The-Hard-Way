
class Scenes(object):

    # def __init__(self):
    #     # self.starting_room = starting_room
    #     # self.locations = {
    #     #     'room1': Room1(),
    #     #     'room2': Room2()
    #     # }

    def start(self):
        print("You are at the start")
        print("Where would you like to go")

    def room1(self):
        print("You enter room 1")

    def room2(self):
        print("You enter room 2")
    
    def finish(self):
        print("You have finished")
        exit(0)
    
    def locations(self)
        map_list = [
            'room1'
        ]

    # def locations(self):
    #     dict_locations = {
    #         'room1': room1(),
    #         'room2': room2()
    #     }
    #     return dict_locations
    # dict_locations = {
    #         'room1': room1(),
    #         'room2': room2()
    # }


# class Locations(Scenes):

#     pass

#     def map(self):
#         dict_locations = {
#             'room1': room1(),
#             'room2': room2()
#         }
#         return dict_locations

# class Engine():

#     def __init__(self, map):
#         self.map = map

#     def play(self):
#         while True:
#             # a = self.map.dict_locations
#             print('yes')

thescenes = Scenes()
# thelocations = Locations()

# thedict = thelocations.map()

# while True:
#     print("loop")
#     thelocations.map.dict_locations.get('room1')

thescenes.start()
