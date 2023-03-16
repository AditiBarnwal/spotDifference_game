import pygame

pygame.init()  # pygame initialization

myfont = pygame.font.SysFont("CosmicSana MS", 30)
screen = pygame.display.set_mode((1200, 418))
clock = pygame.time.Clock()

red = (255, 23, 10)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)

img = pygame.image.load('spot difference images globe - Google Search (1).png')
textsurface = myfont.render("spot difference between these images", True, black)

frames = 0

starting_timer = 60                           # for countdownbar
count_down_bar_height = 400                   # for countdownbar

difference_rectangle = [(170, 0, 200, 70), (0, 171, 0, 30), (140, 125, 10, 26)]
found_difference = []
penalty_seconds = 0
while True:
    frames += 1
    seconds = frames / 30
    # print(seconds)
    # print(frames)                   # for time

    screen.fill(white)

    countdown = starting_timer - seconds - penalty_seconds
    # print(countdown)
    countdown_percentage = countdown / 100

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:  # this will stop printing mouse movement coordinate in console
            pass

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            print(mouse_pos)
            missed = 0
            for i, rect in enumerate(difference_rectangle):
                if mouse_pos[0] > rect[0] and mouse_pos[0] < rect[0] + rect[2] \
                    and mouse_pos[1] > rect[1] and mouse_pos[1] < rect[1] + rect[3]:
                    print("Got it")
                    found_difference.append(i)
                else:
                    print("U missed it!")
                    missed +=1
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
