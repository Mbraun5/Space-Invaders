import pygame


class Ship:
    def __init__(self, images, screen, settings, explode_sound):
        self.__images = images
        self.__screen = screen
        self.explode_sound = explode_sound
        self.__screenRect = self.__screen.get_rect()
        self.__settings = settings
        self.__image_lib = self.__images
        self.__image = images[0]
        self.rect = self.__image.get_rect()
        self.rect.centerx = self.__settings.get_screen_width() / 2
        self.rect.bottom = self.__settings.get_screen_height()

        self.__speed = self.__settings.get_ship_speed()
        self.movingRight = False
        self.movingLeft = False

    def draw_ship(self):
        self.__screen.blit(self.__image, self.rect)

    def explode(self):
        pygame.mixer.Sound.play(self.explode_sound)
        count = 18
        for i in range(0, 4000000):
            if i % 500000 == 0:
                self.__image = self.__image_lib[count]
                count += 1
                self.draw_ship()
                pygame.display.flip()
        self.__image = self.__image_lib[0]
        self.draw_ship()
        pygame.display.flip()

    def update(self):
        if self.movingRight and self.rect.right < self.__screenRect.right:
            self.rect.centerx += self.__speed
        elif self.movingLeft and self.rect.left > self.__screenRect.left:
            self.rect.centerx -= self.__speed
