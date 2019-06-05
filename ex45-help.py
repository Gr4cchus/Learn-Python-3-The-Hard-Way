from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):
    
    def enter(self):
        print("This scene is not yet configured")
        print("subclass it and implement enter().")
        exit(1)

# engine was here

class Death(Scene):

    quips = [
        "You died.",
        "Nice try",
        "Failed."
        ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)


class CentralCorridor(Scene):

    def enter(self):
        print(dedent("Your on a ship. Enemy. 's'hoot, 'd'odge, or 'j'oke?"))

        action = input(">  ")

        if action == "s":
            print(dedent("""
            You shoot but miss.
            """))
            return 'death'

        elif action == "d":
            print(dedent("""
            You dodge but miss a step and fall.
            """))
            return 'death'

        elif action == 'j':
            print(dedent("""
            You kill the Gothon with laughter.
            """))
            return 'laser_weapon_armory'

        else:
            print("Error")
            return 'central_corridor'


class LaserWeaponArmor(Scene):

    def enter(self):
        print(dedent("Your at the armory, 'g'rab the bomb."))
        
        action = input("> ")

        if action == 'g':
            print("You grab the weapon and run to the bridge")
            return 'the_bridge'
        else:
            print("You die.")
            return 'death'
        

class TheBridge(Scene):

    def enter(self):
        print("You arrive to the bridge . Enemy. 'T'hrow, or 'p'lace?")
        action = input("> ")

        if action == "t":
            print("You get shot and die as you watch the Gothon trying to disarm the bomb")
            return 'death'
        
        elif action == 'p':
            print("You point the blaster at the bomb but slowly place it. You back out through the door to the escape pod")
            return 'escape_pod'
        else:
            print("Error")
            return "the_bridge"


class EscapePod(Scene):

    def enter(self):
        print("Escape pods. pick 1 of 5.")

        good_pod = randint(1,5)
        print('Good pod is: ', good_pod)
        guess = input("> ")

        if int(guess) != good_pod:
            print(f"you get into pod {guess} but it blows after ejection.")
            return "death"
        else:
            print(f"You get into pod {guess} and eject. You watch as the ship explodes.")
            return 'finished'


class Finished(Scene):

    def enter(self):
        print("You win")
        return 'finished'


class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmor(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        print("MMMMMM scene_name:", scene_name)
        print("MMMMM next_scene val:", val)
        return val
    
    def opening_scene(self):
        print("MMM opening_scene:", self.next_scene(self.start_scene))
        return self.next_scene(self.start_scene)
        

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        print(">>>>> PLAY")
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')
        

        print("^^^^^^^^ before while current_scene=", current_scene, "last_scene=", last_scene)
        print(current_scene.enter())
        while current_scene != last_scene:
            print("^^^^^ top of while current_scene=", current_scene, "last_scene=", last_scene)
            next_scene_name = current_scene.enter()
            print("^^^next_scene_name:", next_scene_name)
            current_scene = self.scene_map.next_scene(next_scene_name)
            print("^ End of while current_scene=", current_scene, "last_scene=", last_scene, "next_scene_name=", next_scene_name)

        # be sure to print out last scene
        print("<<<<<< end of play: current_scene=", current_scene)
        current_scene.enter()


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
# * Map
#     − next_scene
#     − opening_scene
# * Engine
#     − play
# * Scene
#     − enter
#     * Death
#     * Central Corridor
#     * Laser Weapon Armory
#     * The Bridge
#     * Escape Pod