import sys
import pygame
import alien as a
import bullet as b
import bunker as bu
import time
import ufo as u


def fire_bullet(bullet_list, screen, settings, ship, sound_library):
    if settings.get_shooting_flag():
        if len(bullet_list) < 1:
            pygame.mixer.Sound.play(sound_library[0])
            new_bullet = b.Bullet(screen, settings, ship)
            bullet_list.append(new_bullet)


def check_key_down_events(event, settings, ship):
    if event.key == pygame.K_RIGHT:
        ship.movingRight = True
    elif event.key == pygame.K_LEFT:
        ship.movingLeft = True
    elif event.key == pygame.K_SPACE:
        settings.set_shooting_flag(True)
    elif event.key == pygame.K_q:
        sys.exit()


def check_key_up_events(event, settings, ship):
    if event.key == pygame.K_RIGHT:
        ship.movingRight = False
    elif event.key == pygame.K_LEFT:
        ship.movingLeft = False
    elif event.key == pygame.K_SPACE:
        settings.set_shooting_flag(False)


def check_events(bullet_list, screen, settings, ship, sound_library):
    #   Responds to key presses and mouse events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_key_down_events(event, settings, ship)
        elif event.type == pygame.KEYUP:
            check_key_up_events(event, settings, ship)
    fire_bullet(bullet_list, screen, settings, ship, sound_library)


def load_sounds():
    #   Beeps must be in separate list because as ships aliens up the beep sound follows them.
    beep_list = [pygame.mixer.Sound('Sounds/Beep1.wav'), pygame.mixer.Sound('Sounds/Beep2.wav'),
                 pygame.mixer.Sound('Sounds/Beep3.wav'), pygame.mixer.Sound('Sounds/Beep4.wav')]
    for sound in beep_list:
        sound.set_volume(0.6)
    sound_library = [pygame.mixer.Sound('Sounds/Fire Bullet.wav'), pygame.mixer.Sound('Sounds/Alien Explosion.wav'),
                     pygame.mixer.Sound('Sounds/Ship Explosion.wav'), pygame.mixer.Sound('Sounds/UFO.wav')]
    for sound in sound_library:
        sound.set_volume(0.4)
    return beep_list, sound_library


def load_image_library():
    image_library = [pygame.image.load('Images/Ship.png'), pygame.image.load('Images/UFO.png'),
                     pygame.image.load('Images/Purple Alien1.png'), pygame.image.load('Images/Purple Alien2.png'),
                     pygame.image.load('Images/Blue Alien1.png'), pygame.image.load('Images/Blue Alien2.png'),
                     pygame.image.load('Images/Green Alien1.png'), pygame.image.load('Images/Green Alien2.png'),
                     pygame.image.load('Images/Purple Explode1.png'), pygame.image.load('Images/Purple Explode2.png'),
                     pygame.image.load('Images/Purple Explode3.png'), pygame.image.load('Images/Blue Explode1.png'),
                     pygame.image.load('Images/Blue Explode2.png'), pygame.image.load('Images/Blue Explode3.png'),
                     pygame.image.load('Images/Green Explode1.png'), pygame.image.load('Images/Green Explode2.png'),
                     pygame.image.load('Images/Green Explode3.png'), pygame.image.load('Images/Bunker.png'),
                     pygame.image.load('Images/Ship Explode1.png'), pygame.image.load('Images/Ship Explode2.png'),
                     pygame.image.load('Images/Ship Explode3.png'), pygame.image.load('Images/Ship Explode4.png'),
                     pygame.image.load('Images/Ship Explode5.png'), pygame.image.load('Images/Ship Explode6.png'),
                     pygame.image.load('Images/Ship Explode7.png'), pygame.image.load('Images/Ship Explode8.png')]
    return image_library


def create_bunkers(bunker_list, image_library, screen, settings):
    for i in range(1, 5):
        new_bunker = bu.Bunker(screen, settings, image_library[17])
        new_bunker.change_rect(100 + 400 * (i - 1), settings.get_screen_height() * 3 / 4)
        bunker_list.append(new_bunker)


def draw_bunker(bunker_list):
    for bunker in bunker_list:
        bunker.blit()


def check_bullet_bunker_collision(alien_bullet_list, bunker_list, ship_bullet_list):
    for bul_index, bullet in enumerate(ship_bullet_list):
        for bunk_index, bunker in enumerate(bunker_list):
            if bullet.rect.colliderect(bunker.rect):
                if bunker.check_collision(bullet):
                    bullet.color = (0, 0, 0)
                    bullet.blit()
                    pygame.display.flip()
                    del ship_bullet_list[bul_index]
                    break
            if bunker.durability < 0:
                bunker.blackout()
                pygame.display.flip()
                del bunker_list[bunk_index]
    for bul_index, bullet in enumerate(alien_bullet_list):
        for bunk_index, bunker in enumerate(bunker_list):
            if bullet.rect.colliderect(bunker.rect):
                if bunker.check_collision(bullet):
                    bullet.color = (0, 0, 0)
                    bullet.blit()
                    pygame.display.flip()
                    del alien_bullet_list[bul_index]
                    break
            if bunker.durability < 0:
                bunker.blackout()
                pygame.display.flip()
                del bunker_list[bunk_index]


