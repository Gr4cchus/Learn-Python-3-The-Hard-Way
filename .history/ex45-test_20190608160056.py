
class Entrance(Map):

    def enter(self):
        print("You have reached the house and walk through the door. Where do you want to go?")

        Map().list_options()
        action = input('>  ')

        if action in Map().locations:
            print("success")
            print(Map().locations.get(action))
            print(Map().locations[action])
        else:
            print("Fail")
            print(Map.locations)


class LivingRoom(object):

    def enter(self):
        pass


class Map(object):

    locations = {
        'entrance': Entrance(),
        'living room': LivingRoom(),
    }

    def list_options(self):
        for items in self.locations:
            print(items)


start = Entrance()
start.enter()

# Map.locations.get('entrance')
# print(Map.locations.get('entrance'))