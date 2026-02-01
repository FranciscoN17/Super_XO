import pygame

if not pygame.get_init():
    pygame.init()

GAME_SIZE = 800
HEIGHT = GAME_SIZE
WIDTH = GAME_SIZE

board_sprite = pygame.transform.scale(pygame.image.load("assets/board.png"), (WIDTH, HEIGHT))

x_sprite = pygame.transform.scale(pygame.image.load("assets/x_sprite.png"), (60/800 * HEIGHT, 60/800 * HEIGHT))

o_sprite = pygame.transform.scale(pygame.image.load("assets/o_sprite.png"), (60/800 * HEIGHT, 60/800 * HEIGHT))

board_tables = [
    [
        {
            (0,0): (HEIGHT/20, HEIGHT/20),                                  (0,1): (HEIGHT/20 + HEIGHT/12, HEIGHT/20),                                  (0,2): (HEIGHT/20 + 2*HEIGHT/12, HEIGHT/20),
            (1,0): (HEIGHT/20, HEIGHT/20 + HEIGHT/12),                      (1,1): (HEIGHT/20 + HEIGHT/12, HEIGHT/20 + HEIGHT/12),                      (1,2): (HEIGHT/20 + 2*HEIGHT/12, HEIGHT/20 + HEIGHT/12),
            (2,0): (HEIGHT/20, HEIGHT/20 + 2*HEIGHT/12),                    (2,1): (HEIGHT/20 + HEIGHT/12, HEIGHT/20 + 2*HEIGHT/12),                    (2,2): (HEIGHT/20 + 2*HEIGHT/12, HEIGHT/20 + 2*HEIGHT/12),
        },
        {
            (0,0): (HEIGHT/20 + 263/800*HEIGHT, HEIGHT/20),                 (0,1): (HEIGHT/20 + 263/800*HEIGHT + HEIGHT/12, HEIGHT/20),                 (0,2): (HEIGHT/20 + 263/800*HEIGHT + 2*HEIGHT/12, HEIGHT/20),
            (1,0): (HEIGHT/20 + 263/800*HEIGHT, HEIGHT/20 + HEIGHT/12),     (1,1): (HEIGHT/20 + 263/800*HEIGHT + HEIGHT/12, HEIGHT/20 + HEIGHT/12),     (1,2): (HEIGHT/20 + 263/800*HEIGHT + 2*HEIGHT/12, HEIGHT/20 + HEIGHT/12),
            (2,0): (HEIGHT/20 + 263/800*HEIGHT, HEIGHT/20 + 2*HEIGHT/12),   (2,1): (HEIGHT/20 + 263/800*HEIGHT + HEIGHT/12, HEIGHT/20 + 2*HEIGHT/12),   (2,2): (HEIGHT/20 + 263/800*HEIGHT + 2*HEIGHT/12, HEIGHT/20 + 2*HEIGHT/12),
        },
        {
            (0,0): (HEIGHT/20 + 2*263/800*HEIGHT, HEIGHT/20),               (0,1): (HEIGHT/20 + 2*263/800*HEIGHT + HEIGHT/12, HEIGHT/20),               (0,2): (HEIGHT/20 + 2*263/800*HEIGHT + 2*HEIGHT/12, HEIGHT/20),
            (1,0): (HEIGHT/20 + 2*263/800*HEIGHT, HEIGHT/20 + HEIGHT/12),   (1,1): (HEIGHT/20 + 2*263/800*HEIGHT + HEIGHT/12, HEIGHT/20 + HEIGHT/12),   (1,2): (HEIGHT/20 + 2*263/800*HEIGHT + 2*HEIGHT/12, HEIGHT/20 + HEIGHT/12),
            (2,0): (HEIGHT/20 + 2*263/800*HEIGHT, HEIGHT/20 + 2*HEIGHT/12), (2,1): (HEIGHT/20 + 2*263/800*HEIGHT + HEIGHT/12, HEIGHT/20 + 2*HEIGHT/12), (2,2): (HEIGHT/20 + 2*263/800*HEIGHT + 2*HEIGHT/12, HEIGHT/20 + 2*HEIGHT/12),
        }
    ],
    [
        {
            (0,0): (HEIGHT/20, HEIGHT/20 + HEIGHT/3),                                          (0,1): (HEIGHT/20 + HEIGHT/12, HEIGHT/20 + HEIGHT/3),                                          (0,2): (HEIGHT/20 + 2*HEIGHT/12, HEIGHT/20 + HEIGHT/3),
            (1,0): (HEIGHT/20, HEIGHT/20 + HEIGHT/3 + HEIGHT/12),                              (1,1): (HEIGHT/20 + HEIGHT/12, HEIGHT/20 + HEIGHT/3 + HEIGHT/12),                              (1,2): (HEIGHT/20 + 2*HEIGHT/12, HEIGHT/20 + HEIGHT/3 + HEIGHT/12),
            (2,0): (HEIGHT/20, HEIGHT/20 + HEIGHT/3 + 2*HEIGHT/12),                            (2,1): (HEIGHT/20 + HEIGHT/12, HEIGHT/20 + HEIGHT/3 + 2*HEIGHT/12),                            (2,2): (HEIGHT/20 + 2*HEIGHT/12, HEIGHT/20 + HEIGHT/3 + 2*HEIGHT/12),
        },
        {
            (0,0): (HEIGHT/20 + 263/800*HEIGHT, HEIGHT/20 + 263/800*HEIGHT),                   (0,1): (HEIGHT/20 + 263/800*HEIGHT + HEIGHT/12, HEIGHT/20 + 263/800*HEIGHT),                   (0,2): (HEIGHT/20 + 263/800*HEIGHT + 2*HEIGHT/12, HEIGHT/20 + 263/800*HEIGHT),
            (1,0): (HEIGHT/20 + 263/800*HEIGHT, HEIGHT/20 + 263/800*HEIGHT + HEIGHT/12),       (1,1): (HEIGHT/20 + 263/800*HEIGHT + HEIGHT/12, HEIGHT/20 + 263/800*HEIGHT + HEIGHT/12),       (1,2): (HEIGHT/20 + 263/800*HEIGHT + 2*HEIGHT/12, HEIGHT/20 + 263/800*HEIGHT + HEIGHT/12),
            (2,0): (HEIGHT/20 + 263/800*HEIGHT, HEIGHT/20 + 263/800*HEIGHT + 2*HEIGHT/12),     (2,1): (HEIGHT/20 + 263/800*HEIGHT + HEIGHT/12, HEIGHT/20 + 263/800*HEIGHT + 2*HEIGHT/12),     (2,2): (HEIGHT/20 + 263/800*HEIGHT + 2*HEIGHT/12, HEIGHT/20 + 263/800*HEIGHT + 2*HEIGHT/12),
        },
        {
            (0,0): (HEIGHT/20 + 2*263/800*HEIGHT, HEIGHT/20 + 263/800*HEIGHT),                 (0,1): (HEIGHT/20 + 2*263/800*HEIGHT + HEIGHT/12, HEIGHT/20 + 263/800*HEIGHT),                 (0,2): (HEIGHT/20 + 2*263/800*HEIGHT + 2*HEIGHT/12, HEIGHT/20 + 263/800*HEIGHT),
            (1,0): (HEIGHT/20 + 2*263/800*HEIGHT, HEIGHT/20 + 263/800*HEIGHT + HEIGHT/12),     (1,1): (HEIGHT/20 + 2*263/800*HEIGHT + HEIGHT/12, HEIGHT/20 + 263/800*HEIGHT + HEIGHT/12),     (1,2): (HEIGHT/20 + 2*263/800*HEIGHT + 2*HEIGHT/12, HEIGHT/20 + 263/800*HEIGHT + HEIGHT/12),
            (2,0): (HEIGHT/20 + 2*263/800*HEIGHT, HEIGHT/20 + 263/800*HEIGHT + 2*HEIGHT/12),   (2,1): (HEIGHT/20 + 2*263/800*HEIGHT + HEIGHT/12, HEIGHT/20 + 263/800*HEIGHT + 2*HEIGHT/12),   (2,2): (HEIGHT/20 + 2*263/800*HEIGHT + 2*HEIGHT/12, HEIGHT/20 + 263/800*HEIGHT + 2*HEIGHT/12),
        },
    ],
    [
        {
            (0,0): (HEIGHT/20, HEIGHT/20 + 2*263/800*HEIGHT),                                  (0,1): (HEIGHT/20 + HEIGHT/12, HEIGHT/20 + 2*263/800*HEIGHT),                                  (0,2): (HEIGHT/20 + 2*HEIGHT/12, HEIGHT/20 + 2*263/800*HEIGHT),
            (1,0): (HEIGHT/20, HEIGHT/20 + 2*263/800*HEIGHT + HEIGHT/12),                      (1,1): (HEIGHT/20 + HEIGHT/12, HEIGHT/20 + 2*263/800*HEIGHT + HEIGHT/12),                      (1,2): (HEIGHT/20 + 2*HEIGHT/12, HEIGHT/20 + 2*263/800*HEIGHT + HEIGHT/12),
            (2,0): (HEIGHT/20, HEIGHT/20 + 2*263/800*HEIGHT + 2*HEIGHT/12),                    (2,1): (HEIGHT/20 + HEIGHT/12, HEIGHT/20 + 2*263/800*HEIGHT + 2*HEIGHT/12),                    (2,2): (HEIGHT/20 + 2*HEIGHT/12, HEIGHT/20 + 2*263/800*HEIGHT + 2*HEIGHT/12),
        },
        {
            (0,0): (HEIGHT/20 + 263/800*HEIGHT, HEIGHT/20 + 2*263/800*HEIGHT),                 (0,1): (HEIGHT/20 + 263/800*HEIGHT + HEIGHT/12, HEIGHT/20 + 2*263/800*HEIGHT),                 (0,2): (HEIGHT/20 + 263/800*HEIGHT + 2*HEIGHT/12, HEIGHT/20 + 2*263/800*HEIGHT),
            (1,0): (HEIGHT/20 + 263/800*HEIGHT, HEIGHT/20 + 2*263/800*HEIGHT + HEIGHT/12),     (1,1): (HEIGHT/20 + 263/800*HEIGHT + HEIGHT/12, HEIGHT/20 + 2*263/800*HEIGHT + HEIGHT/12),     (1,2): (HEIGHT/20 + 263/800*HEIGHT + 2*HEIGHT/12, HEIGHT/20 + 2*263/800*HEIGHT + HEIGHT/12),
            (2,0): (HEIGHT/20 + 263/800*HEIGHT, HEIGHT/20 + 2*263/800*HEIGHT + 2*HEIGHT/12),   (2,1): (HEIGHT/20 + 263/800*HEIGHT + HEIGHT/12, HEIGHT/20 + 2*263/800*HEIGHT + 2*HEIGHT/12),   (2,2): (HEIGHT/20 + 263/800*HEIGHT + 2*HEIGHT/12, HEIGHT/20 + 2*263/800*HEIGHT + 2*HEIGHT/12),
        },
        {
            (0,0): (HEIGHT/20 + 2*263/800*HEIGHT, HEIGHT/20 + 2*263/800*HEIGHT),               (0,1): (HEIGHT/20 + 2*263/800*HEIGHT + HEIGHT/12, HEIGHT/20 + 2*263/800*HEIGHT),               (0,2): (HEIGHT/20 + 2*263/800*HEIGHT + 2*HEIGHT/12, HEIGHT/20 + 2*263/800*HEIGHT),
            (1,0): (HEIGHT/20 + 2*263/800*HEIGHT, HEIGHT/20 + 2*263/800*HEIGHT + HEIGHT/12),   (1,1): (HEIGHT/20 + 2*263/800*HEIGHT + HEIGHT/12, HEIGHT/20 + 2*263/800*HEIGHT + HEIGHT/12),   (1,2): (HEIGHT/20 + 2*263/800*HEIGHT + 2*HEIGHT/12, HEIGHT/20 + 2*263/800*HEIGHT + HEIGHT/12),
            (2,0): (HEIGHT/20 + 2*263/800*HEIGHT, HEIGHT/20 + 2*263/800*HEIGHT + 2*HEIGHT/12), (2,1): (HEIGHT/20 + 2*263/800*HEIGHT + HEIGHT/12, HEIGHT/20 + 2*263/800*HEIGHT + 2*HEIGHT/12), (2,2): (HEIGHT/20 + 2*263/800*HEIGHT + 2*HEIGHT/12, HEIGHT/20 + 2*263/800*HEIGHT + 2*HEIGHT/12),
        },
    ],
]
# --- New Font Definitions ---
FONT_PATH = "assets/PressStart2P-vaV7.ttf" # Adjust this path if needed!

# Load the font and handle potential file not found error
try:
    # Title Font (larger)
    TITLE_FONT = pygame.font.Font(FONT_PATH, 48)
    
    # Button/UI Font (smaller)
    BUTTON_FONT = pygame.font.Font(FONT_PATH, 32)
    
    # You could also define a smaller font for in-game text
    SMALL_FONT = pygame.font.Font(FONT_PATH, 20)

except pygame.error as e:
    print(f"Error loading font file: {FONT_PATH}. Falling back to default font.")
    # Fallback to a system font if the custom one fails
    TITLE_FONT = pygame.font.Font(None, 74)
    BUTTON_FONT = pygame.font.Font(None, 50)
    SMALL_FONT = pygame.font.Font(None, 30)

