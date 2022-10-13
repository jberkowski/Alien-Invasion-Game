# Settings class which stores all setting for Alien Invasion Game.

class Settings:
    """A class to store all settings for Alien Invasion Game."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings.
        self.screen_width = 1280
        self.screen_height = 720
        self.bg_color = (100, 100, 100)

        # Ship speed.
        self.ship_limit = 3

        # Bullet settings.
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (50, 50, 50)
        self.bullets_allowed = 3

        # Alien settings.
        self.fleet_drop_speed = 10

        # How quickly the game speeds up.
        self.speedup_scale_easy = 1.1
        self.speedup_scale_medium = 1.2
        self.speedup_scale_hard = 1.3

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 0.7

        # fleet_direction of 1 represents right, -1 represents left.
        self.fleet_direction = 1