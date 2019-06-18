
class Scenes(object):

    # def __init__(self):
    #     # self.starting_room = starting_room
    #     # self.locations = {
    #     #     'room1': Room1(),
    #     #     'room2': Room2()
    #     # }
    map_list = [
            'room1',
            'room2',
            'finish'
        ]

    def start(self):
        print("You are at the start")
        print("Where would you like to go")
        self.locations()

    def room1(self):
        print("You enter room 1")
        print("Where would you like to go")
        self.locations()

    def room2(self):
        print("You enter room 2")
        print("Where would you like to go")
        self.locations()
    
    def finish(self):
        print("You have finished")
        exit(0)
    
    def locations(self):
        print("def locations:", self.cmd)
        for i in self.cmd:
            print(i)

    cmd = {
        'room1': room1,
        'room2': room2,
        'finished': finish
    }

# class Map(Scenes):

#     a = Scenes()

#     map_dict = {
#         'room1': a.room1(),
#         'room2': a.room2(),
#     }

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
while True:
    action = input("> ")
    if action in thescenes.cmd:
    # if thescenes.cmd.get(action):
        print("success")
        # trying to test user input on calling a function from a list or dict.
        # thescenes.map_list[action]()
        thescenes.cmd.get(action](thescenes)
