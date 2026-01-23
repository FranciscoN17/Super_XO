import socket, sys, threading
import pickle
import pygame

import utils
import assets
from utils import Board, Game

HOST = "localhost"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(2)

clients = []
symbols = ["X", "O"]

print("Servidor aguardando jogadores...")

game = Game({(0,0): Board(assets.board_tables[0][0]), (0,1): Board(assets.board_tables[0][1]), (0,2): Board(assets.board_tables[0][2]), 
             (1,0): Board(assets.board_tables[1][0]), (1,1): Board(assets.board_tables[1][1]), (1,2): Board(assets.board_tables[1][2]), 
             (2,0): Board(assets.board_tables[2][0]), (2,1): Board(assets.board_tables[2][1]), (2,2): Board(assets.board_tables[2][2])
             })

def receive(socket, symbol):
    global game
    buffer = b""
    while True:
        if symbol == game.player_turn:
            try:
                packet = socket.recv(4096)
                if not packet:
                    break
                buffer += packet
                while buffer:
                    (board_key_temp, board_turn_temp) = pickle.loads(buffer)

                    if board_key_temp and board_turn_temp:
                        if (board_turn_temp == game.board_turn or game.free_play):
                            if not game.info[board_turn_temp].info[board_key_temp] and not game.info[board_turn_temp].winner:
                                game = utils.make_move(game, board_turn_temp, board_key_temp)
                                data = pickle.dumps(game)
                                for client in clients:
                                    client.sendall(data)
                    buffer = b""

            except:
                break

while len(clients) < 2:
    client, addr = server.accept()
    symbol = symbols[len(clients)]
    clients.append(client)
    threading.Thread(target=receive, args=(client, symbol), daemon=True).start()
    print(f"Jogador {symbol} conectado:", addr)

## GAME CONFIGURATION ##

pygame.init()

screen = pygame.display.set_mode((assets.height,assets.width))
pygame.display.set_caption("Super XO - Server")


while True:
    utils.show_game(game, screen)
    #EVENT HANDLER
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            server.close()
            sys.exit()

    pygame.display.flip()

        