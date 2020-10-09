import pygame


class Character(pygame.sprite.Sprite):
    def __init__ (self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.color = (0, 0, 0)
        self.speed = [2, 2]
        self.direction = [0, 0, 0 ,0] # left right up down
        self.size = [30, 30]
        self.image = pygame.Surface (self.size)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def move(self, screen_rect):
        self.collide(screen_rect)
        self.rect.x += self.speed[0] * (self.direction[1] - self.direction[0])
        self.rect.y += self.speed[1] * (self.direction[3] - self.direction[2])

    def collide(self, screen_rect):
        if self.rect.left <= screen_rect.left:
            self.rect.left = screen_rect.left

        if self.rect.right >= screen_rect.right:
            self.rect.right = screen_rect.right

        if self.rect.top <= screen_rect.top:
            self.rect.top = screen_rect.top
        
        if self.rect.bottom >= screen_rect.bottom:
            self.rect.bottom = screen_rect.bottom
        

