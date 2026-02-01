import pygame, sys
import assets
from utils import Game

#Desenha o retângulo verde em volta do tabuleiro que pode ser jogado
def draw_green_rectangle(game: Game, screen):
    if game.free_play:
        pygame.draw.rect(screen, (0,255,0), (2, 2, assets.WIDTH-4, assets.HEIGHT-4), 3)
    else:
        pygame.draw.rect(screen, (0,255,0), ((game.board_turn[1]*264+3)*assets.HEIGHT/800, (game.board_turn[0]*264+3)*assets.HEIGHT/800, 265*assets.HEIGHT/800, 265*assets.HEIGHT/800), 3)

#Desenha X e O na tela de acordo com o que tem salvo nos tabuleiros
def show_game(game: Game, screen):
    screen.blit(assets.board_sprite, (0,0))
    draw_green_rectangle(game, screen)

    for board_key in game.info:
        for cell_key in game.info[board_key].positions:
            if not game.info[board_key].winner:
                draw_pos = game.info[board_key].positions[cell_key]
                if game.info[board_key].info[cell_key] == "X":
                    screen.blit(assets.x_sprite, draw_pos)
                elif game.info[board_key].info[cell_key] == "O":
                    screen.blit(assets.o_sprite, draw_pos)
            else:
                center_pos = ((board_key[1]*264+3)*assets.HEIGHT/800, (board_key[0]*264+3)*assets.HEIGHT/800)
                if game.info[board_key].winner == "X":
                    screen.blit(pygame.transform.scale(assets.x_sprite, (264/800 * assets.HEIGHT, 264/800 * assets.HEIGHT)), center_pos)
                elif game.info[board_key].winner == "O":
                    screen.blit(pygame.transform.scale(assets.o_sprite, (264/800 * assets.HEIGHT, 264/800 * assets.HEIGHT)), center_pos)

def run(game: Game):
    pygame.init()

    screen = pygame.display.set_mode((assets.HEIGHT,assets.WIDTH))
    pygame.display.set_caption("Super XO")

    while True:
        show_game(game, screen)
        #EVENT HANDLER
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.flip()