import pygame
import utils
import assets
import menu
from utils import Board, Game

# pygame.init()
screen = pygame.display.set_mode((assets.height,assets.width))
pygame.display.set_caption("Super XO")

game = Game({(0,0): Board(assets.board_tables[0][0]), (0,1): Board(assets.board_tables[0][1]), (0,2): Board(assets.board_tables[0][2]), 
             (1,0): Board(assets.board_tables[1][0]), (1,1): Board(assets.board_tables[1][1]), (1,2): Board(assets.board_tables[1][2]), 
             (2,0): Board(assets.board_tables[2][0]), (2,1): Board(assets.board_tables[2][1]), (2,2): Board(assets.board_tables[2][2])
             })

running = True

player_turn = "X"
board_turn = (1,1)
free_play = True
board_key = None

# Menu: Possible game states
MENU_STATE = 0
GAME_STATE = 1
GAME_OVER_DRAW_STATE = 2 
GAME_OVER_X_STATE = 3
GAME_OVER_O_STATE = 4

# Set the initial state
current_state = MENU_STATE

#Game loop
while running:
    # Get all events first
    events = pygame.event.get()

    # Event handler for quitting the game
    for event in events:
        if event.type == pygame.QUIT:
            running = False
            
    if current_state == MENU_STATE:
        current_state = menu.draw_menu(screen, events, current_state, GAME_STATE)
    
    if current_state in (GAME_OVER_DRAW_STATE, GAME_OVER_X_STATE, GAME_OVER_O_STATE):
        current_state = menu.draw_game_over(screen, events, current_state, MENU_STATE)
    

    elif current_state == GAME_STATE:

        #Mostra a UI do jogo
        utils.show_game(game, screen, free_play, board_turn)

        #Event handler
        for event in pygame.event.get():
            #Fecha a janela se o jogador clicar em fechar
            if event.type == pygame.QUIT:
                running = False

            #Verifica se o jogador clicou em algum lugar
            if utils.handle_click(event):
                clicked_pos = utils.handle_click(event)
                #Caso a jogada atual não seja livre
                if not free_play:
                    #Verifica em qual célula do tabuleiro o jogador clicou
                    board_key = utils.get_board_key_from_pos(clicked_pos, game.info[board_turn].positions)

                    #Faz a jogada se a célula estiver vazia
                    if board_key and not game.info[board_turn].info[board_key]:
                        game, player_turn, board_turn, free_play = utils.make_move(game, board_turn, board_key, player_turn)

                #Caso a jogada atual seja livre
                else:
                    #Verifica em qual célula do tabuleiro o jogador clicou
                    board_key, board_turn = utils.get_board_key_from_pos_global(game, clicked_pos)

                    #Faz a jogada se a célula estiver vazia e disponível
                    if board_key and not game.info[board_turn].info[board_key] and not game.info[board_turn].winner:
                        game, player_turn, board_turn, free_play = utils.make_move(game, board_turn, board_key, player_turn)

        #Finaliza o jogo se houver um vencedor
        if game.winner:
            print(f"The winner is: {game.winner}")
            # running = False
            current_state = GAME_OVER_X_STATE if game.winner == "X" else GAME_OVER_O_STATE

            
        #Finaliza o jogo se houver empate
        if game.draw:
            print("It's a draw!")
            # running = False
            current_state = GAME_OVER_DRAW_STATE

        pygame.display.flip()

        
pygame.quit()