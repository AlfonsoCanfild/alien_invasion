class Settings:

    def __init__(self):
        # config da tela
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (109, 139, 143)
        self.ship_speed = 4
        self.ship_limit = 3
        # config dos tiros
        self.bullet_speed = 2.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5
        self.alien_speed = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

        self.speed_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 2.5
        self.alien_speed = 1.0

        self.fleet_direction = 1

    def increase_speed(self):
        self.ship_speed *= self.speed_scale
        self.bullet_speed *= self.speed_scale
        self.alien_speed *= self.speed_scale
