import pygame
import utils, front, assets
import menu
from utils import Game

# pygame.init()
screen = pygame.display.set_mode((assets.height,assets.width))
pygame.display.set_caption("Super XO")

game = Game()

running = True

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
        front.show_game(game, screen)

        #Event handler
        for event in pygame.event.get():
            #Fecha a janela se o jogador clicar em fechar
            if event.type == pygame.QUIT:
                running = False

            #Verifica se o jogador clicou em algum lugar
            if utils.handle_click(event):
                clicked_pos = utils.handle_click(event)
                #Verifica em qual célula do tabuleiro o jogador clicou
                board_key, board_turn = utils.get_board_key_from_pos_global(game, clicked_pos)
                game.make_move(board_turn, board_key)

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