import pygame

pygame.init()  # pygame initialization

myfont = pygame.font.SysFont("CosmicSana MS", 30)
screen = pygame.display.set_mode((1200, 480))
clock = pygame.time.Clock()

red = (255,23, 10)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)

img = pygame.image.load('spot difference images globe - Google Search (1).png')
textsurface = myfont.render("spotted 3 difference between these images", True, black)

while True:
    screen.fill(white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:  # this will stop printing mouse movement coordinate in console
            pass

        elif event.type == pygame.MOUSEBUTTONDOWN:
            pass

    screen.blit(img, (0, 0))
    # rect for spotting difference
    pygame.draw.rect(screen, black, (170,0,200,70), 2)
    pygame.draw.rect(screen, black, (0,171,20,30), 2)
    pygame.draw.rect(screen, black, (140,125,10,26), 2)
    pygame.draw.rect(screen, white, (0, 405, 1200, 10))      # background of text
    screen.blit(textsurface, (50, 400))

    clock.tick(10)
    pygame.display.update()   # game
