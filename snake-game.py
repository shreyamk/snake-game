# Importing packages
import pygame
import sys
import time
import random
from pygame.locals import *

# Initializing display, clock
pygame.init()
width, height = 640, 360
screen = pygame.display.set_mode((width, height),0,32)
surface = pygame.Surface(screen.get_size())
surface = surface.convert()
surface.fill((255,255,255))
clock = pygame.time.Clock()