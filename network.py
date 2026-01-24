import pickle
import utils
from utils import Game

def send_game_state(game: Game, client_list, symbols = utils.symbols):
    for i in range(len(client_list)):
        data = pickle.dumps((game, symbols[i]))
        client_list[i].sendall(data)

def send_move(socket, board_key, board_turn):
    data = pickle.dumps((board_key, board_turn))
    socket.sendall(data)