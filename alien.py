class Alien:
    def __init__(self, screen, settings, image_one, image_two, image_three, image_four, image_five):
        self.__screen = screen
        self.__settings = settings
        self.__screenRect = self.__screen.get_rect()
        self.image_one = image_one
        self.image_two = image_two
        self.rect = self.image_one.get_rect()

        self.dead = False
        self.exploding = False

        self.explode_lib = [image_three, image_four, image_five]
        self.current_explode = 0

    def blit(self):
        self.__screen.blit(self.image_one, self.rect)

    def update(self):
        self.rect.x += self.__settings.get_alien_speed() * self.__settings.get_alien_direction()

    def check_edges(self):
        if self.rect.right >= self.__screenRect.right or self.rect.left <= self.__screenRect.left:
            return True
        return False

    def swap_images(self):
        self.image_one, self.image_two = self.image_two, self.image_one

    def show_next_explode(self):
        self.__screen.blit(self.explode_lib[self.current_explode], self.rect)
        self.current_explode += 1
        if self.current_explode > 2:
            self.dead = True
            self.current_explode = 2

    def get_value(self):
        pass


class PurpleAlien(Alien):
    def __init__(self, screen, settings, image_one, image_two, image_three, image_four, image_five):
        super().__init__(screen, settings, image_one, image_two, image_three, image_four, image_five)

    def get_value(self):
        return 40


class BlueAlien(Alien):
    def __init__(self, screen, settings, image_one, image_two, image_three, image_four, image_five):
        super().__init__(screen, settings, image_one, image_two, image_three, image_four, image_five)

    def get_value(self):
        return 20


class GreenAlien(Alien):
    def __init__(self, screen, settings, image_one, image_two, image_three, image_four, image_five):
        super().__init__(screen, settings, image_one, image_two, image_three, image_four, image_five)

    def get_value(self):
        return 10
