#Settings class which stores all setting for Alien Invasion Game.

class Settings:
    """A class to store all settings for Alien Invasion Game."""

    def __init__(self):
        #Screen settings.
        self.screen_width = 1280
        self.screen_height = 720
        self.bg_color = (100, 100, 100)

        #Ship speed
        self.ship_speed = 1.5