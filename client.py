import pygame, socket, pickle, threading, sys

import utils, assets, network
from utils import Game

SERVER_IP = "localhost"
PORT = 5000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((SERVER_IP, PORT))

game = Game()
my_symbol = ""

def receive(socket):
    global game, my_symbol
    buffer = b""
    while True:
        try:
            packet = socket.recv(4096)
            if not packet:
                break
            buffer += packet
            while buffer:
                game, my_symbol = pickle.loads(buffer)
                print("game recebido")
                buffer = b""
        except:
            break

threading.Thread(target=receive, args=(sock,), daemon=True).start()

## GAME CONFIGURATION ##

pygame.init()

screen = pygame.display.set_mode((assets.height,assets.width))

while True:
    utils.show_game(game, screen)
    pygame.display.set_caption(f"Super XO - Client {my_symbol}")
    #EVENT HANDLER
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sock.close()
            sys.exit()
    
    if utils.handle_click(event):
        clicked_pos = utils.handle_click(event)
        #Verifica em qual célula do tabuleiro o jogador clicou
        board_key, board_turn  = utils.get_board_key_from_pos_global(game, clicked_pos)
        network.send_move(sock, board_key, board_turn)

    pygame.display.flip()