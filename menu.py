import pygame
import assets

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
BRIGHT_GREEN = (0, 255, 0)


try:
    TITLE_FONT = pygame.font.Font(None, 74)
    BUTTON_FONT = pygame.font.Font(None, 50)
except:
    print("Warning: Could not load default font. Menu text might not render.")
    TITLE_FONT = None
    BUTTON_FONT = None


def draw_menu(screen, events, current_state, GAME_STATE):
    """Draws the main menu and handles menu events."""

    screen.fill(BLACK)

    # 1. Draw Title
    if TITLE_FONT:
        title_text = TITLE_FONT.render("Ultimate Tic-Tac-Toe", True, WHITE)
        title_rect = title_text.get_rect(center=(assets.width // 2, assets.height // 4))
        screen.blit(title_text, title_rect)

    # 2. Draw Play Button
    # Define button dimensions and position
    button_width = 200
    button_height = 75
    button_x = assets.width // 2 - button_width // 2
    button_y = assets.height // 2

    play_button = pygame.Rect(button_x, button_y, button_width, button_height)
    
    # Check for hover/click
    mouse_pos = pygame.mouse.get_pos()
    button_color = BRIGHT_GREEN if play_button.collidepoint(mouse_pos) else GREEN
    
    # Draw the button rectangle
    pygame.draw.rect(screen, button_color, play_button)

    # Draw the button text
    if BUTTON_FONT:
        text = BUTTON_FONT.render("Play", True, BLACK)
        text_rect = text.get_rect(center=play_button.center)
        screen.blit(text, text_rect)

    # 3. Handle Events for the Menu
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if play_button.collidepoint(event.pos):
                # Transition to the GAME_STATE
                current_state = GAME_STATE
                # Re-initialize game if needed (optional, but safe)
                # global game, player_turn, board_turn, free_play
                # game = Game({...}) # Recreate the game object
                # player_turn = "X" 
                # board_turn = (1,1)
                # free_play = True
                
    pygame.display.flip()

    return current_state

