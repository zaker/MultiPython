import pygame
from Input import *

#SCREEN_SIZE = (100,100)

display_size = (100, 100)
display_flags = 0

# Initialize display and window
pygame.init()

screen = pygame.display.set_mode(display_size, display_flags)
pygame.display.set_caption('MultiPython')
pygame.mouse.set_visible(0)


num = 1
on = True
#Run Game
while on:
    print num 
    num += 1
    #inputs
    input(pygame.event.get())
    (m1,m2,m3) = pygame.mouse.get_pressed()
    if m1 == 1 :
        on = False
    #reset values 
#    lock framerate
    #clock.tick(30)
#    draw black rectangle to renew the canvas
    pygame.draw.rect(screen, (200,0,200), (0, 0, screen.get_width(), screen.get_height()))


