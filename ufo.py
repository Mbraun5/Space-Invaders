import pygame
import random


def generate_score():
    return 50 * random.randint(1, 9)


class UFO:
    def __init__(self, image, scoreboard, screen, settings, sound):
        self.__scoreboard = scoreboard
        self.__settings = settings
        self.__screen = screen
        self.__sound = sound

        #   UFO Image and rect
        self.image = pygame.transform.scale(image, (140, 75))
        self.rect = self.image.get_rect()
        self.speed = 1
        self.rect.top = scoreboard.currentScoreRect.bottom

        #   Text to display when UFO Explodes
        self.font = pygame.font.Font('Fonts/PixFont.ttf', 40)
        self.textColor = self.__settings.get_bullet_color()
        self.scoreValue = generate_score()
        self.scoreImage = self.font.render("{}".format(self.scoreValue), True, self.textColor,
                                           self.__settings.get_bg_color())
        self.scoreRect = self.scoreImage.get_rect()

        self.random_side()
        pygame.mixer.Sound.play(self.__sound, -1)

    def random_side(self):
        var = random.randint(1, 100)
        if var % 2 == 0:
            self.rect.x = 0 - self.image.get_width()
        else:
            self.rect.x = self.__settings.get_screen_width()
            self.speed *= -1

    def blit(self):
        self.__screen.blit(self.image, self.rect)

    def update(self):
        self.rect.x += self.speed

    def explode(self):
        self.scoreRect.centery = self.rect.centery
        self.scoreRect.centerx = self.rect.centerx
        #   Blacks out the image and replaces image with score text.
        pygame.draw.rect(self.__screen, (0, 0, 0), self.rect)
        self.__screen.blit(self.scoreImage, self.scoreRect)
        self.__scoreboard.update_score(self.scoreValue)
        pygame.mixer.Sound.stop(self.__sound)
        pygame.display.flip()

    def check_bounds(self):
        if self.rect.right < 0 or self.rect.left > self.__settings.get_screen_width():
            pygame.mixer.Sound.stop(self.__sound)
            return True
        return False
