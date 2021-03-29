from random import randint
import pygame


def rules():
    new_screen = pygame.display.set_mode((500, 400))
    font = pygame.font.SysFont("Arial", 30)
    new_screen.blit(background, (0, 0))

    newrun = True
    while newrun:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                newrun = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if x >= 405 and x<=405+80 and y >= 350 and y <= 350+40:
                    newrun = False

        #heading
        new_screen.blit(font.render("Rules", False, (255, 255, 255)), (220, 10))

        #messages
        pygame.draw.rect(new_screen, (0, 0, 0), (10, 46, 484, 285))
        smallfont = pygame.font.SysFont("Arial", 23)
        message = "Lunar Lander 2.0 is a new version of the ATARI game 'Lunar lander' released in 1979. You are " \
                  "several meters away from the Moon's surface, and as a trained pilot we trust YOU to safely land" \
                  " our spaceship. However, the Moon's gravity is very strong, and in order to not blast into the " \
                  "Moon's surface you have to use your fuel to decrease the speed that you are falling   " \
                  "                                IMPORTANT NOTES:               You can use your fuel by hitting the" \
                  " arrow key up. You are also required to land on top of the Moon's base station and the maximum" \
                  " speed allowed to land is 10m/s                                    "
        count = 0
        beginning = 0
        y = 50
        for i in message:
            count += 1
            if (count >= 52 and i == " ") or i == "   ":
                if i == "   ":
                    count -= 1
                new_screen.blit(smallfont.render(message[beginning:(beginning+count)], False, (250, 250, 250)), (30, y))
                beginning = beginning + count
                count = 0
                y += 25

        pygame.draw.rect(new_screen, (50, 50, 250), (405, 350, 80, 40))
        new_screen.blit(font.render("Back", False, (0, 0, 0)), (415, 355))
        pygame.display.update()


def final_screen(results):
    new_screen = pygame.display.set_mode((500, 400))
    font = pygame.font.SysFont("Arial", 30)
    font = pygame.font.SysFont("Arial", 28)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if x >= 405 and x<=405+80 and y >= 300 and y <= 300+40:
                    return False
                if x >= 405 and x<=405+80 and y >= 350 and y <= 350+40:
                    return True

        new_screen.fill((255, 255, 220))
        if results:
            new_screen.blit(font.render("Well done youve managed to land safely!", True, (0, 0, 0)), (10, 10))
        else:
            new_screen.blit(font.render("Oh no! you are such a bad pilot", True, (0, 0, 0)), (10, 10))

        new_screen.blit(font.render("Wanna try again?", True, (0, 0, 0)), (15, 35))
        pygame.draw.rect(new_screen, (50, 50, 250), (405, 300, 80, 40))
        new_screen.blit(font.render("Menu", True, (255, 255, 255)), (415, 305))

        pygame.draw.rect(new_screen, (50, 50, 250), (405, 350, 80, 40))
        new_screen.blit(font.render("Back", True, (255, 255, 255)), (415, 355))

        pygame.display.update()


def checkwin(playerx, playery, targetx, targety, velocity):
    if (playerx > targetx-15 and playerx < targetx + 60) and (playery < targety + 5 and playery > targety - 15):
        if velocity > 10:
            print("speedy")
            return False
        else:
            print("won")
            return True

    elif playery > targety:
        print(f"player{playerx}, {playery}, target {targetx}, {targety} ")
        print("didnt fall on top")
        return False
    else:
        return None


def player_pos():
    playerx = randint(50, 450)
    playery = 15
    return playerx, playery


def gameinfo():
    acc = 0.3
    velocity = 1
    return acc, velocity


def target_pos():
    targetx = randint(50, 450)
    targety = 350
    return targetx, targety


def play():
    new_screen = pygame.display.set_mode((500, 400))
    font = pygame.font.SysFont("Arial", 30)

    #player
    player = pygame.image.load("player.png")
    playerx, playery = player_pos()

    #target
    target = pygame.image.load("target.png")
    targetx, targety = target_pos()

    acc, velocity = gameinfo()

    new_run = True
    while new_run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                new_run = False

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    playerx -= 10

                elif event.key == pygame.K_RIGHT:
                    playerx += 10

                elif event.key == pygame.K_UP:
                    velocity -= 3

        new_screen.fill((220, 255, 255))
        playery += velocity*acc
        current_vel = (f"Velocity(m/s): {velocity}")
        new_screen.blit(font.render(current_vel, True, (0, 0, 0)), (0, 0))
        velocity += 1

        new_screen.blit(player, (playerx, playery))
        new_screen.blit(target, (targetx, targety))
        final = checkwin(playerx, playery, targetx, targety, velocity)
        if final is not None:
            new_run = final_screen(final)
            playerx, playery = player_pos()
            targetx, targety = target_pos()
            acc, velocity = gameinfo()

        pygame.time.delay(100)
        pygame.display.update()


def button(screen, x, y, w, h, text, func=None):
    font = pygame.font.SysFont("Arial", 30)
    xpos, ypos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    light = (10, 10, 10)
    dark = (80, 80, 80)

    if (xpos >= x and xpos <= x+w) and (ypos >= y and ypos <= y+h):
        pygame.draw.rect(screen, dark, (x, y, w, h))
        if click[0]:
            func()
    else:
        pygame.draw.rect(screen, light, (x, y, w, h))
    screen.blit(font.render(text, True, (255, 255, 255)), (x+10, y+4))


def main():
    global background
    screen = pygame.display.set_mode((500, 400))
    font = pygame.font.SysFont("Arial", 30)
    background = pygame.image.load("sky.jpg")
    icon = pygame.image.load("icon.jpg")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(background, (0, 0))
        screen.blit(icon, (190, 100))
        screen.blit(font.render("Lunar Lander 2.0", True, (255, 255, 255)), (165, 50))

        button(screen, 215, 300, 80, 40, "Rules", func=rules)
        button(screen, 215, 350, 80, 40, "Play", func=play)
        pygame.display.update()


if __name__ == "__main__":
    pygame.init()
    main()
    pygame.quit()
