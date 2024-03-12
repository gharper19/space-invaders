import pygame, sys
from pygame.locals import *

IMAGES_FILEPATH = "images/"

WINDOW_NAME = "Mane: Wait Hol Up, The Sequel" 
WINDOW_SIZE = (600, 400)
WINDOW_BASE_PLAY_SIZE = (300, 200) # Used for upscaling - If you half the values you make each pixel twice as large
WINDOW_BACKGROUND_COLOR = (0 , 0, 0)

# Initialize window
pygame.init()
pygame.display.set_caption(WINDOW_NAME)
screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
display = pygame.Surface(WINDOW_BASE_PLAY_SIZE) # display surface drawn on top of screen

# Load player movement data
moving_right = False
moving_left = False
player_speed = 4
player_y_momentum = 0
player_location = (0, 0)

clock = pygame.time.Clock() # Set up game clock


def send_wave():
    pass

def game_loop():
    
    pass