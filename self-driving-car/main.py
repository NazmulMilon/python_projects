
import pygame
pygame.init()
window = pygame.display.set_mode((1200, 400))
track = pygame.image.load('track1.png')

car = pygame.image.load('tesla.png')
car = pygame.transform.scale(car, (30, 60))
car_x = 155
car_y = 300
drive = True
clock = pygame.time.Clock()
while drive:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drive = False

    car_y = car_y - 2

    window.blit(track, (0,0))
    window.blit(car, (car_x, car_y))
    pygame.display.update()