def check_ship_bullet_collision(alien_bullet_list, ship, scoreboard):
    for index, bullet in enumerate(alien_bullet_list):
        if bullet.rect.colliderect(ship.rect):
            ship.explode()
            scoreboard.update_lives(-1)
            del alien_bullet_list[index]
            return True
    return False


def check_collisions(alien_bullet_list, alien_list, bunker_list, screen, ship, ship_bullet_list, scoreboard):
    check_bullet_bunker_collision(alien_bullet_list, bunker_list, ship_bullet_list)
    if check_ship_bullet_collision(alien_bullet_list, ship, scoreboard):
        alien_bullet_list = []
        ship_bullet_list = []
        screen.fill((0, 0, 0))
        for bunker in bunker_list:
            bunker.blit()
        ship.draw_ship()
        scoreboard.display_scores()
        for alien in alien_list:
            alien.blit()
        pygame.display.flip()
        time.sleep(1)
    return alien_bullet_list, ship_bullet_list


def create_fleet(alien_list, image_library, screen, settings):
    create_purple_aliens(alien_list, image_library, screen, settings)
    create_blue_aliens(alien_list, image_library, screen, settings)
    create_green_aliens(alien_list, image_library, screen, settings)

    for alien in alien_list:
        alien.blit()
    pygame.display.flip()


def create_purple_aliens(alien_list, image_library, screen, settings):
    purple_one = a.PurpleAlien(screen, settings, image_library[2], image_library[3], image_library[8], image_library[9],
                               image_library[10])
    purple_one.rect.x = 100
    purple_one.rect.y = 100
    purple_two = a.PurpleAlien(screen, settings, image_library[2], image_library[3], image_library[8], image_library[9],
                               image_library[10])
    purple_two.rect.x = 100
    purple_two.rect.top = purple_one.rect.bottom
    alien_list.append(purple_one)
    for counter in range(1, 11):
        if counter % 11 == 0:
            alien_list.append(purple_two)
        else:
            new_alien = a.PurpleAlien(screen, settings, image_library[2], image_library[3], image_library[8],
                                      image_library[9], image_library[10])
            if counter % 2 == 0:
                new_alien.swap_images()
            new_alien.rect.left = alien_list[counter-1].rect.right
            new_alien.rect.top = alien_list[counter-1].rect.top
            alien_list.append(new_alien)


def create_blue_aliens(alien_list, image_library, screen, settings):
    blue_one = a.BlueAlien(screen, settings, image_library[4], image_library[5], image_library[11], image_library[12],
                           image_library[13])
    blue_one.rect.x = 100
    blue_one.rect.top = alien_list[0].rect.bottom
    blue_two = a.BlueAlien(screen, settings, image_library[4], image_library[5], image_library[11], image_library[12],
                           image_library[13])
    blue_two.rect.x = 100
    blue_two.rect.top = blue_one.rect.bottom
    alien_list.append(blue_one)
    for counter in range(12, 33):
        if counter % 11 == 0:
            alien_list.append(blue_two)
        else:
            new_alien = a.BlueAlien(screen, settings, image_library[4], image_library[5], image_library[11],
                                    image_library[12], image_library[13])
            if counter % 2 == 0:
                new_alien.swap_images()
            new_alien.rect.left = alien_list[counter-1].rect.right
            new_alien.rect.top = alien_list[counter-1].rect.top
            alien_list.append(new_alien)


def create_green_aliens(alien_list, image_library, screen, settings):
    green_one = a.GreenAlien(screen, settings, image_library[6], image_library[7], image_library[14], image_library[15],
                             image_library[16])
    green_one.rect.x = 100
    green_one.rect.top = alien_list[32].rect.bottom
    green_two = a.GreenAlien(screen, settings, image_library[6], image_library[7], image_library[14], image_library[15],
                             image_library[16])
    green_two.rect.x = 100
    green_two.rect.top = green_one.rect.bottom
    alien_list.append(green_one)
    for counter in range(34, 55):
        if counter % 11 == 0:
            alien_list.append(green_two)
        else:
            new_alien = a.GreenAlien(screen, settings, image_library[6], image_library[7], image_library[14],
                                     image_library[15], image_library[16])
            if counter % 2 == 0:
                new_alien.swap_images()
            new_alien.rect.left = alien_list[counter-1].rect.right
            new_alien.rect.top = alien_list[counter-1].rect.top
            alien_list.append(new_alien)


def change_fleet_direction(alien_list, settings):
    settings.change_alien_direction()
    for alien in alien_list:
        alien.rect.y += settings.get_alien_drop()


def check_fleet_edges(alien_list, settings):
    for alien in alien_list:
        if alien.check_edges():
            change_fleet_direction(alien_list, settings)
            break


