import pygame as game

game.init()

#Defining Variables
WHITE = (255,255,255)
BLUE = (   0,   0, 255)
GREEN = ( 0, 255, 0)
BLACK = (0,0,0)
done = False
y_offset = 0
clock = game.time.Clock()
size = (700,500)
font = game.font.SysFont('Calibri', 25, True, False)
text = font.render("I EAT ASS",True, WHITE)

game.display.set_caption("EAT THIS ASS BOI")
screen = game.display.set_mode(size)

rect_x = 50 
rect_y = 50
rect_x_change = 5
rect_y_change = 5
while not done:
	for event in game.event.get(): # getting what the user did
		if (event.type == game.QUIT):
			print("You are trying to quit") #i COULD USE THIS FOR A KEYLOGGER
			done = True
	screen.fill(WHITE)
	screen.fill(BLACK)

	game.draw.rect(screen, WHITE, [rect_x, rect_y, 50, 50])
	if (rect_y > 450 or rect_y < 0):
		rect_y_change *= -1
	if (rect_x > 650 or rect_x < 0):
		rect_x_change *= -1
	rect_x += rect_x_change #Changes the movement of the rect in the x coordinate
	rect_y += rect_y_change #Changes the movement of the rect in the y coordinate
	game.display.flip()
	clock.tick(60)

game.quit()