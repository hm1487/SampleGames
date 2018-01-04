import pygame as game

game.init()

#Defining Variables
WHITE = (255,255,255)
BLUE = (   0,   0, 255)
done = False
clock = game.time.Clock()
size = (700,500)


game.display.set_caption("EAT THIS ASS BOI")
screen = game.display.set_mode(size)

while not done:
	for event in game.event.get(): # getting what the user did
		if (event.type ==game.QUIT):
			print("You are trying to quit") #i COULD USE THIS FOR A KEYLOGGER
			done = True
		elif (event.type == game.KEYDOWN):
			print("You pressed a key")
		elif (event.type == game.KEYUP):
			print("You released a key")
		elif (event.type == game.MOUSEBUTTONDOWN):
			print("You pressed on the mouse")
		screen.fill(BLUE)	
		game.display.flip()
		clock.tick(60)

game.quit()