def create_alien_bullet(alien, alien_bullet_list, screen, settings):
    new_bullet = b.AlienBullet(screen, settings, alien)
    alien_bullet_list.append(new_bullet)


def update_aliens(alien_list, beep_counter, beep_sounds, bunker_list, counter, image_library,
                  scoreboard, screen, settings, time_var):
    if counter == time_var:
        screen.fill(settings.get_bg_color())
        for bunker in bunker_list:
            bunker.blit()
        for alien in alien_list:
            if not alien.exploding:
                alien.swap_images()
                alien.update()
                alien.blit()
        pygame.mixer.Sound.play(beep_sounds[beep_counter])
        beep_counter += 1
        beep_counter = beep_counter % 4             # There are 4 sounds, so 0-3 in the list. Mod4 keeps sounds playing.
        if beep_counter == 3 and time_var > 25:
            settings.increase_fire_rate(1)
            time_var -= 1
        check_fleet_edges(alien_list, settings)
    if counter % 20 == 0:
        for index, alien in enumerate(alien_list):
            if alien.exploding:
                alien.show_next_explode()
            if alien.dead:
                del alien_list[index]
                if len(alien_list) == 0:
                    create_fleet(alien_list, image_library, screen, settings)
                    beep_counter = 0
                    time_var = settings.get_time_var()
                    scoreboard.update_lives(1)
    if counter > time_var:
        counter = 0
    else:
        counter += 1
    #   These are passed by value, not reference, so must be returned for this loop.
    return beep_counter, counter, time_var


def check_bullet_alien_collisions(alien_list, scoreboard, settings, ship_bullet_list, sound_library):
    for bullet_index, bullet in enumerate(ship_bullet_list):
        for alien_index, alien in enumerate(alien_list):
            if bullet.rect.colliderect(alien.rect):
                bullet.color = settings.get_bg_color()
                bullet.blit()
                if len(ship_bullet_list) > 0:
                    del ship_bullet_list[bullet_index]
                alien.exploding = True
                scoreboard.update_score(alien.get_value())
                pygame.mixer.Sound.play(sound_library[1])


def check_bullet_ufo_collisions(ship_bullet_list, ufo_list):
    for bullet in ship_bullet_list:
        for ufo in ufo_list:
            if bullet.rect.colliderect(ufo.rect):
                ufo.explode()
                ufo_list = []
    return ufo_list


def update_bullets(alien_list, scoreboard, screen, settings, ship_bullet_list, sound_library, ufo_list):
    for index, bullet in enumerate(ship_bullet_list):
        bullet.update()
        bullet.blit()
        if bullet.rect.top <= screen.get_rect().top:
            bullet.color = settings.get_bg_color()
            bullet.blit()
            pygame.display.flip()
            del ship_bullet_list[index]
    check_bullet_alien_collisions(alien_list, scoreboard, settings, ship_bullet_list, sound_library)
    ufo_list = check_bullet_ufo_collisions(ship_bullet_list, ufo_list)
    return ufo_list


def update_alien_bullets(alien_bullet_list, alien_list, screen, settings):
    for index, bullet in enumerate(alien_bullet_list):
        bullet.update()
        if bullet.rect.top > alien_list[len(alien_list) - 1].rect.bottom:
            bullet.blit()
        if bullet.rect.top <= screen.get_rect().top:
            bullet.color = settings.get_bg_color()
            bullet.blit()
            pygame.display.flip()
            del alien_bullet_list[index]


def append_score(current_score):
    score_list = []
    try:
        with open('high score.txt', 'r') as f:
            new_one = f.readline()
            while new_one != "":
                score_list.append(int(new_one))
                new_one = f.readline()
            score_list.append(int(current_score))
            score_list.sort(reverse=True)
            while len(score_list) > 10:
                del (score_list[10])
            print(score_list)
            f.close()
        with open('high score.txt', 'w') as f:
            for line in score_list:
                f.write(str(line))
                f.write("\n")
            f.close()
    except FileNotFoundError:
        with open('high score.txt', 'w') as f:
            f.write(current_score)


def reset_game(alien_list, bunker_list, image_library, scoreboard, screen, settings, ship):
    create_fleet(alien_list, image_library, screen, settings)
    create_bunkers(bunker_list, image_library, screen, settings)
    screen.fill(settings.get_bg_color())
    pygame.display.flip()
    settings.set_reset(False)
    ship.movingLeft = False
    ship.movingRight = False
    scoreboard.numberOfLives = 3
    return alien_list, bunker_list


def wait_for_space():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                return False
            elif event.key == pygame.K_q:
                sys.exit(0)
    return True


def create_ufo(image_library, scoreboard, screen, settings, sound_library, ufo_list):
    new_ufo = u.UFO(image_library[1], scoreboard, screen, settings, sound_library[3])
    ufo_list.append(new_ufo)


def update_ufo(ufo_list):
    for ufo in ufo_list:
        ufo.update()
        ufo.blit()
        if ufo.check_bounds():
            ufo_list = []
    return ufo_list
