import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    def __init__(self,screen,position):
        super(Star,self).__init__()
        self.screen = screen

        self.image = pygame.image.load("assets/star.png")
        self.rect = self.image.get_rect()

        self.rect.center = position
        
    def blitme(self):
        self.screen.blit(self.image,self.rect)

