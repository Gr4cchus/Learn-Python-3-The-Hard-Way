import random

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
        self.guessing_game()
        self.locations()

    def room2(self):
        print("You enter room 2")
        print("Oh no an enemy presents itself. 's'hoot or 'r'un?")
        action = input('> ')

        if action == 's':
            print("You shoot and kill the threat.")
        elif action == 'r':
            print("You run and end up back in room 1!")
            self.room1()    # this wont work, it prints double.
            return 'room1'
        self.locations()
        print("Where would you like to go")
    
    def finish(self):
        print("You have finished")
        exit(0)
    
    def locations(self):
        # print("def locations:", self.cmd)
        # for i in self.cmd:
        #     # print(i)
        for key, value in self.cmd.items():
            print(key)
        # print(self.cmd.keys())


    cmd = {
        'room1': room1,
        'room2': room2,
        'finished': finish
    }

    def guessing_game(self):
        n = random.randint(1,4)
        print("Oh no a mini-game.")
        print("Guess the number between 1-4. To pass")
        answer = 0
        while answer != n:
            answer = int(input("> "))
                if answer !=print("wrong guess again!")
            print(f'Its {n}')
        if answer == n:
            print("Success")

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
        thescenes.cmd[action](thescenes)
