"""Main Module"""

import sys
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_function as gf
from game_stats import GameStats
from button import Button
from scoreboard import ScoreBoard
import os
#import random 



def main():

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
    sb = ScoreBoard(s,screen,stats)
    stats.high_score = gf.load_high_score(s,stats)  
    while True:

        gf.check_events(s,screen,stats,sb,play_button,ship,aliens,bullets)
        if stats.game_active:
                ship.update()
                gf.update_bullets(s,screen,stats,sb,ship,aliens,bullets)
                gf.update_aliens(s,stats,sb,screen,ship,aliens,bullets)
        gf.update_screen(s,screen,ship,stats,sb,aliens,bullets,play_button)
        
if __name__ == "__main__":
	main()
