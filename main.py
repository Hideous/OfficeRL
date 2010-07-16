import libtcodpy as libtcod

SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50

def update():
	pass

def draw():
	libtcod.console_flush()

def main():
	libtcod.console_set_custom_font('terminal8x8_gs_ro.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_INROW)
	libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'OfficeRL', False)
	
	while not libtcod.console_is_window_closed():
		update()
		draw()


if __name__ == "__main__":
	main()