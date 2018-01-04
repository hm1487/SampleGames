import pygame as game

game.init()

#Defining Variables
WHITE = (255,255,255)
BLUE = (   0,   0, 255)
GREEN = ( 0, 255, 0)
done = False
y_offset = 0
clock = game.time.Clock()
size = (700,500)
font = game.font.SysFont('Calibri', 25, True, False)
text = font.render("I EAT ASS",True, WHITE)

game.display.set_caption("EAT THIS ASS BOI")
screen = game.display.set_mode(size)

while not done:
	for event in game.event.get(): # getting what the user did
		if (event.type == game.QUIT):
			print("You are trying to quit") #i COULD USE THIS FOR A KEYLOGGER
			done = True
		
		screen.fill(BLUE)
		game.draw.line(screen,GREEN,[0,0+y_offset],[100,100+y_offset],5) #lmao this looks funny
		screen.blit(text,[300,0 + y_offset])
		y_offset += 10
		game.display.flip()
		clock.tick(60)

game.quit()