# -*- coding: utf-8 -*-
import pygame
import os
import sys
from pygame.locals import *

# input handler
def input(events):
  for event in events:
    if event.type == QUIT:
      sys.exit(0)
    elif event.type == KEYDOWN:
        if event.key == K_ESCAPE:
            #pygame.display.quit();
            sys.exit(0)
    else:
      #print event
      pass