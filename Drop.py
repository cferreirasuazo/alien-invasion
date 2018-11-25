import pygame
from pygame.sprite import Sprite

class Drop(Sprite):
    def __init__(self,screen,position):
        super(Drop,self).__init__()
        self.screen = screen

        self.image = pygame.image.load("assets/drop.png")
        self.rect = self.image.get_rect()
        self.rect.center = position

    def __blitme__(self):
        self.screen.blit(self.image, self.rect)
    