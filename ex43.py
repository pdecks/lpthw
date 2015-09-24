# Gothons from Planet Percal #25

from sys import exit
from random import randint

# Parent Classes
class Scene(object):

	def enter(self):
		print "This scene is not yet configured. Subclass it and implement enter()."
		exit(1) # why not just exit()?

class Engine(object):

	def __init__(self, scene_map):
		self.scene_map = scene_map

	def play(self):
		current_scene = self.scene_map.opening_scene()

		while True:
			print "\n--------"
			next_scene_name = current_scene.enter() # user action returns next scene name
			current_scene = self.scene_map.next_scene(next_scene_name) # from Map class call next scene from dictionary



# Child Classes
class Death(Scene):

	def enter(self):
		print "You really messed up this time. YOU ARE DEAD.\n"
		print "GAME OVER.\n\n"
		print "--------"
		exit(1)

class CentralCorridor(Scene):

	def enter(self):
		print "You find yourself in a central corridor. Gothon is here with you."
		print "What would you like to do? [Enter 'shoot', 'dodge', or 'tell a joke']"
		action = raw_input('> ')

		if action == 'shoot':
			print "You are a bad shot. You miss Gothon, and he pounds you into a pulp."
			return 'death'
		elif action == 'dodge':
			print "This isn't a boxing match. Gothon stomps on your head repeatedly."
			return 'death'
		elif action == 'tell a joke':
			print "Those hours you spent honing your jokes in college paid off. Gothon"
			print "laughs so hard that he doesn't notice you jumping through the Weapon"
			print "Armory door."
			return 'laser_weapon_armory'
		else:
			print "DOES NOT COMPUTE!"
			return 'central_corridor'


class LaserWeaponArmory(Scene):

	def enter(self):
		print "Check out all of these cool weapons! It looks like the only one that will"
		print "help you get out of here is a neutron bomb. Unfortunately, the bomb is"
		print "in a locked box fitted with a keypad. You decide to guess the 1-digit code."
		print "Better guess wisely!"
		code = randint(1, 9)
		# code = "%d%d%d" % (randint(1, 9), randint(1, 9), randint(1, 9))
		guess = int(raw_input("[keypad]> "))
		guesses = 0

		while guess != code and guesses < 10:
			print "BZZZZEDDD!"
			guesses += 1
			guess = int(raw_input("[keypad]> "))

		if guess == code:
			print "You did it! You haul the bomb to the bridge."
			return 'the_bridge'
		else:
			return 'death'


class TheBridge(Scene):

	def enter(self):
		print "This is the bridge. Gothon is blocking your way to the escape pods."
		print "What do you want to do? [Enter 'throw bomb' or 'place bomb']"
		action = raw_input("> ")

		if action == "throw bomb":
			print "You hastily chuck the bomb and try to flee, but a bullet gets you in the back."
			return 'death'
		elif action == "place bomb":
			print "You place the bomb and run to the escape pod."
			return 'escape_pod'
		else:
			print "DOES NOT COMPUTE!"
			return 'the_bridge'


class EscapePod(Scene):

	def enter(self):
		print "There are 5 escape pods, some of which might be damaged. Which one do you take?"
		print "Enter a number from 1 to 5."
		
		good_pod = randint(1, 5)
		guess = int(raw_input("> "))

		if guess != good_pod:
			print "You chose poorly."
			return 'death'
		else:
			print "You made it out alive! You win!"

			return 'finished'


class Finish(Scene):

	def enter(self):
		return False


# Map has to come after the scenes because the dictionary has to refer to them
# so they have to exist
class Map(object):

	scenes = {
		'central_corridor': CentralCorridor(),
		'laser_weapon_armory': LaserWeaponArmory(),
		'the_bridge': TheBridge(),
		'escape_pod': EscapePod(),
		'death': Death(),
		'finished': Finish()
	}

	def __init__(self, start_scene):
		self.start_scene = start_scene

	def next_scene(self, scene_name):
		return Map.scenes.get(scene_name) # returns dict value for given key

	def opening_scene(self):
		return self.next_scene(self.start_scene)

a_map = Map('central_corridor') # starting scene is central corridor
a_game = Engine(a_map) # start a new game
a_game.play() # run the game