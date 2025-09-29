import pygame
height = 800
width = 800
board_sprite = pygame.transform.scale(pygame.image.load("assets/board.png"), (width, height))

x_sprite = pygame.transform.scale(pygame.image.load("assets/x_sprite.png"), (60, 60))

o_sprite = pygame.transform.scale(pygame.image.load("assets/o_sprite.png"), (60, 60))
