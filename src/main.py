#!/usr/bin/env python

import pygame
from Input import *
from Models.World import *

WHITE = (255,255,255)
#SCREEN_SIZE = (100,100)
display_size = (400, 400)
display_flags = 0

# Initialize display and window
pygame.init()

screen = pygame.display.set_mode(display_size, display_flags)
pygame.display.set_caption('MultiPython')
pygame.mouse.set_visible(0)

world = World()
num = 1
on = True
#Run Game
while on:
	num += 1
	#inputs
	input(pygame.event.get())
	(m1,m2,m3) = pygame.mouse.get_pressed()
	if m1 == 1 :
		print "done"
		on = False
		exit()

	#reset values 
#    lock framerate
	#clock.tick(30)			
#    draw black rectangle to renew the canvas
	pygame.draw.rect(screen, (200,0,200), (0, 0, screen.get_width(), screen.get_height()))
	pygame.draw.rect(screen, (0,0,0), (50,50,10,10))
	pygame.draw.circle(screen,(255,255,255),(screen.get_width() / 2, screen.get_height() / 2),5)
	pygame.draw.rect(screen, WHITE, ( (screen.get_width() / 2) -5, (screen.get_height() / 2) -5, 10,5))
	pygame.draw.rect(screen, WHITE, ( (screen.get_width() / 2) -5, (screen.get_height() / 2) -5, 5,10))
	
	
	pygame.display.update()


