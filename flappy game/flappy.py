import pygame
from pygame.locals import *

WIDTH = 480
HEIGHT = 600

FPS = 30

#variabel warna
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Flappy bird clone')
clock = pygame.time.Clock()

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.image = pygame.Surface((20, 20))  
        self.image.fill(BLUE)      
        self.rect = self.image.get_rect()        
        self.rect.x = 50
        self.rect.y = HEIGHT // 2
        
        
all_sprites = pygame.sprite.Group()
bird = Bird()

all_sprites.add(bird)


#Game looping
run = True
while run:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
     
     
    all_sprites.update()       
    all_sprites.draw(screen)
    
    pygame.display.flip()
    
pygame.quit()

