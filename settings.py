class Settings():

    def __init__(self):
        """Class for settings """
        self.hs_directory = "high_score"
        self.hs_file = "high_score.json" 
        self.fullpath = self.hs_directory + "/" + self.hs_file


        self.screen_width = 1000
        self.screen_height = 600 
        self.bg_color = (230,230,230)
        
        #ship settings
        #self.ship_speed_factor = 2.5
        self.ship_limit = 1

        #bullet settings
        #self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allow = 3
        
        # #alien settings
        self.alien_speed_factor = 0.5
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

        #game speed up
        self.speedup_scale = 1.1 
        self.score_scale = 1.5
        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.fleet_direction *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        

    