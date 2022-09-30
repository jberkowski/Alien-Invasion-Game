# Settings class which stores all setting for Alien Invasion Game.

class Settings:
    """A class to store all settings for Alien Invasion Game."""

    def __init__(self):
        # Screen settings.
        self.screen_width = 1280
        self.screen_height = 720
        self.bg_color = (100, 100, 100)

        # Ship speed
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (50, 50, 50)
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed = 0.5
        self.fleet_drop_speed = 5
        # fleet_direction of 1 represents right, -1 represents left.
        self.fleet_direction = 1