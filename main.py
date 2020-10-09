import pygame
import character
pygame.init ()
size = width, height = 800, 600
screen = pygame.display.set_mode (size)
run = True
screen_rect = screen.get_rect ()
#OBJECTS
all_objects = pygame.sprite.Group()
character = character.Character (width/2, height/2)
all_objects.add (character)
#UPDATE
def update():
    event = pygame.event.get ()
    character.move (event)
    keys = pygame.key.get_pressed ()
    pygame.display.flip ()

while run:
    for event in pygame.event.get ():
        if event.type == pygame.QUIT: 
            run = False
    screen.fill ((255,255,255))
    update()