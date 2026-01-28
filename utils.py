import pygame
import assets

class Board:
    def __init__(self, positions, info=None):
        self.positions = positions
        self.info = info if info is not None else {
            (0,0): None, (0,1): None, (0,2): None,
            (1,0): None, (1,1): None, (1,2): None,
            (2,0): None, (2,1): None, (2,2): None,
        }
        self._winner = None

    def check_winner(self):
        # Check rows
        for row in range(3):
            if self.info[(row, 0)] == self.info[(row, 1)] == self.info[(row, 2)] != None:
                return self.info[(row, 0)]
        # Check columns
        for col in range(3):
            if self.info[(0, col)] == self.info[(1, col)] == self.info[(2, col)] != None:
                return self.info[(0, col)]
        # Check diagonals
        if self.info[(0, 0)] == self.info[(1, 1)] == self.info[(2, 2)] != None:
            return self.info[(0, 0)]
        if self.info[(0, 2)] == self.info[(1, 1)] == self.info[(2, 0)] != None:
            return self.info[(0, 2)]
        return None

    @property
    def winner(self):
        if self._winner == None:
            self._winner = self.check_winner()
        return self._winner
    
    @property
    def draw(self):
        # Check if all cells are filled
        for value in self.info.values():
            if value is None:
                return False
        
        # If there's a winner, it's not a draw
        if self.winner:
            return False
        
        return True

boards = {(i, j): Board(assets.board_tables[i][j]) for i in range(3) for j in range(3)}

class Game:
    def __init__(self, info=boards):
        self.info = info if info is not None else {
            (0,0): None, (0,1): None, (0,2): None, 
            (1,0): None, (1,1): None, (1,2): None, 
            (2,0): None, (2,1): None, (2,2): None
        }
        self._winner = None
        self.board_turn = None
        self.free_play = True
        self.player_turn = "X"
    
    def reset(self):
        for board in self.info.values():
            board.info = {
                (0,0): None, (0,1): None, (0,2): None,
                (1,0): None, (1,1): None, (1,2): None,
                (2,0): None, (2,1): None, (2,2): None,
            }
            board._winner = None
        self._winner = None
        self.board_turn = None
        self.free_play = True
        self.player_turn = "X"

    def is_move_valid(self, board_key, board_turn):
        if board_key and board_turn:
            if board_turn == self.board_turn or self.free_play:
                if not self.info[board_turn].info[board_key] and not self.info[board_turn].winner and not self.info[board_turn].draw:
                    return True
            return False
        return False

    def is_next_move_free(self, board_turn):
        if self.info[board_turn].winner or self.info[board_turn].draw:
            return True
        return False

    def make_move(self, board_turn, board_key):
        if self.is_move_valid(board_key, board_turn):
            self.info[board_turn].info[board_key] = self.player_turn
            self.player_turn = "O" if self.player_turn == "X" else "X"
            self.board_turn = board_key if board_key else board_turn
            self.free_play = self.is_next_move_free(self.board_turn)
            return True
        return False

    def check_winner(self, info):
        # Check rows
        for row in range(3):
            if info[(row, 0)] == info[(row, 1)] == info[(row, 2)] != None:
                return info[(row, 0)]
        # Check columns
        for col in range(3):
            if info[(0, col)] == info[(1, col)] == info[(2, col)] != None:
                return info[(0, col)]
        # Check diagonals
        if info[(0, 0)] == info[(1, 1)] == info[(2, 2)] != None:
            return info[(0, 0)]
        if info[(0, 2)] == info[(1, 1)] == info[(2, 0)] != None:
            return info[(0, 2)]
        return None

    @property
    def winner(self):
        self._winner = self.check_winner({k: v.winner for k, v in self.info.items()})
        return self._winner
    
    @property
    def draw(self):

        # Check if all boards are won or drawn
        for board in self.info.values():
            if not board.winner and not board.draw:
                return False
        
        # If there's a winner, it's not a draw
        if self.winner:
            return False
        
        return True

symbols = ["X", "O"]

def get_board_key_from_pos(pos, board_table):
    if pos:
        x, y = pos
        for key, value in board_table.items():
            vx, vy = value
            if vx <= x < vx + 60 and vy <= y < vy + 60:
                return key
    return None

def get_board_key_from_pos_global(game: Game, clicked_pos):
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