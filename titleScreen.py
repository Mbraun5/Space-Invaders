import pygame
import time
import gameFunctions as gF


class TitleScreen:
    def __init__(self, screen, settings):
        self.__screen = screen
        self.__settings = settings
        self.__font = pygame.font.SysFont('impact', 200)
        self.__space_text = self.__font.render('SPACE', False, (255, 255, 255))
        self.__invaders_text = self.__font.render('INVADERS', False, (0, 255, 0))

        self.__playImageWhite = pygame.image.load('Images/playbuttonwhite.png')
        self.__playRectWhite = self.__playImageWhite.get_rect()
        self.__playRectWhite.bottom = self.__settings.get_screen_height() - 125
        self.__playRectWhite.centerx = self.__settings.get_screen_width() / 2

        self.__playImageGreen = pygame.image.load('Images/playbuttongreen.png')
        self.__playRectGreen = self.__playImageGreen.get_rect()
        self.__playRectGreen.bottom = self.__playRectWhite.bottom
        self.__playRectGreen.centerx = self.__playRectWhite.centerx

        self.__highScoresImageWhite = pygame.image.load('Images/High Scores White.png')
        self.__whiteScoresRect = self.__highScoresImageWhite.get_rect()
        self.__whiteScoresRect.top = self.__playRectGreen.bottom + 5
        self.__whiteScoresRect.centerx = self.__playRectGreen.centerx

        self.__highScoresImageGreen = pygame.image.load('Images/High Scores Green.png')
        self.__greenScoresRect = self.__highScoresImageGreen.get_rect()
        self.__greenScoresRect.top = self.__whiteScoresRect.top
        self.__greenScoresRect.centerx = self.__whiteScoresRect.centerx

        #   #######################################################################
        #           Alien Images and Rects                                        #
        ###########################################################################
        self.__ufoAlienImage = pygame.image.load('Images/ufo.png')
        self.__ufoAlienRect = self.__ufoAlienImage.get_rect()
        self.__ufoAlienRect.bottom = self.__playRectWhite.top - 10
        self.__ufoAlienRect.centerx = self.__playRectWhite.centerx - 150

        self.__purpleAlienImage = pygame.image.load('Images/Purple Alien1.png')
        self.__purpleAlienRect = self.__purpleAlienImage.get_rect()
        self.__purpleAlienRect.bottom = self.__ufoAlienRect.top
        self.__purpleAlienRect.centerx = self.__ufoAlienRect.centerx

        self.__blueAlienImage = pygame.image.load('Images/Blue Alien1.png')
        self.__blueAlienRect = self.__blueAlienImage.get_rect()
        self.__blueAlienRect.bottom = self.__purpleAlienRect.top
        self.__blueAlienRect.centerx = self.__purpleAlienRect.centerx

        self.__greenAlienImage = pygame.image.load('Images/Green Alien1.png')
        self.__greenAlienRect = self.__greenAlienImage.get_rect()
        self.__greenAlienRect.bottom = self.__blueAlienRect.top
        self.__greenAlienRect.centerx = self.__blueAlienRect.centerx

        #   #######################################################################
        #           Point Images and Rects                                        #
        ###########################################################################
        self.__tenPointsImage = pygame.image.load('Images/ten points.png')
        self.__tenPointsRect = self.__tenPointsImage.get_rect()
        self.__tenPointsRect.left = self.__greenAlienRect.right
        self.__tenPointsRect.centery = self.__greenAlienRect.centery

        self.__twentyPointsImage = pygame.image.load('Images/twenty points.png')
        self.__twentyPointsRect = self.__twentyPointsImage.get_rect()
        self.__twentyPointsRect.left = self.__blueAlienRect.right
        self.__twentyPointsRect.centery = self.__blueAlienRect.centery

        self.__fortyPointsImage = pygame.image.load('Images/forty points.png')
        self.__fortyPointsRect = self.__fortyPointsImage.get_rect()
        self.__fortyPointsRect.left = self.__purpleAlienRect.right
        self.__fortyPointsRect.centery = self.__purpleAlienRect.centery

        self.__unknownPointsImage = pygame.image.load('Images/unknown points.png')
        self.__unknownPointsRect = self.__unknownPointsImage.get_rect()
        self.__unknownPointsRect.left = self.__ufoAlienRect.right
        self.__unknownPointsRect.centery = self.__ufoAlienRect.centery

        self.create_high_score_file()

    def title_loop(self):
        self.__screen.fill(self.__settings.get_bg_color())
        self.__screen.blit(self.__space_text, (self.__settings.get_screen_width() / 2.75, 0))
        self.__screen.blit(self.__invaders_text, (self.__settings.get_screen_width() / 3.35, 175))
        self.__screen.blit(self.__playImageWhite, self.__playRectWhite)
        self.__screen.blit(self.__highScoresImageWhite, self.__whiteScoresRect)
        pygame.display.flip()

        self.__screen.blit(self.__greenAlienImage, self.__greenAlienRect)
        pygame.display.flip()
        time.sleep(0.25)
        self.__screen.blit(self.__tenPointsImage, self.__tenPointsRect)
        pygame.display.flip()
        time.sleep(0.25)
        self.__screen.blit(self.__blueAlienImage, self.__blueAlienRect)
        pygame.display.flip()
        time.sleep(0.25)
        self.__screen.blit(self.__twentyPointsImage, self.__twentyPointsRect)
        pygame.display.flip()
        time.sleep(0.25)
        self.__screen.blit(self.__purpleAlienImage, self.__purpleAlienRect)
        pygame.display.flip()
        time.sleep(0.25)
        self.__screen.blit(self.__fortyPointsImage, self.__fortyPointsRect)
        pygame.display.flip()
        time.sleep(0.25)
        self.__screen.blit(self.__ufoAlienImage, self.__ufoAlienRect)
        pygame.display.flip()
        time.sleep(0.25)
        self.__screen.blit(self.__unknownPointsImage, self.__unknownPointsRect)
        pygame.display.flip()
        time.sleep(0.25)
        pygame.mouse.set_visible(True)

        while self.check_mouse_events():
            if self.__playRectWhite.collidepoint(pygame.mouse.get_pos()):
                self.__screen.blit(self.__playImageGreen, self.__playRectGreen)
                self.__screen.blit(self.__highScoresImageWhite, self.__whiteScoresRect)
            elif self.__whiteScoresRect.collidepoint(pygame.mouse.get_pos()):
                self.__screen.blit(self.__highScoresImageGreen, self.__greenScoresRect)
                self.__screen.blit(self.__playImageWhite, self.__playRectWhite)
            else:
                self.__screen.blit(self.__playImageWhite, self.__playRectWhite)
                self.__screen.blit(self.__highScoresImageWhite, self.__whiteScoresRect)
            pygame.display.flip()

    def check_mouse_events(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.__playRectGreen.collidepoint(pygame.mouse.get_pos()):
                    self.__screen.fill(self.__settings.get_bg_color())
                    return False
                elif self.__greenScoresRect.collidepoint(pygame.mouse.get_pos()):
                    self.high_score_screen()
                    self.title_loop()
                    return False
        return True

    def high_score_screen(self):
        self.__screen.fill(self.__settings.get_bg_color())
        font = pygame.font.Font('Fonts/PixFont.ttf', 40)
        text_color = self.__settings.get_bullet_color()
        image_rect = None
        image_one_rect = None
        high_score_image = font.render("HIGH SCORES!", True, text_color, self.__settings.get_bg_color())
        high_score_rect = high_score_image.get_rect()
        high_score_rect.centerx = self.__settings.get_screen_width() / 2
        high_score_rect.y = 100
        self.__screen.blit(high_score_image, high_score_rect)
        pygame.display.flip()
        try:
            with open("high score.txt") as f:
                score = f.readline()
                if score == "":
                    return
                score = score.strip('\n')
                image_one = font.render("Score: {}".format(score), True, text_color, self.__settings.get_bg_color())
                image_one_rect = image_one.get_rect()
                image_one_rect.centerx = self.__settings.get_screen_width() / 2
                image_one_rect.y = 200
                self.__screen.blit(image_one, image_one_rect)
                pygame.display.flip()
                time.sleep(0.2)
                for count in range(0, 10):
                    score = f.readline()
                    if score == "":
                        break
                    score = score.strip('\n')
                    image = font.render("Score: {}".format(score), True, text_color, self.__settings.get_bg_color())
                    image_rect = image.get_rect()
                    image_rect.left = image_one_rect.left
                    image_rect.top = image_one_rect.bottom
                    image_one_rect = image_rect
                    self.__screen.blit(image, image_rect)
                    pygame.display.flip()
                    time.sleep(0.2)
        except FileNotFoundError:
            pass
        continue_image = font.render("PRESS SPACE TO CONTINUE, Q TO EXIT", True, text_color)
        continue_rect = continue_image.get_rect()
        try:
            continue_rect.centerx = image_rect.centerx
            continue_rect.top = image_rect.bottom + 50
        except AttributeError:
            continue_rect.centerx = image_one_rect.centerx
            continue_rect.top = image_one_rect.bottom + 50
        self.__screen.blit(continue_image, continue_rect)
        pygame.display.flip()
        while gF.wait_for_space():
            continue

    @staticmethod
    #   Ensures a high score file is inside directory. If one is not there, makes one. If it is there, it does nothing.
    def create_high_score_file():
        try:
            with open('high score.txt', 'r') as f:
                f.close()
        except FileNotFoundError:
            with open('high score.txt', 'w') as f:
                f.write("0000")
