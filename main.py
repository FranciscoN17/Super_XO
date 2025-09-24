import pygame
import utils

pygame.init()
height = 800
width = 800
screen = pygame.display.set_mode((height,width))
pygame.display.set_caption("Super XO")


board_table = utils.board_tables[1][1]
board_infos = utils.board_infos
win_infos = utils.win_infos

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
free_play = True
board_key = None

while running:
    screen.blit(board_sprite, (0,0))
    
    if free_play:
        pygame.draw.rect(screen, (0,255,0), (2, 2, width-4, height-4), 3)
    else:
        pygame.draw.rect(screen, (0,255,0), (board_turn[1]*264+3, board_turn[0]*264+3, 265, 265), 3)

    for board in board_infos:
        for b in board:
            for key in b:
                draw_pos = utils.board_tables[board_infos.index(board)][board.index(b)][key]
                if b[key] == "X":
                    screen.blit(x_sprite, draw_pos)
                elif b[key] == "O":
                    screen.blit(o_sprite, draw_pos)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if utils.handle_click(event):
            clicked_pos = utils.handle_click(event)
            if not free_play:
                board_key = utils.get_board_key_from_pos(clicked_pos, board_table)
                if board_key and not board_infos[board_turn[0]][board_turn[1]][board_key]:
                    board_infos[board_turn[0]][board_turn[1]][board_key] = player_turn
                    player_turn = "O" if player_turn == "X" else "X"
            else:
                for i in range(len(utils.board_tables[0])):
                    for j in range(len(utils.board_tables)):
                        table = utils.board_tables[i][j]
                        key = utils.get_board_key_from_pos(clicked_pos, table)
                        if key:
                            board_key = key
                            board_turn = (i, j)
                            board_table = table
                            break
                if not board_infos[board_turn[0]][board_turn[1]][board_key]:
                    if not win_infos[(board_turn[0],board_turn[1])]:
                        board_infos[board_turn[0]][board_turn[1]][board_key] = player_turn
                        player_turn = "O" if player_turn == "X" else "X"
                        free_play = False
        
        board_turn = board_key if board_key else board_turn
    board_table = utils.board_tables[board_turn[0]][board_turn[1]]

    winner = utils.check_winner(win_infos)

    if winner:
        print(f"The winner is: {winner}")
        running = False

    pygame.display.flip()

    if utils.check_winner(board_infos[board_turn[0]][board_turn[1]]):
        win_infos[(board_turn[0],board_turn[1])] = utils.check_winner(board_infos[board_turn[0]][board_turn[1]])
        free_play = True
        
pygame.quit()