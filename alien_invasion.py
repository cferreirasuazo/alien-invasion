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

    #gf.create_fleet(s,screen,ship,aliens)

    drops = Group()


    while True:

        gf.check_events(s,screen,ship,bullets)
        ship.update()

        gf.fall_drop(screen,random.uniform(1,1000),drops)
        gf.update_drops(drops)
        gf.update_bullets(bullets)
      #  gf.update_aliens(s,aliens)
        gf.update_screen(s,screen,ship,aliens,bullets,stars,drops)
        
run_game()
