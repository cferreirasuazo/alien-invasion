class Settings():

    def __init__(self):

        self.screen_width = 1000
        self.screen_height = 600 
        self.bg_color = (230,230,230)

        #ship settings
        self.ship_speed_factor = 2.5
        self.ship_limit = 3 

        #bullet settings
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allow = 3
        
        # #alien settings
        self.alien_speed_factor = 0.4
        self.fleet_drop_speed = 15
        self.fleet_direction = 1

        