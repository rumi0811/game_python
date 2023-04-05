import pygame

pygame.init()

height = 600
width = 600

screen = pygame.display.set_mode([height, width])


screen.fill((255, 0, 0))


pygame.draw.line(screen, (0,0,255),(100,100),(300,300),75)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
            
pygame.quit()