class Settings:
    def __init__(self):
        self.bg_color = (25, 10, 105)
        self.screen_width = 1200
        self.screen_height = 600
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 210, 60)
        self.fleet_drop_speed = 10
        self.ship_limit = 3
        self.speedup = 1.2
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 2
        self.alien_speed = 1.0
        self.fleet_direction = 1

    def increase_speed(self):
        self.ship_speed *= self.speedup
        self.bullet_speed += self.speedup
        self.alien_speed *= self.speedup


