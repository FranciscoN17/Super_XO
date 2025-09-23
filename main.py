import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Super XO")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    
    screen.fill((255,255,255))

    pygame.display.flip()

pygame.quit()