class Settings():

    def __init__(self):

        self.screen_width = 1000
        self.screen_height = 600 
        self.bg_color = (230,230,230)
        self.ship_speed_factor = 2.5

        
        #bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allow = 3
        
        # #alien settings
        self.alien_speed_factor = 0.4
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

        