import pygame

pygame.init()  # pygame initialization

screen = pygame.display.set_mode((600, 480))

clock = pygame.time.Clock()

red = (255,23, 10)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
pi = 3.14

x_position_rect = 200
y_position_rect = 140

x_position_circle = 400
y_position_circle = 350

circle_radius = 40
while True:
    screen.fill(white)
    # pygame.draw.line(screen, red, (30, 450), (500, 100))
    pygame.draw.rect(screen, blue, (x_position_rect, y_position_rect, 200, 120))
    pygame.draw.circle(screen, red, (x_position_circle, y_position_circle), circle_radius)
    # pygame.draw.arc(screen, green, (100, 200, 100, 240), pi, pi/2, 4)
    x_position_rect += 5
    y_position_rect += 5

    x_position_circle -= 4
    y_position_circle -= 4

    circle_radius -= 1
    clock.tick(10)
    pygame.display.update()   # game
