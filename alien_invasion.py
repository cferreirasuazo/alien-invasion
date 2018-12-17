#main method    

import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_function as gf
from game_stats import GameStats
from button import Button
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
    stats = GameStats(s)
    play_button = Button(s,screen,"Play")

    while True:

        gf.check_events(s,screen,stats,play_button,ship,bullets)
        if stats.game_active:
                ship.update()
                gf.update_bullets(s,screen,ship,aliens,bullets)
                gf.update_aliens(s,stats,screen,ship,aliens,bullets)
        gf.update_screen(s,screen,ship,stats,aliens,bullets,play_button)
        
run_game()
