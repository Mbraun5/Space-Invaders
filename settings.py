class Settings:
    def __init__(self):
        #   Screen Settings
        self.__screenWidth = 1600
        self.__screenHeight = 1000
        self.__bgColor = (0, 0, 0)

        #   Game Settings
        self.__gameTitle = "Space Invaders"

        #   Ship Settings
        self.__shipSpeed = 2

        #   Alien Settings
        self.__alienDirection = 1
        self.__alienSpeed = 20
        self.__alienDropSpeed = 40
        self.__timeVar = 250            # Variable to detect how often aliens are updated.
        self.__alienFireRate = 700      # Aliens have a 1/(rate) change to fire a bullet every time through loop.

        #   Bullet Settings
        self.__bulletColor = (255, 255, 255)
        self.__bulletWidth = 5
        self.__bulletHeight = 25
        self.__bulletSpeed = 2
        self.__shootingFlag = False

        #   Reset Flag
        self.__game_reset = False

    def get_bg_color(self):
        return self.__bgColor

    def get_game_title(self):
        return self.__gameTitle

    def get_screen_width(self):
        return self.__screenWidth

    def get_screen_height(self):
        return self.__screenHeight

    ################################################################################
    #                   Ship Functions                                             #
    ################################################################################
    def get_ship_speed(self):
        return self.__shipSpeed

    ################################################################################
    #                   Alien Functions                                            #
    ################################################################################
    def get_alien_speed(self):
        return self.__alienSpeed

    def get_alien_direction(self):
        return self.__alienDirection

    def change_alien_direction(self):
        self.__alienDirection *= -1

    def get_alien_drop(self):
        return self.__alienDropSpeed

    def get_time_var(self):
        return self.__timeVar

    def get_alien_fire_rate(self):
        return self.__alienFireRate

    def increase_fire_rate(self, value):
        if self.__alienFireRate > 100:
            self.__alienFireRate -= value

    ################################################################################
    #                   Bullet Functions                                           #
    ################################################################################
    def get_bullet_width(self):
        return self.__bulletWidth

    def get_bullet_height(self):
        return self.__bulletHeight

    def get_bullet_color(self):
        return self.__bulletColor

    def get_bullet_speed(self):
        return self.__bulletSpeed

    def get_shooting_flag(self):
        return self.__shootingFlag

    def set_shooting_flag(self, bool_var):
        self.__shootingFlag = bool_var

    def set_reset(self, bool_var):
        self.__game_reset = bool_var
        if bool_var:
            self.__timeVar = 250
            self.__alienFireRate = 700

    def get_game_reset(self):
        return self.__game_reset
