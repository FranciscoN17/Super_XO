import pygame
import utils
from utils import Board, Game

pygame.init()
height = 800
width = 800
screen = pygame.display.set_mode((height,width))
pygame.display.set_caption("Super XO")

game = Game({(0,0): Board(utils.board_tables[0][0]), (0,1): Board(utils.board_tables[0][1]), (0,2): Board(utils.board_tables[0][2]), 
             (1,0): Board(utils.board_tables[1][0]), (1,1): Board(utils.board_tables[1][1]), (1,2): Board(utils.board_tables[1][2]), 
             (2,0): Board(utils.board_tables[2][0]), (2,1): Board(utils.board_tables[2][1]), (2,2): Board(utils.board_tables[2][2])
             })

board_sprite = pygame.transform.scale(pygame.image.load("assets/board.png"), (width, height))

x_sprite = pygame.transform.scale(pygame.image.load("assets/x_sprite.png"), (60, 60))

o_sprite = pygame.transform.scale(pygame.image.load("assets/o_sprite.png"), (60, 60))

running = True

player_turn = "X"
board_turn = (1,1)
free_play = True
board_key = None

#Game loop
while running:
    #Desenha o tabuleiro de fundo
    screen.blit(board_sprite, (0,0))
    
    #Desenha o retângulo verde em volta do tabuleiro que pode ser jogado
    if free_play:
        pygame.draw.rect(screen, (0,255,0), (2, 2, width-4, height-4), 3)
    else:
        pygame.draw.rect(screen, (0,255,0), (board_turn[1]*264+3, board_turn[0]*264+3, 265, 265), 3)

    #Desenha X e O na tela de acordo com o que tem salvo nos tabuleiros
    for board_key in game.info:
        for cell_key in game.info[board_key].positions:
            if not game.info[board_key].winner:
                draw_pos = game.info[board_key].positions[cell_key]
                if game.info[board_key].info[cell_key] == "X":
                    screen.blit(x_sprite, draw_pos)
                elif game.info[board_key].info[cell_key] == "O":
                    screen.blit(o_sprite, draw_pos)
            else:
                center_pos = (board_key[1]*264+3, board_key[0]*264+3)
                if game.info[board_key].winner == "X":
                    screen.blit(pygame.transform.scale(x_sprite, (264, 264)), center_pos)
                elif game.info[board_key].winner == "O":
                    screen.blit(pygame.transform.scale(o_sprite, (264, 264)), center_pos)

    #Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if utils.handle_click(event):
            clicked_pos = utils.handle_click(event)
            if not free_play:
                board_key = utils.get_board_key_from_pos(clicked_pos, game.info[board_turn].positions)

                if board_key and not game.info[board_turn].info[board_key]:
                    game.info[board_turn].info[board_key] = player_turn
                    player_turn = "O" if player_turn == "X" else "X"
                    board_turn = board_key if board_key else board_turn
                    #Determina se o próximo lance é livre ou não
                    if game.info[board_turn].winner:
                        free_play = True
                    else:
                        free_play = False

            else:
                for table_key in game.info:
                    table = game.info[table_key].positions
                    key = utils.get_board_key_from_pos(clicked_pos, table)
                    if key:
                        board_key = key
                        board_turn = table_key
                        break
                if not game.info[board_turn].info[board_key]:
                    if not game.info[board_turn].winner:
                        game.info[board_turn].info[board_key] = player_turn
                        player_turn = "O" if player_turn == "X" else "X"
                        board_turn = board_key if board_key else board_turn
                        #Determina se o próximo lance é livre ou não
                        if game.info[board_turn].winner:
                            free_play = True
                        else:
                            free_play = False

    #Finaliza o jogo se houver um vencedor
    if game.winner:
        print(f"The winner is: {game.winner}")
        running = False

    pygame.display.flip()

        
pygame.quit()