import pygame as game
import random

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
snow_list = []

game.display.set_caption("EAT THIS ASS BOI")
screen = game.display.set_mode(size)


for i in range(50):
	x = random.randrange(0,700)
	y = random.randrange(0,500)
	snow_list.append([x,y])

while not done:
	for event in game.event.get(): # getting what the user did
		if (event.type == game.QUIT):
			print("You are trying to quit") #i COULD USE THIS FOR A KEYLOGGER
			done = True
	screen.fill(BLACK)
		
	for i in range(len(snow_list)):
		game.draw.circle(screen,WHITE,snow_list[i],2)
		snow_list[i][1] += 2
		if snow_list[i][1] > 400:
			y = random.randrange(-50,-10)
			snow_list[i][0] = y
			x = random.randrange(0,700)
			snow_list[i][0] = x

	game.display.flip()
	clock.tick(20) #Faster makes it look ridiculous lmao
game.quit()