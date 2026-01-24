import pygame, socket, pickle, threading, sys

import utils, assets, network
from utils import Game

HOST = "localhost"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(2)

clients = []

print("Servidor aguardando jogadores...")

game = Game()

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

                    if utils.is_move_valid(game, board_key_temp, board_turn_temp):
                        game = utils.make_move(game, board_turn_temp, board_key_temp)
                        network.send_game_state(game, clients)
                    buffer = b""

            except:
                break

while len(clients) < 2:
    client, addr = server.accept()
    symbol = utils.symbols[len(clients)]
    clients.append(client)
    threading.Thread(target=receive, args=(client, symbol), daemon=True).start()
    print(f"Jogador {symbol} conectado:", addr)

network.send_game_state(game, clients)
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

        