import libtcodpy as libtcod

class Actor:
	
	x = 0
	y = 0
	character = '@'
	color = libtcod.Color(255, 255, 255)
	
	def __init__(self, X, Y, char, col):
		x = X
		y = Y
		character = char
		color = col
		
	def draw(console = None):
		console_set_fore(console, x, y, color)
		console_set_char(console, x, y, character)
		
	def update()
		#Do logic here, depending on what we are working with
		pass
		
