import pygame, socket, pickle, threading, sys

import utils, assets
from utils import Board, Game


SERVER_IP = "localhost"
PORT = 5000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((SERVER_IP, PORT))

game = Game({(0,0): Board(assets.board_tables[0][0]), (0,1): Board(assets.board_tables[0][1]), (0,2): Board(assets.board_tables[0][2]), 
             (1,0): Board(assets.board_tables[1][0]), (1,1): Board(assets.board_tables[1][1]), (1,2): Board(assets.board_tables[1][2]), 
             (2,0): Board(assets.board_tables[2][0]), (2,1): Board(assets.board_tables[2][1]), (2,2): Board(assets.board_tables[2][2])
             })

def receive(socket):
    global game
    buffer = b""
    while True:
        try:
            packet = socket.recv(4096)
            if not packet:
                break
            buffer += packet
            while buffer:
                game = pickle.loads(buffer)
                print("game recebido")
                buffer = b""
        except:
            break

threading.Thread(target=receive, args=(sock,), daemon=True).start()

## GAME CONFIGURATION ##

pygame.init()

screen = pygame.display.set_mode((assets.height,assets.width))
pygame.display.set_caption("Super XO - Client")

while True:
    utils.show_game(game, screen)
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
        data = pickle.dumps((board_key, board_turn))
        sock.sendall(data)

    pygame.display.flip()