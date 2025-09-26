import pygame
import utils
from utils import Game
from utils import Board

pygame.init()
height = 800
width = 800
screen = pygame.display.set_mode((height,width))
pygame.display.set_caption("Super XO")

board00 = Board(utils.board_tables[0][0])
board10 = Board(utils.board_tables[1][0])
board20 = Board(utils.board_tables[2][0])
board01 = Board(utils.board_tables[0][1])
board11 = Board(utils.board_tables[1][1])
board21 = Board(utils.board_tables[2][1])
board02 = Board(utils.board_tables[0][2])
board12 = Board(utils.board_tables[1][2])
board22 = Board(utils.board_tables[2][2])

game = Game({(0,0): board00, (0,1): board01, (0,2): board02, 
             (1,0): board10, (1,1): board11, (1,2): board12, 
             (2,0): board20, (2,1): board21, (2,2): board22
             })


board_sprite = pygame.image.load("assets/board.png")
board_sprite = pygame.transform.scale(board_sprite, (width, height))

x_sprite = pygame.image.load("assets/x_sprite.png")
x_sprite = pygame.transform.scale(x_sprite, (60, 60))
o_sprite = pygame.image.load("assets/o_sprite.png")
o_sprite = pygame.transform.scale(o_sprite, (60, 60))

running = True

player_turn = "X"
board_turn = (1,1)
clicked_pos = None
free_play = False
board_key = None

while running:
    screen.blit(board_sprite, (0,0))
    
    if free_play:
        pygame.draw.rect(screen, (0,255,0), (2, 2, width-4, height-4), 3)
    else:
        pygame.draw.rect(screen, (0,255,0), (board_turn[1]*264+3, board_turn[0]*264+3, 265, 265), 3)

    #Desenha X e O na tela de acordo com o que tem salvo nos tabuleiros
    for board_key in game.info:
        for cell_key in game.info[board_key].positions:
            draw_pos = game.info[board_key].positions[cell_key]
            if game.info[board_key].info[cell_key] == "X":
                screen.blit(x_sprite, draw_pos)
            elif game.info[board_key].info[cell_key] == "O":
                screen.blit(o_sprite, draw_pos)

    #Game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if utils.handle_click(event):
            clicked_pos = utils.handle_click(event)
            print("O jogador clicou \n")
            #if not free_play:
            board_key = utils.get_board_key_from_pos(clicked_pos, game.info[board_turn].positions)
            print("Ele clicou na célula ", board_key, "\n")

            if board_key and not game.info[board_turn].info[board_key]:
                print("A célula está pronta para receber um valor \n")
                game.info[board_turn].info[board_key] = player_turn
                print("A célula ",board_key, "do tabuleiro", board_turn,"recebeu o valor ", player_turn)
                player_turn = "O" if player_turn == "X" else "X"
                board_turn = board_key if board_key else board_turn

            #else:
            #    for i in range(len(utils.board_tables[0])):
            #        for j in range(len(utils.board_tables)):
            #            table = utils.board_tables[i][j]
            #            key = utils.get_board_key_from_pos(clicked_pos, table)
            #            if key:
            #                board_key = key
            #                board_turn = (i, j)
            #                break
            #    if not game.info[(board_turn[0],board_turn[1])].info[board_key]:
            #        if not game.info[board_turn].winner:
            #            game.info[(board_turn[0],board_turn[1])].info[board_key] = player_turn
            #            player_turn = "O" if player_turn == "X" else "X"
            #            free_play = False

    #if game.winner:
    #    print(f"The winner is: {game.winner}")
    #    running = False

    pygame.display.flip()

        
pygame.quit()