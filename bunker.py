import pygame
import random
import math


class Bunker:
    def __init__(self, screen, settings, image):
        self.__screen = screen
        self.__settings = settings
        self.__image = image
        self.rect = self.__image.get_rect()
        self.durability = 100
        self.color = (0, 0, 0)

    def blit(self):
        self.__screen.blit(self.__image, self.rect)

    def blackout(self):
        pygame.draw.rect(self.__screen, self.color, self.rect)

    def change_rect(self, x, y):
        self.rect.x, self.rect.y = x, y

    def check_collision(self, bullet):
        try:
            if bullet.rect.y < self.rect.y or bullet.rect.y > self.rect.bottom:
                return False
            elif self.__image.get_at((math.floor(bullet.rect.x - self.rect.x),
                                      math.floor(bullet.rect.y - self.rect.y))) == (0, 0, 0, 255):
                return False
            else:
                self.bunker_hit(math.floor(bullet.rect.x - self.rect.x), math.floor(bullet.rect.y - self.rect.y))
                return True
        except IndexError:
            return False

    def bunker_hit(self, x, y):
        image = self.__image.convert()
        for i in range(max(0, x - 15), min(x + 15, image.get_width())):
            for j in range(max(0, y - 15), min(y + 15, image.get_height())):
                if abs(i - j) < 20 or abs(i - j) > 40:
                    image.set_at((i, j), (0, 0, 0))
        for i in range(max(0, x - 30), min(x + 30, image.get_width())):
            for j in range(max(0, y - 30), min(y + 30, image.get_height())):
                if random.randint(3, 5) == 4:
                    image.set_at((i, j), (0, 0, 0))
        self.__image = image
        self.blit()
        pygame.display.flip()
        self.durability -= 1
