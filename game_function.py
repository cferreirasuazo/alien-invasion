
#events
import sys
import pygame
from Bullet import Bullet
from Alien import Alien
from time import sleep

#KEYDOWN Event 
def check_keydown_events(event,settings,screen,ship,bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullets(settings,screen,ship,bullets)
    elif event.key == pygame.K_q:
                sys.exit()

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(settings,screen,stats,play_button,ship,aliens,bullets):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                check_keydown_events(event,settings,screen,ship,bullets)
            elif event.type == pygame.KEYUP:
                check_keyup_events(event,ship)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                check_play_button(settings,screen,stats,play_button,ship,aliens,bullets,mouse_x,mouse_y)
            
def check_play_button(settings,screen,stats,play_button,ship,aliens,bullets,mouse_x,mouse_y):
    if play_button.rect.collidepoint(mouse_x,mouse_y):
        stats.reset_stats()
        stats.game_active = True

        aliens.empty()
        bullets.empty()

        create_fleet(settings,screen,ship,aliens)
        ship.center_ship()        
        

#Updates positon of the bullets
def update_bullets(settings,screen,ship,aliens, bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <=0:
            bullets.remove(bullet)
    

    check_bullet_alien_collition(settings,screen,ship,aliens, bullets)

def check_bullet_alien_collition(settings,screen,ship,aliens, bullets):
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)

    if len(aliens) == 0:
        bullets.empty()
        create_fleet(settings,screen,ship,aliens)

#ship fires a bullet 
def fire_bullets(settings,screen,ship,bullets):
    if len(bullets) < settings.bullets_allow:
        new_bullet = Bullet(settings,screen,ship)
        bullets.add(new_bullet)


#get how many aliens could be avariable in the screen
def get_number_aliens_x(settings,alien_width):
    avariable_space_x = settings.screen_width - 2 * alien_width
    number_aliens_x = int(avariable_space_x / (2 * alien_width))    
    return number_aliens_x

def get_number_rows(settings, ship_heigth, alien_height):
    avariable_space_y = (settings.screen_height - (3 * alien_height) - ship_heigth)
    number_rows = int(avariable_space_y / (2* alien_height))
    return number_rows 

#creates and alien 
def create_alien(settings, screen,aliens,alien_number,row_number):
    alien = Alien(settings,screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    alien.rect.x = alien.x
    aliens.add(alien)

def create_fleet(settings,screen,ship,aliens):
    alien = Alien(settings,screen)
    number_aliens_x = get_number_aliens_x(settings,alien.rect.width)
    number_rows = get_number_rows(settings,ship.rect.height,alien.rect.height)

    for row_number in range(number_rows):
        for alien_number in (range(number_aliens_x)):
            create_alien(settings,screen,aliens,alien_number,row_number)


def shit_hit(settings,stats,screen,ship,aliens,bullets):
    if stats.ship_left > 0:
        stats.ship_left -= 1
        aliens.empty()
        bullets.empty()
        create_fleet(settings,screen,ship,aliens)
        ship.center_ship()
        sleep(0.5)
    else:
        stats.game_active = False

def check_aliens_bottom(settings, stats, screen, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            shit_hit(settings,stats,screen,ship,aliens,bullets)
            break

def update_aliens(settings,stats,screen,ship,aliens,bullets):
    check_aliens_bottom(settings, stats, screen, ship, aliens, bullets)
    check_fleet_edges(settings,aliens)
    aliens.update()


    if pygame.sprite.spritecollideany(ship,aliens):
        shit_hit(settings,stats,screen,ship,aliens,bullets)


def change_fleet_direction(settings,aliens):
    for alien in aliens.sprites():
        alien.rect.y +=settings.fleet_drop_speed
    settings.fleet_direction *= -1

def check_fleet_edges(settings,aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(settings,aliens)
            break

def update_screen(settings,screen,ship,stats,aliens,bullets,play_button):
    screen.fill(settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    if not stats.game_active:
        play_button.draw_button()

    pygame.display.flip()
