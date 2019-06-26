import random
# # class Foo:
# #     answer = 42

# # f1 = Foo()
# # f2 = Foo()

# # print(f1.answer)
# # print(f2.answer)
# # # both will print 42

# # f1.answer = 84
# # Foo.answer = 21

# # print(f1.answer)  # 84
# # print(f2.answer) # 21



# class Foo:
#     def __init__(self):
#         self.answer = 42

# f1 = Foo()
# f2 = Foo()
# # f2.answer = 4000
# Foo.answer = 21
# # f1.answer = 2000

# print(f1.answer)
# print(f2.answer)
# # both will print 42 still


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
        print("def locations:", self.map_list)
        for i in self.map_list:
            print(i)

    cmd = {
        'room1': room1,
        'room2': room2,
    }

    def guessing_game(self):
        n = random.randint(1,4)
        print("Oh no a mini-game.")
        print("Guess the number between 1-4. To pass")
        answer = 0
        while answer =! n:
            answer = input("> ")
            if a

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
    if action in thescenes.map_list:
        print("success")
        thescenes.map_list[action](thescenes)
