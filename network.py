import pickle, threading, socket, pygame, sys, random
import utils, front, assets
from utils import Game

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

def broadcast_msg(clients: list, obj):
    for client in clients:
        send_msg(client, (obj, utils.symbols[clients.index(client)]))

class Server:
    def __init__(self, host="localhost", port=5000, game=Game()):
        self.host = host
        self.port = port
        self.clients = []
        self.game = game

    def handle_client(self, socket, symbol):
        while True:
            if symbol == self.game.player_turn:
                try:
                    msg = recv_msg(socket)
                    if not msg:
                        break
                    (board_key_temp, board_turn_temp) = msg
                    print("recebido:", (board_key_temp, board_turn_temp))

                    if self.game.make_move(board_turn_temp, board_key_temp):
                        broadcast_msg(self.clients, self.game)
                        print("jogada feita:", (board_key_temp, board_turn_temp))
                        
                except:
                    break

    def start(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.host, self.port))
        server.listen(2)

        print("Servidor aguardando jogadores...")

        while len(self.clients) < 2:
            client, addr = server.accept()
            symbol = utils.symbols[len(self.clients)]
            self.clients.append(client)
            threading.Thread(target=self.handle_client, args=(client, symbol), daemon=True).start()
            print(f"Jogador {symbol} conectado:", addr)

        broadcast_msg(self.clients, self.game)

        front.run(self.game)

        server.close()

class Client:
    def __init__(self, game = Game()):
        self.symbol = ""
        self.game = game
        self.sock = None

    def connect(self, server_ip = "localhost", port=5000):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((server_ip, port))
    
    def receive(self):
        while True:
            try:
                msg = recv_msg(self.sock)
                if not msg:
                    break
                self.game, self.symbol = msg
                print("game recebido")
            except:
                break
    
    def start(self):
        threading.Thread(target=self.receive, args=(), daemon=True).start()

        pygame.init()
        screen = pygame.display.set_mode((assets.HEIGHT,assets.WIDTH))

        while True:
            front.show_game(self.game, screen)
            pygame.display.set_caption(f"Super XO - Client {self.symbol}")
            #EVENT HANDLER
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.sock.close()
                    sys.exit()

                if utils.handle_click(event):
                    clicked_pos = utils.handle_click(event)
                    #Verifica em qual célula do tabuleiro o jogador clicou
                    board_key, board_turn  = utils.get_board_key_from_pos_global(self.game, clicked_pos)
                    send_msg(self.sock, (board_key, board_turn))
                    print("enviado:", (board_key, board_turn))

            pygame.display.flip()
    
class AIClient(Client):
    def start(self):

        while True:
            try:
                msg = recv_msg(self.sock)
                if not msg:
                    break
                self.game, self.symbol = msg
                print("game recebido")
            except:
                break
            wait = random.uniform(0.5, 1.5)
            pygame.time.delay(int(wait * 1000))
            if self.symbol == self.game.player_turn:
                board_key, board_turn = self.chose_next_move()
                send_msg(self.sock, (board_key, board_turn))
                print("enviado:", (board_key, board_turn))
    
    def chose_next_move(self):
        possible_moves = []
        if self.game.free_play:
            for board_turn in self.game.info:
                    for board_key in self.game.info[board_turn].positions:
                        if self.game.is_move_valid(board_key, board_turn):
                            possible_moves.append((board_key, board_turn))
        else:
            for board_key in self.game.info[self.game.board_turn].positions:
                if self.game.is_move_valid(board_key, self.game.board_turn):
                    possible_moves.append((board_key, self.game.board_turn))
        chosen_move = random.choice(possible_moves)
        print("AI escolheu:", chosen_move)
        return chosen_move