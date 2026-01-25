import pygame, socket, pickle, threading, sys

import utils, assets, network
from utils import Game

HOST = "192.168.0.154"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(2)

clients = []

print("Servidor aguardando jogadores...")

game = Game()

def receive(socket, symbol):
    global game
    while True:
        if symbol == game.player_turn:
            try:
                msg = network.recv_msg(socket)
                if not msg:
                    break
                (board_key_temp, board_turn_temp) = msg

                if utils.is_move_valid(game, board_key_temp, board_turn_temp):
                    game = utils.make_move(game, board_turn_temp, board_key_temp)
                    for client in clients:
                        print("jogo enviado para cliente")
                        network.send_msg(client, (game, symbol))

            except:
                break

while len(clients) < 2:
    client, addr = server.accept()
    symbol = utils.symbols[len(clients)]
    clients.append(client)
    threading.Thread(target=receive, args=(client, symbol), daemon=True).start()
    print(f"Jogador {symbol} conectado:", addr)

for client in clients:
    network.send_msg(client, (game, utils.symbols[clients.index(client)]))
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

        