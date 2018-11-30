import pygame
import gameFunctions as gF


def get_high_score_value():
    try:
        with open('high score.txt', 'r') as f:
            high_score_value = int(f.readline())
            high_score_str = str(high_score_value)
            if high_score_value < 1000:
                if high_score_value < 100:
                    if high_score_value < 10:
                        high_score_str = "000" + str(high_score_value)
                        return high_score_str
                    high_score_str = "00" + str(high_score_value)
                    return high_score_str
                high_score_str = "0" + str(high_score_value)
    except FileNotFoundError:
        high_score_str = '0000'
    return high_score_str


class ScoreBoard:
    def __init__(self, screen, settings, ship_image, title_screen):
        self.__titleScreen = title_screen
        self.__screen = screen
        self.__settings = settings
        self.__screenRect = self.__screen.get_rect()

        #   Text Settings
        self.textColor = self.__settings.get_bullet_color()
        self.font = pygame.font.Font('Fonts/PixFont.ttf', 30)

        #   Current Score Image
        self.currentScore = '0000'
        self.currentScoreImage = self.font.render("SCORE: {}".format(self.currentScore), True, self.textColor,
                                                  self.__settings.get_bg_color())
        self.currentScoreRect = self.currentScoreImage.get_rect()
        self.currentScoreRect.top = self.__screenRect.top
        self.currentScoreRect.x = self.__screenRect.x + 20

        #   High Score Image
        self.high_score_value = get_high_score_value()
        self.highScoreValueImage = self.font.render("HIGH SCORE: {}".format(self.high_score_value), True,
                                                    self.textColor, self.__settings.get_bg_color())
        self.highScoreValueRect = self.highScoreValueImage.get_rect()
        self.highScoreValueRect.top = self.__screenRect.top
        self.highScoreValueRect.x = self.__settings.get_screen_width() / 3

        #   Lives Image
        self.numberOfLives = 3
        self.livesTextImage = self.font.render("LIVES:", True, self.textColor, self.__settings.get_bg_color())
        self.livesTextRect = self.livesTextImage.get_rect()
        self.livesTextRect.top = self.__screenRect.top
        self.livesTextRect.x = self.__settings.get_screen_width() * 2 / 3

        #   Ship Image for Lives
        self.__shipImage = pygame.transform.scale(ship_image, (60, 40))
        self.__shipRect = self.__shipImage.get_rect()
        self.__shipRect.top = self.livesTextRect.top
        self.__shipRect.left = self.livesTextRect.right
        self.__shipRectList = [self.__shipRect]

        self.prep_lives()

    def prep_scores(self):
        self.currentScoreImage = self.font.render("SCORE: {}".format(self.currentScore), True, self.textColor,
                                                  self.__settings.get_bg_color())
        self.currentScoreRect = self.currentScoreImage.get_rect()
        self.currentScoreRect.top = self.__screenRect.top
        self.currentScoreRect.x = self.__screenRect.x + 20

        if int(self.currentScore) > int(self.high_score_value):
            self.high_score_value = self.currentScore
            self.highScoreValueImage = self.font.render("HIGH SCORE: {}".format(self.high_score_value), True,
                                                        self.textColor, self.__settings.get_bg_color())
            self.highScoreValueRect = self.highScoreValueImage.get_rect()
            self.highScoreValueRect.top = self.__screenRect.top
            self.highScoreValueRect.x = self.__settings.get_screen_width() / 3

    def update_lives(self, value):
        if self.numberOfLives < 7:
            self.numberOfLives += value
            self.prep_lives()
        if self.numberOfLives <= 0:
            self.game_over()

    def game_over(self):
        pygame.mixer.stop()
        font = pygame.font.Font('Fonts/PixFont.ttf', 45)
        current_score = self.currentScore
        high_score = self.high_score_value
        if current_score > high_score:
            self.high_score_value = current_score
        game_over_image = font.render("GAME OVER", True, self.textColor)
        game_over_rect = game_over_image.get_rect()
        game_over_rect.centerx = self.__screenRect.centerx
        game_over_rect.y = self.__settings.get_screen_height() / 8

        high_score_image = font.render("HIGH SCORE:{}".format(high_score), True, self.textColor)
        high_score_rect = high_score_image.get_rect()
        high_score_rect.centerx = game_over_rect.centerx
        high_score_rect.top = game_over_rect.bottom + 150

        current_score_image = font.render("CURRENT SCORE:{}".format(current_score), True, self.textColor)
        current_score_rect = current_score_image.get_rect()
        current_score_rect.centerx = game_over_rect.centerx
        current_score_rect.top = high_score_rect.bottom + 150

        continue_image = font.render("PRESS SPACE TO CONTINUE, Q TO EXIT".format(current_score), True, self.textColor)
        continue_rect = continue_image.get_rect()
        continue_rect.centerx = current_score_rect.centerx
        continue_rect.top = current_score_rect.bottom + 150

        self.currentScore = 0
        while gF.wait_for_space():
            self.__screen.fill(self.__settings.get_bg_color())
            self.__screen.blit(game_over_image, game_over_rect)
            self.__screen.blit(high_score_image, high_score_rect)
            self.__screen.blit(current_score_image, current_score_rect)
            self.__screen.blit(continue_image, continue_rect)
            pygame.display.flip()

        gF.append_score(current_score)
        self.__settings.set_reset(True)
        self.__titleScreen.title_loop()

    def prep_lives(self):
        self.__shipRectList = [self.__shipRect]
        for i in range(2, self.numberOfLives + 1):
            new_rect = self.__shipRectList[i - 2].copy()
            new_rect.left = self.__shipRectList[i - 2].right
            self.__shipRectList.append(new_rect)

    def display_scores(self):
        self.prep_lives()
        self.prep_scores()
        self.__screen.blit(self.currentScoreImage, self.currentScoreRect)
        self.__screen.blit(self.highScoreValueImage, self.highScoreValueRect)
        self.__screen.blit(self.livesTextImage, self.livesTextRect)
        for i in range(0, self.numberOfLives):
            self.__screen.blit(self.__shipImage, self.__shipRectList[i])

    def update_score(self, value):
        int_score = int(self.currentScore)
        int_score += value
        if int_score < 1000:
            if int_score < 100:
                if int_score < 10:
                    self.currentScore = "000" + str(int_score)
                    return
                self.currentScore = "00" + str(int_score)
                return
            self.currentScore = "0" + str(int_score)
        self.currentScore = str(int_score)
