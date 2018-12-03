#main method    

import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_function as gf


#import random 



def run_game():
    pygame.init()
    s = Settings()
    screen = pygame.display.set_mode((s.screen_width, s.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(s,screen)
    aliens = Group()
    bullets = Group()
    

    gf.create_fleet(s,screen,ship,aliens)


    while True:

        gf.check_events(s,screen,ship,bullets)
        ship.update()
        gf.update_bullets(s,screen,ship,aliens,bullets)
        gf.update_aliens(s,aliens)
        gf.update_screen(s,screen,ship,aliens,bullets)
        
run_game()
