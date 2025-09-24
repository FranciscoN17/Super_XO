import pygame

win_infos = {
    (0,0): None, (0,1): None, (0,2): None,
    (1,0): None, (1,1): None, (1,2): None,
    (2,0): None, (2,1): None, (2,2): None,
}

board_infos = [[{
    (0,0): None, (0,1): None, (0,2): None,
    (1,0): None, (1,1): None, (1,2): None,
    (2,0): None, (2,1): None, (2,2): None,
},
{
    (0,0): None, (0,1): None, (0,2): None,
    (1,0): None, (1,1): None, (1,2): None,
    (2,0): None, (2,1): None, (2,2): None,
},
{
    (0,0): None, (0,1): None, (0,2): None,
    (1,0): None, (1,1): None, (1,2): None,
    (2,0): None, (2,1): None, (2,2): None,
}],
[{
    (0,0): None, (0,1): None, (0,2): None,
    (1,0): None, (1,1): None, (1,2): None,
    (2,0): None, (2,1): None, (2,2): None,
},
{
    (0,0): None, (0,1): None, (0,2): None,
    (1,0): None, (1,1): None, (1,2): None,
    (2,0): None, (2,1): None, (2,2): None,
},
{
    (0,0): None, (0,1): None, (0,2): None,
    (1,0): None, (1,1): None, (1,2): None,
    (2,0): None, (2,1): None, (2,2): None,
}],
[{
    (0,0): None, (0,1): None, (0,2): None,
    (1,0): None, (1,1): None, (1,2): None,
    (2,0): None, (2,1): None, (2,2): None,
},
{
    (0,0): None, (0,1): None, (0,2): None,
    (1,0): None, (1,1): None, (1,2): None,
    (2,0): None, (2,1): None, (2,2): None,
},
{
    (0,0): None, (0,1): None, (0,2): None,
    (1,0): None, (1,1): None, (1,2): None,
    (2,0): None, (2,1): None, (2,2): None,
}]]

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

def get_board_key_from_pos(pos, board_table):
    if pos:
        x, y = pos
        for key, value in board_table.items():
            vx, vy = value
            if vx <= x < vx + 60 and vy <= y < vy + 60:
                return key
    return None

def handle_click(event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            return mouse_pos
        return None

def check_winner(board_info):
    # Check rows
    for row in range(3):
        if board_info[(row, 0)] == board_info[(row, 1)] == board_info[(row, 2)] != None:
            return board_info[(row, 0)]
    # Check columns
    for col in range(3):
        if board_info[(0, col)] == board_info[(1, col)] == board_info[(2, col)] != None:
            return board_info[(0, col)]
    # Check diagonals
    if board_info[(0, 0)] == board_info[(1, 1)] == board_info[(2, 2)] != None:
        return board_info[(0, 0)]
    if board_info[(0, 2)] == board_info[(1, 1)] == board_info[(2, 0)] != None:
        return board_info[(0, 2)]
    return None

def check_global_winner(board_infos):
    # Create a summary board to check for global winner
    summary_board = {}
    for i in range(3):
        for j in range(3):
            local_winner = check_winner(board_infos[i][j])
            summary_board[(i, j)] = local_winner

    return check_winner(summary_board)