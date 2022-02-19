from turtle import window_width, title

import asteroid as asteroid
import pygame
import self as self
from pygame.constants import (QUIT, K_KP_PLUS, K_KP_MINUS, K_ESCAPE, KEYDOWN)
import os

class Settings(object):
    window_width = 800
    window_height = 500
    window_border = 10
    fps = 60
    title = "Asteroids_Grygierek"
    os.path_file = os.path.dirname(os.path.abspath(__file__))
    os.path_image = os.path.join(os.path_file, "images")
    directions = {'stop':(0, 0), 'down':(0,  1), 'up':(0, -1), 'left':(-1, 0), 'right':(1, 0)}



if __name__ == '__main__':
    os.environ['SDL_VIDEO_WINDOW_POS'] = "10, 50"   # left, top corner of the window
    pygame.init()                                   # start PyGame

    screen = pygame.display.set_mode((Settings.window_width, Settings.window_height))    # create an window 1000= breite 600= höhe
    clock = pygame.time.Clock()                     # start the clock

    background_image = pygame.image.load("images/background.png")
    background_image = pygame.transform.scale(background_image, (Settings.window_width, Settings.window_height))
    background_rect = background_image.get_rect()

    raumschiff_image = pygame.image.load("images/raumschiff.png")
    raumschiff_image = pygame.transform.scale(raumschiff_image, (55,90))
    raumschiff_rect = raumschiff_image.get_rect()
    raumschiff_rect.centerx = Settings.window_width //2
    raumschiff_rect.bottom = Settings.window_height - Settings.window_border
    #Drehung des Raumschiffes um 22,5 Grad

    asteroid_image = pygame.image.load("images/asteroid.png")
    asteroid_image = pygame.transform.scale(asteroid_image, (50,50))
    asteroid_rect = asteroid_image.get_rect()
    asteroid_rect.centerx = Settings.window_width //2
    #Random Spwanen

    #self.speed_x = self.speed_x - sin (angle)
    #self.speed_y = self.speed_y - cos (angle)  #beschleunigung in Blickrichtung

    #Geschwindigkeit auf Intervall (-10/10) begrenzen

    #Spawen des Raumschiffes auf der gegenüberliegenden Seite 

    running = True
    while running:                                  # main loop
        clock.tick(60)                              # slow down to 1/60 sec
        for event in pygame.event.get():            # event handle
            if event.type == pygame.QUIT:
                running = False
        screen.blit(background_image, (background_rect.left, background_rect.top))
        screen.blit(raumschiff_image, (raumschiff_rect.left, raumschiff_rect.top))
        screen.blit(asteroid_image, (asteroid_rect.left, asteroid_rect.top))
        pygame.display.flip()                       # flip doublebuffer

    pygame.quit()                                   # stop PyGame
