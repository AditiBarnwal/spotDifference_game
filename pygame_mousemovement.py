import pygame

pygame.init()  # pygame initialization

screen = pygame.display.set_mode((600, 480))
clock = pygame.time.Clock()

red = (255, 23, 10)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)

while True:
    screen.fill(white)

    for event in pygame.event.get():
        print(event)

    clock.tick(10)
    pygame.display.update()  # game
