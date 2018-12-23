class GameStats():
    def __init__(self,settings):
        self.game_active = False
        self.settings = settings
        self.reset_stats()
        

    def reset_stats(self):
        self.ship_left = self.settings.ship_limit
        self.score = 0

    


