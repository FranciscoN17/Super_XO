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


def send_msg(sock, obj):
    payload = pickle.dumps(obj)
    size = len(payload).to_bytes(4, byteorder="big")
    sock.sendall(size + payload)

def recv_msg(sock):
    # 1) lê o tamanho
    size_data = sock.recv(4)
    if not size_data:
        return None

    size = int.from_bytes(size_data, byteorder="big")

    # 2) lê exatamente `size` bytes
    data = b""
    while len(data) < size:
        packet = sock.recv(size - len(data))
        if not packet:
            return None
        data += packet

    return pickle.loads(data)