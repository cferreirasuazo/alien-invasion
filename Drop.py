import pygame
from pygame.sprite import Sprite

class Drop(Sprite):
    def __init__(self,screen,x):
        super(Drop,self).__init__()
        self.screen = screen

        self.image = pygame.image.load("assets/drop.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.y = float(self.rect.y)

    def update(self):
        self.y  += 5
        self.rect.y = self.y
     

    def blitme(self):
        self.screen.blit(self.image, self.rect)
    