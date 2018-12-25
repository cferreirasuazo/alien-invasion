import pygame.font

class ScoreBoard():

    """A class for scoring information"""

    def __init__(self,settings,screen,stats):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.settings = settings 
        self.stats = stats 

        self.text_color = (30,30,30)
        self.font = pygame.font.Font("assets/ARCADE_R.TTF",30)

        self.prep_score()
        self.prep_high_score()
        self.prep_level()

    def prep_score(self):
        self.rounded_score = int(round(self.stats.score,-1))
        score_str  = "{:,}".format(self.rounded_score)
        self.score_image = self.font.render(score_str,True,self.text_color,self.settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        self.high_score = int(round(self.stats.high_score,-1))
        self.high_score_str = "{:,}".format(self.high_score)
        self.high_score_image = self.font.render(self.high_score_str,True,self.text_color,self.settings.bg_color)

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        self.level_image = self.font.render(str(self.stats.level),True,self.text_color,self.settings.bg_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def show_score(self):
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(self.level_image,self.level_rect)
