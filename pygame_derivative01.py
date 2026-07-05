import os
# Hide the welcome message
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

import pygame
import numpy

screen = None
_screen_width = 0
_screen_height= 0

def make_screen(x=_screen_width,y=_screen_height):
  screen = pygame.display.set_mode((x, y))

def full_screen():
  screen = pygame.display.set_mode((screen_width, screen_height))
