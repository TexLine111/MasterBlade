import pygame
import character


pygame.init ()
pygame.display.set_caption("MasterBlade")
size = width, height = 800, 600
screen = pygame.display.set_mode (size)
screen_rect = screen.get_rect ()
clock = pygame.time.Clock()
FPS =  75
WHITE = (255, 255, 255)
run = True

#OBJECTS
all_objects = pygame.sprite.Group()
character = character.Character (width/2, height/2)
all_objects.add (character)


#DRAW
def draw():
    screen.fill (WHITE)
    all_objects.draw(screen)


#UPDATE
def update():
    character.move (screen_rect)
    clock.tick(FPS)
    pygame.display.flip ()


while run:
    for event in pygame.event.get ():
        #QUIT
        if event.type == pygame.QUIT: 
            run = False
        #CHANGE DIRECTION
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character.direction[0] = 1
            if event.key == pygame.K_RIGHT:
                character.direction[1] = 1
            if event.key == pygame.K_UP:
                character.direction[2] = 1
            if event.key == pygame.K_DOWN:
                character.direction[3] = 1
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                character.direction[0] = 0
            if event.key == pygame.K_RIGHT:
                character.direction[1] = 0
            if event.key == pygame.K_UP:
                character.direction[2] = 0
            if event.key == pygame.K_DOWN:
                character.direction[3] = 0
    draw()
    update()
