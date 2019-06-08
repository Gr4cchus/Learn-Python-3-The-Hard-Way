class Death(object):
    death_prologue = [
        'dead',
        'game over'
    ]

    def enter(self):
        pass

class Scene(object):

    def enter(self):
        print("This scene is not yet configured")
        print("subclass it and implement enter().")
        exit(1)

class Entrance(object):

    def enter(self):
        print("You have reached the house and walk through the door. Where do you want to go?")
        # print(Map.locations)

        # action = input('>  ')

        # for items in Map.locations:
        #     print(items)


class LivingRoom(object):

    def enter(self):
        pass

class MasterBedroom(object):

    def enter(self):
        pass

class MasterBedroomBathroom(object):

    def enter(self):
        pass

class Bedroom(object):

    def enter(self):
        pass

class Bathroom(object):

    def enter(self):
        pass

class DinningArea(object):

    def enter(self):
        pass

class Exit(object):

    def enter(self):
        pass

class Patio(object):

    def enter(self):
        pass

class Kitchen(object):

    def enter(self):
        pass

class Finished(object):

    def enter(self):
        print("You have finished!")
        exit(0)

class Map(object):

    locations = {
        'entrance': Entrance(),
        'living room': LivingRoom(),
        'master bedroom': MasterBedroom(),
        'master bedroom bathroom': MasterBedroom(),
        'bedroom': Bedroom(),
        'bathroom': Bathroom(),
        'dining area': DinningArea(),
        'exit': Exit(),
        'patio': Patio(),
        'kitchen': Kitchen(),
        'Finished': Finished(),
    }

    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass


# start = Entrance()
# start.enter()
(Map.locations.get('entrance'))

for items in Map.locations:
    print(items)