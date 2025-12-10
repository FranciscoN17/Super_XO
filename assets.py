import pygame

if not pygame.get_init():
    pygame.init()

height = 800
width = 800
board_sprite = pygame.transform.scale(pygame.image.load("assets/board.png"), (width, height))

x_sprite = pygame.transform.scale(pygame.image.load("assets/x_sprite.png"), (60, 60))

o_sprite = pygame.transform.scale(pygame.image.load("assets/o_sprite.png"), (60, 60))

board_tables = [
    [
        {
            (0,0): (40, 40), (0,1): (106, 40), (0,2): (172, 40),
            (1,0): (40, 106), (1,1): (106, 106), (1,2): (172, 106),
            (2,0): (40, 172), (2,1): (106, 172), (2,2): (172, 172),
        },
        {
            (0,0): (303, 40), (0,1): (369, 40), (0,2): (435, 40),
            (1,0): (303, 106), (1,1): (369, 106), (1,2): (435, 106),
            (2,0): (303, 172), (2,1): (369, 172), (2,2): (435, 172),
        },
        {
            (0,0): (566, 40), (0,1): (632, 40), (0,2): (698, 40),
            (1,0): (566, 106), (1,1): (632, 106), (1,2): (698, 106),
            (2,0): (566, 172), (2,1): (632, 172), (2,2): (698, 172),
        },
    ],
    [
        {
            (0,0): (40, 303), (0,1): (106, 303), (0,2): (172, 303),
            (1,0): (40, 369), (1,1): (106, 369), (1,2): (172, 369),
            (2,0): (40, 435), (2,1): (106, 435), (2,2): (172, 435),
        },
        {
            (0,0): (303, 303), (0,1): (369, 303), (0,2): (435, 303),
            (1,0): (303, 369), (1,1): (369, 369), (1,2): (435, 369),
            (2,0): (303, 435), (2,1): (369, 435), (2,2): (435, 435),
        },
        {
            (0,0): (566, 303), (0,1): (632, 303), (0,2): (698, 303),
            (1,0): (566, 369), (1,1): (632, 369), (1,2): (698, 369),
            (2,0): (566, 435), (2,1): (632, 435), (2,2): (698, 435),
        },
    ],
    [
        {
            (0,0): (40, 566), (0,1): (106, 566), (0,2): (172, 566),
            (1,0): (40, 632), (1,1): (106, 632), (1,2): (172, 632),
            (2,0): (40, 698), (2,1): (106, 698), (2,2): (172, 698),
        },
        {
            (0,0): (303, 566), (0,1): (369, 566), (0,2): (435, 566),
            (1,0): (303, 632), (1,1): (369, 632), (1,2): (435, 632),
            (2,0): (303, 698), (2,1): (369, 698), (2,2): (435, 698),
        },
        {
            (0,0): (566, 566), (0,1): (632, 566), (0,2): (698, 566),
            (1,0): (566, 632), (1,1): (632, 632), (1,2): (698, 632),
            (2,0): (566, 698), (2,1): (632, 698), (2,2): (698, 698),
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

