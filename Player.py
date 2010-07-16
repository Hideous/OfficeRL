import Actor
import libtcodpy as libtcod

class Player(Actor.Actor):
	#The player class! Handles movement and whatnot.
	
	def __init__(self):
		Actor.__init__(self, 0, 0, '@', libtcod.Color(255, 255, 255))
	
	def update(self):
		#handle keyboard control stuff here, make turns pass when appropriate
		Actor.update(self)
