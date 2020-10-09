import pygame
class Character(pygame.sprite.Sprite):
    def __init__ (self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.size = [20,20]
        self.image = pygame.Surface (self.size)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def move(self,event):
        if event.type == pygame.KEYDOWN:
                if self.keys == pygame.K_DOWN:
                    self.y -= 3
                if self.keys == pygame.K_UP:
                    self.y += 3
                if self.keys == pygame.K_LEFT:
                    self.x -= 3
                if self.keys == pygame.K_RIGHT:
                    self.x += 3