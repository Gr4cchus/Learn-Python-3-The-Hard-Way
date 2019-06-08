
class Entrance(object):

    def enter(self):
        print("You have reached the house and walk through the door. Where do you want to go?")

        Map().list_options()
        action = input('>  ')


class Map(object):

    locations = {
        'entrance': Entrance(),
    }

    def list_options(self):
        for items in self.locations:
            print(items)


start = Entrance()
start.enter()
