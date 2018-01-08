import pygame as game
import random

WHITE = (255,255,255)
GREEN = ( 0, 255, 0)
BLACK = (0,0,0)
BLUE = (0,0,255)
RED = (255,0,0)

def drawCircles(screen, x, y):
	game.draw.circle(screen,WHITE,[x,y],50)
	game.draw.circle(screen,GREEN,[x,y],30)
	game.draw.circle(screen,BLUE,[x,y],10)

def main():
	game.init()

	#Defining Variables
	size = (700,500)
	done = False
	x_speed = 0
	y_speed = 0
	x_coord = size[0] // 2
	y_coord = size[1] // 2

	clock = game.time.Clock()
	font = game.font.SysFont('Calibri', 25, True, False)
	text = font.render("I EAT ASS",True, WHITE)

	game.display.set_caption("EAT THIS ASS BOI")
	screen = game.display.set_mode(size)
	game.mouse.set_visible(False)


	while not done:
		for event in game.event.get(): # getting what the user did
			if (event.type == game.QUIT):
				print("You are trying to quit") #i COULD USE THIS FOR A KEYLOGGER
				done = True
			elif (event.type == game.KEYDOWN):
				if event.key == game.K_LEFT:
					x_speed = -3
				elif (event.key == game.K_RIGHT):
					x_speed = 3
				elif (event.key == game.K_UP):
					y_speed = -3
				elif (event.key == game.K_DOWN):
					y_speed = 3
			elif (event.type == game.KEYUP):
				if(event.key == game.K_LEFT or event.key == game.K_RIGHT):
					x_speed = 0
				elif(event.key == game.K_UP or event.key == game.K_DOWN):
					y_speed = 0
		screen.fill(BLACK)
		#pos = game.mouse.get_pos()		Gets the position of the mouse
		if (x_coord < 650 and x_coord > 50):
			x_coord += x_speed
		elif (x_coord > 650):
			if (x_speed < 0):
				x_coord += x_speed
		elif (x_coord < 50):
			if (x_speed > 0):
				x_coord += x_speed	#weird error going on here...			
		if (y_coord < 450 and y_coord > 50):
			y_coord += y_speed
		elif (y_coord > 450):
			if (y_speed < 0):
				y_coord += y_speed
		elif (y_coord < 50):
			if (y_speed > 0):
				y_coord += y_speed		
		drawCircles(screen, x_coord, y_coord)
		game.display.flip()
		clock.tick(60) #Faster makes it look ridiculous lmao
	game.quit()
main()