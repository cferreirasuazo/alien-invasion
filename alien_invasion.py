#main method

import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_function as gf


import random 
from Star import Star


def run_game():
    pygame.init()
    s = Settings()
    screen = pygame.display.set_mode((s.screen_width, s.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(s,screen)
    aliens = Group()
    bullets = Group()
    
    stars = Group()

    gf.create_fleet(s,screen,ship,aliens)

#     for o in range(1,100):

#         coor_x = random.randint(1,1000)
#         coor_y = random.randint(1,600)
#         star = Star(screen, (coor_x,coor_y))
#         stars.add(star)

    while True:

        gf.check_events(s,screen,ship,bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(s,screen,ship,aliens,bullets,stars)
        
run_game()
