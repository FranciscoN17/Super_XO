import pygame
import assets

board_tables = [
    [
        {
            (0,0): (40, 40), (0,1): (106, 40), (0,2): (172, 40),
            (1,0): (40, 106), (1,1): (106, 106), (1,2): (172, 106),
            (2,0): (40, 172), (2,1): (106, 172), (2,2): (172, 172),
        },
        {
            (0,0): (303, 40), (0,1): (369, 40), (0,2): (435, 40),
            (1,0): (303, 106), (1,1): (369, 106), (1,2): (435, 106),
            (2,0): (303, 172), (2,1): (369, 172), (2,2): (435, 172),
        },
        {
            (0,0): (566, 40), (0,1): (632, 40), (0,2): (698, 40),
            (1,0): (566, 106), (1,1): (632, 106), (1,2): (698, 106),
            (2,0): (566, 172), (2,1): (632, 172), (2,2): (698, 172),
        },
    ],
    [
        {
            (0,0): (40, 303), (0,1): (106, 303), (0,2): (172, 303),
            (1,0): (40, 369), (1,1): (106, 369), (1,2): (172, 369),
            (2,0): (40, 435), (2,1): (106, 435), (2,2): (172, 435),
        },
        {
            (0,0): (303, 303), (0,1): (369, 303), (0,2): (435, 303),
            (1,0): (303, 369), (1,1): (369, 369), (1,2): (435, 369),
            (2,0): (303, 435), (2,1): (369, 435), (2,2): (435, 435),
        },
        {
            (0,0): (566, 303), (0,1): (632, 303), (0,2): (698, 303),
            (1,0): (566, 369), (1,1): (632, 369), (1,2): (698, 369),
            (2,0): (566, 435), (2,1): (632, 435), (2,2): (698, 435),
        },
    ],
    [
        {
            (0,0): (40, 566), (0,1): (106, 566), (0,2): (172, 566),
            (1,0): (40, 632), (1,1): (106, 632), (1,2): (172, 632),
            (2,0): (40, 698), (2,1): (106, 698), (2,2): (172, 698),
        },
        {
            (0,0): (303, 566), (0,1): (369, 566), (0,2): (435, 566),
            (1,0): (303, 632), (1,1): (369, 632), (1,2): (435, 632),
            (2,0): (303, 698), (2,1): (369, 698), (2,2): (435, 698),
        },
        {
            (0,0): (566, 566), (0,1): (632, 566), (0,2): (698, 566),
            (1,0): (566, 632), (1,1): (632, 632), (1,2): (698, 632),
            (2,0): (566, 698), (2,1): (632, 698), (2,2): (698, 698),
        },
    ],
]

def make_move(game, board_turn, board_key, player_turn):
    game.info[board_turn].info[board_key] = player_turn
    player_turn = "O" if player_turn == "X" else "X"
    board_turn = board_key if board_key else board_turn
    return game, player_turn, board_turn, is_next_move_free(game, board_turn)

def is_next_move_free(game, board_turn):
    if game.info[board_turn].winner:
        return True
    return False

def get_board_key_from_pos(pos, board_table):
    if pos:
        x, y = pos
        for key, value in board_table.items():
            vx, vy = value
            if vx <= x < vx + 60 and vy <= y < vy + 60:
                return key
    return None

def get_board_key_from_pos_global(game, clicked_pos):
    for table_key in game.info:
        table = game.info[table_key].positions
        key = get_board_key_from_pos(clicked_pos, table)
        if key and table_key:
            return key, table_key
    return None, None

def handle_click(event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            return mouse_pos
        return None

def check_winner(board_info):
    # Check rows
    for row in range(3):
        if board_info[(row, 0)] == board_info[(row, 1)] == board_info[(row, 2)] != None:
            return board_info[(row, 0)]
    # Check columns
    for col in range(3):
        if board_info[(0, col)] == board_info[(1, col)] == board_info[(2, col)] != None:
            return board_info[(0, col)]
    # Check diagonals
    if board_info[(0, 0)] == board_info[(1, 1)] == board_info[(2, 2)] != None:
        return board_info[(0, 0)]
    if board_info[(0, 2)] == board_info[(1, 1)] == board_info[(2, 0)] != None:
        return board_info[(0, 2)]
    return None

#Desenha o retângulo verde em volta do tabuleiro que pode ser jogado
def draw_green_rectangle(screen, free_play, board_turn):
    if free_play:
        pygame.draw.rect(screen, (0,255,0), (2, 2, assets.width-4, assets.height-4), 3)
    else:
        pygame.draw.rect(screen, (0,255,0), (board_turn[1]*264+3, board_turn[0]*264+3, 265, 265), 3)

#Desenha X e O na tela de acordo com o que tem salvo nos tabuleiros
def show_game(game, screen, free_play, board_turn):
    screen.blit(assets.board_sprite, (0,0))
    draw_green_rectangle(screen, free_play, board_turn)

    for board_key in game.info:
        for cell_key in game.info[board_key].positions:
            if not game.info[board_key].winner:
                draw_pos = game.info[board_key].positions[cell_key]
                if game.info[board_key].info[cell_key] == "X":
                    screen.blit(assets.x_sprite, draw_pos)
                elif game.info[board_key].info[cell_key] == "O":
                    screen.blit(assets.o_sprite, draw_pos)
            else:
                center_pos = (board_key[1]*264+3, board_key[0]*264+3)
                if game.info[board_key].winner == "X":
                    screen.blit(pygame.transform.scale(assets.x_sprite, (264, 264)), center_pos)
                elif game.info[board_key].winner == "O":
                    screen.blit(pygame.transform.scale(assets.o_sprite, (264, 264)), center_pos)

def check_global_winner(info):
    # Create a summary board to check for global winner
    summary_board = {}
    for i in range(3):
        for j in range(3):
            local_winner = check_winner(info[(i,j)].info)
            summary_board[(i, j)] = local_winner

    return check_winner(summary_board)

class Board:
    def __init__(self, positions, info=None):
        self.positions = positions
        self.info = info if info is not None else {
            (0,0): None, (0,1): None, (0,2): None,
            (1,0): None, (1,1): None, (1,2): None,
            (2,0): None, (2,1): None, (2,2): None,
        }
        self._winner = None

    @property
    def winner(self):
        self._winner = check_winner(self.info)
        return self._winner


class Game:
    def __init__(self, info=None):
        self.info = info if info is not None else {
            (0,0): None, (0,1): None, (0,2): None, 
            (1,0): None, (1,1): None, (1,2): None, 
            (2,0): None, (2,1): None, (2,2): None
        }
        self._winner = None

    @property
    def winner(self):
        self._winner = check_global_winner(self.info)
        return self._winner


