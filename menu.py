import pygame
import assets

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
BRIGHT_GREEN = (0, 255, 0)


def draw_menu(screen, events, current_state, GAME_STATE):
    """Draws the main menu and handles menu events."""

    screen.fill(BLACK)

    # 1. Draw Title
    title_text = assets.TITLE_FONT.render("Super XO", False, WHITE)
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
    text = assets.BUTTON_FONT.render("Play", True, BLACK)
    text_rect = text.get_rect(center=play_button.center)
    screen.blit(text, text_rect)

    # 3. Handle Events for the Menu
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if play_button.collidepoint(event.pos):
                # Transition to the GAME_STATE
                current_state = GAME_STATE

    pygame.display.flip()

    return current_state

def draw_game_over(screen, events, current_state, MENU_STATE):
    """Draws the game over screen and handles events."""
    
    screen.fill(BLACK)

    if current_state == 2:
        title = "It's a Draw!"
    elif current_state == 3:
        title = "X Wins!"
    elif current_state == 4:
        title = "O Wins!"
    else:
        title = "Game Over"


    # 1. Draw Game Over Title
    title_text = assets.TITLE_FONT.render(title, False, WHITE)
    title_rect = title_text.get_rect(center=(assets.width // 2, assets.height // 4))
    screen.blit(title_text, title_rect)

    # 2. Draw Return to Menu Button
    # button_width = 300
    button_width = 600
    button_height = 75
    button_x = assets.width // 2 - button_width // 2
    button_y = assets.height // 2

    menu_button = pygame.Rect(button_x, button_y, button_width, button_height)
    
    # Check for hover/click
    mouse_pos = pygame.mouse.get_pos()
    button_color = BRIGHT_GREEN if menu_button.collidepoint(mouse_pos) else GREEN
    
    # Draw the button rectangle
    pygame.draw.rect(screen, button_color, menu_button)

    # Draw the button text
    text = assets.BUTTON_FONT.render("Return to Menu", True, BLACK)
    text_rect = text.get_rect(center=menu_button.center)
    screen.blit(text, text_rect)

    # 3. Handle Events for the Game Over Screen
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if menu_button.collidepoint(event.pos):
                # Transition back to the MENU_STATE
                current_state = MENU_STATE
                
    pygame.display.flip()

    return current_state