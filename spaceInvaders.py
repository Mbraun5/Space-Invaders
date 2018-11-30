import pygame
import os
import settings as se
import titleScreen as tS
import ship as sh
import gameFunctions as gF
import scoreboard as sb
import random


def run_game():
    #   Provides consistent window positioning. These settings center Pygame window for my computer.
    os.environ['SDL_VIDEO_WINDOW_POS'] = '60, 35'
    pygame.init()
    pygame.mouse.set_visible(False)     # Mouse is invisible until Title Sequence finishes animation.

    settings = se.Settings()
    screen = pygame.display.set_mode((settings.get_screen_width(), settings.get_screen_height()))
    pygame.display.set_caption(settings.get_game_title())

    screen.fill(settings.get_bg_color())
    title_screen = tS.TitleScreen(screen, settings)
    title_screen.title_loop()

    image_library = gF.load_image_library()
    beep_sounds, sound_library = gF.load_sounds()

    scoreboard = sb.ScoreBoard(screen, settings, image_library[0], title_screen)

    alien_list = []
    ship_bullet_list = []
    alien_bullet_list = []
    bunker_list = []
    ufo_list = []

    gF.create_bunkers(bunker_list, image_library, screen, settings)
    for bunker in bunker_list:
        bunker.blit()
    gF.create_fleet(alien_list, image_library, screen, settings)
    ship = sh.Ship(image_library, screen, settings, sound_library[2])

    counter = 0
    beep_counter = 0
    time_var = settings.get_time_var()
    while True:
        #   Now attached to title_screen. If you uncomment this, comment that one out or it's redundant.
        if settings.get_game_reset():
            alien_list = []
            bunker_list = []
            alien_list, bunker_list = gF.reset_game(alien_list, bunker_list, image_library, scoreboard, screen,
                                                    settings, ship)
            ufo_list = []
            alien_bullet_list = []
            ship_bullet_list = []
        gF.check_events(ship_bullet_list, screen, settings, ship, sound_library)
        ship.update()
        ufo_list = gF.update_bullets(alien_list, scoreboard, screen, settings, ship_bullet_list, sound_library,
                                     ufo_list)
        ufo_list = gF.update_ufo(ufo_list)
        beep_counter, counter, time_var = gF.update_aliens(alien_list, beep_counter, beep_sounds, bunker_list, counter,
                                                           image_library, scoreboard, screen, settings, time_var)
        if random.randint(1, settings.get_alien_fire_rate()) == 5:
            gF.create_alien_bullet(alien_list[random.randint(0, len(alien_list) - 1)], alien_bullet_list, screen,
                                   settings)
            a = random.randint(1, 25)
            if a is 5 and len(ufo_list) is 0:
                gF.create_ufo(image_library, scoreboard, screen, settings, sound_library, ufo_list)
        gF.update_alien_bullets(alien_bullet_list, alien_list, screen, settings)
        alien_bullet_list, ship_bullet_list = gF.check_collisions(alien_bullet_list, alien_list, bunker_list,
                                                                  screen, ship, ship_bullet_list, scoreboard)

        ship.draw_ship()
        scoreboard.display_scores()
        pygame.display.flip()


run_game()
