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

starting_timer = 60
count_down_bar_height = 400

while True:
    frames += 1
    seconds = frames / 30
    print(seconds)
    print(frames)                   # for time

    screen.fill(white)

    countdown = starting_timer - seconds
    # print(countdown)
    countdown_percentage = countdown / 100

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:  # this will stop printing mouse movement coordinate in console
            pass

        elif event.type == pygame.MOUSEBUTTONDOWN:
            pass

    screen.blit(img, (0, 0))

    # for countdown bar
    pygame.draw.rect(screen, white, (1200/2 - 20, 0, 40, 450))           # white backgrd of bar

    pygame.draw.rect(screen, blue, (600 - 15, 5, 30, count_down_bar_height * countdown_percentage))

    # rect for spotting difference
    pygame.draw.rect(screen, black, (170, 0, 200, 70), 2)
    pygame.draw.rect(screen, black, (0, 171, 0, 30), 2)
    pygame.draw.rect(screen, black, (140, 125, 10, 26), 2)


    time_label = myfont.render(str(int(countdown)), True, black)          # or str(int(seconds))
    screen.blit(time_label, (100, 100))                  # Displayed time

    pygame.draw.rect(screen, white, (0, 400, 1200, 20))  # background of text
    screen.blit(textsurface, (50, 400))

    clock.tick(40)
    pygame.display.update()   # game
