import pygame


class Bullet:
    def __init__(self, screen, settings, ship):
        self.screen = screen
        self.settings = settings

        self.rect = pygame.Rect(0, 0, settings.get_bullet_width(), settings.get_bullet_height())
        self.color = settings.get_bullet_color()
        self.rect.top = ship.rect.top
        self.rect.centerx = ship.rect.centerx

        self.trailingBlackRect = pygame.Rect(0, 0, settings.get_bullet_width(), 4)

        self.speed = settings.get_bullet_speed()

    def update(self):
        self.rect.y -= self.speed
        self.trailingBlackRect.left = self.rect.left
        self.trailingBlackRect.top = self.rect.bottom

    def blit(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        pygame.draw.rect(self.screen, self.settings.get_bg_color(), self.trailingBlackRect)


class AlienBullet(Bullet):
    def __init__(self, screen, settings, alien):
        super().__init__(screen, settings, alien)

    def update(self):
        self.rect.y += self.speed
        self.trailingBlackRect.left = self.rect.left
        self.trailingBlackRect.bottom = self.rect.top
