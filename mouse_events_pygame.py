import pygame

pygame.init()  # pygame initialization

screen = pygame.display.set_mode((600, 480))
clock = pygame.time.Clock()

red = (255,23, 10)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)

x_position_circle = int(600/2)
y_position_circle = int(380/2)
while True:
    screen.fill(white)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:  # this will stop printing mouse movement coordinate in console
            if event.key == pygame.K_a:   # specially for printing particular key in console
                x_position_circle += 6    # everytime u press letter 'a' circle will move to x-axis
            elif event.key == pygame.K_z:
                x_position_circle = x_position_circle - 4
            elif event.key == pygame.K_k:
                y_position_circle = y_position_circle + 4
            elif event.key == pygame.K_j:
                y_position_circle = y_position_circle - 4
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                print("left button")
                # mouse_position = pygame.mouse.get_pos()
                # print(mouse_position)
                # x_position_circle = mouse_position[0]
                # y_position_circle = mouse_position[1]
    mouse_position = pygame.mouse.get_pos()
    x_position_circle = mouse_position[0]
    y_position_circle = mouse_position[1]
    pygame.draw.circle(screen, red, (x_position_circle, y_position_circle), 40)

    clock.tick(10)
    pygame.display.update()   # game
