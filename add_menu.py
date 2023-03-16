import pygame

pygame.init()  # pygame initialization

myfont = pygame.font.SysFont("CosmicSana MS", 30)
title_font = pygame.font.SysFont("CosmicSana MS", 45)            # for menu bar

ok_sound = pygame.mixer.Sound('success-1-6297.mp3')
failed_sound = pygame.mixer.Sound('error-sound-39539.mp3')

screen = pygame.display.set_mode((1200, 418))
clock = pygame.time.Clock()

red = (255, 23, 10)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)

img = pygame.image.load('spot difference images globe - Google Search (1).png')
textsurface = myfont.render("spot difference between these images", True, black)
menu_title = title_font.render('Welcome to spot differences', True, black)       # for menu
start_text = myfont.render('Click anywhere on the screen to start the game', True, black)
pause_text = myfont.render('Press button p from keyword to pause game', True, black)

frames = 0

starting_timer = 60                           # for countdownbar
count_down_bar_height = 400                   # for countdownbar

difference_rectangle = [(170, 0, 200, 70), (0, 171, 0, 30), (140, 125, 10, 26)]
found_difference = []
penalty_seconds = 0

menu = True
while True:
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.quit:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    menu = False


        screen.fill(white)
        screen.blit(menu_title, (190, 50))
        screen.blit(start_text, (100, 150))
        screen.blit(pause_text, (130, 180))

        clock.tick(30)
        pygame.display.update()

    frames += 1
    seconds = frames / 30
    # print(seconds)
    # print(frames)                   # for time

    countdown = starting_timer - seconds - penalty_seconds
    # print(countdown)
    countdown_percentage = countdown / 100

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:  # this will stop printing mouse movement coordinate in console
            if event.key == pygame.K_p:
                menu = True

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            print(mouse_pos)
            missed = 0
            for i, rect in enumerate(difference_rectangle):
                if mouse_pos[0] > rect[0] and mouse_pos[0] < rect[0] + rect[2] \
                    and mouse_pos[1] > rect[1] and mouse_pos[1] < rect[1] + rect[3]:
                    print("Got it")
                    found_difference.append(i)
                    pygame.mixer.Sound.play(ok_sound)
                else:
                    print("U missed it!")
                    missed +=1
                    pygame.mixer.Sound.play(failed_sound)
            if missed == 3:
                penalty_seconds += 5
        print(countdown)

    screen.blit(img, (0, 0))

    # for countdown bar
    pygame.draw.rect(screen, white, (1200/2 - 20, 0, 40, 450))           # white backgrd of bar

    pygame.draw.rect(screen, blue, (600 - 15, 5, 30, count_down_bar_height * countdown_percentage))

    for f in found_difference:
        # print(f)
        rect = difference_rectangle[f]
        pygame.draw.rect(screen,black, rect, 3)

    pygame.draw.rect(screen, white, (0, 400, 1200, 20))  # background of text
    screen.blit(textsurface, (50, 400))

    clock.tick(40)
    pygame.display.update()   # game
