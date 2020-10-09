import pygame
pygame.init ()
size = width, height = 800, 600
screen = pygame.display.set_mode (size)
run = True
while run:
    for event in pygame.event.get ():
        if event.type == pygame.QUIT: 
            run = False
        screen.fill ((255,255,255))
        pygame.display.flip()