import pygame


def neighbours_color(x, y):
    neighbours = []
    for offset in range(-1, 2):
        if board[x + offset][y - 1] == 1:
            neighbours.append(1)
        else:
            neighbours.append(0)
    return neighbours


def set_rule(x, y):
    neighbours = neighbours_color(x, y)

    if neighbours == [1, 1, 1]:
        board[x][y] = 0
    elif neighbours == [1, 1, 0]:
        board[x][y] = 0
    elif neighbours == [1, 0, 1]:
        board[x][y] = 0
    elif neighbours == [1, 0, 0]:
        board[x][y] = 1
    elif neighbours == [0, 1, 1]:
        board[x][y] = 1
    elif neighbours == [0, 1, 0]:
        board[x][y] = 1
    elif neighbours == [0, 0, 1]:
        board[x][y] = 1
    else:
        board[x][y] = 0


def new_board(line):
    for col in range(1, RESOLUTION - 1):
        set_rule(col, line)


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

DIMENSION_RATIO = 2
SCREEN_HEIGHT = 700
SCREEN_WIDTH = SCREEN_HEIGHT * DIMENSION_RATIO

RESOLUTION = 300  # on height
CELL_WIDTH = int(SCREEN_WIDTH / RESOLUTION)

launched = True
board = [[0 for _ in range(RESOLUTION * DIMENSION_RATIO)] for _ in range(RESOLUTION)]
board[int(RESOLUTION / 2)][0] = 1  # first cell
current_line = 1

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Elementary Cellular Automaton - Rule 30")

while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launched = False
    screen.fill(WHITE)
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                pygame.draw.rect(screen, BLACK, [i * CELL_WIDTH, j * CELL_WIDTH, CELL_WIDTH, CELL_WIDTH])
    new_board(current_line)
    current_line += 1
    pygame.display.update()
