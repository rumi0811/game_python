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

gravity = 0

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()        
        self.image = pygame.Surface((20, 20))  
        self.image.fill(BLUE)      
        self.rect = self.image.get_rect()        
        self.rect.x = 50
        self.rect.y = HEIGHT // 2
        
class Pipa(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.Surface((20, 500))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = 400 + 10
        
    def update(self):
        self.rect.x -= 4
        if self.rect.x <= -20:
            self.rect.x = WIDTH +10
        
    
class Top(Pipa):
    def __init__(self, y):
        super().__init__()   
        self.rect.y = y     
        
class Bottom(Pipa):
    def __init__(self, y):
        super().__init__()   
        self.rect.y = y
        
all_sprites = pygame.sprite.Group()
pipas = pygame.sprite.Group()
bird = Bird()


for i in range(2):
    p1 = Top(-300)
    p2 = Bottom(350)
    pipas.add(p1)
    pipas.add(p2)
    all_sprites.add(p1)
    all_sprites.add(p2)
    
all_sprites.add(bird)


#Game looping
run = True
while run:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
            
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                gravity = 0
                gravity -=5
            
    gravity += 0.25
    bird.rect.y += gravity
     
     
    all_sprites.update()
    screen.fill(BLACK)       
    all_sprites.draw(screen)
    
    pygame.display.flip()
    
pygame.quit()

