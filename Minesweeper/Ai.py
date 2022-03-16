import pygame
import Board
import math

class Ai_tile(pygame.sprite.Sprite):
    def __init__(self, pos) -> None:
        super().__init__()
        self.image = pygame.Surface((tilesize, tilesize), pygame.SRCALPHA)
        self.rect = self.image.get_rect(topleft=pos)
        self.image.fill((0, 0, 0, 0))

    def set_alpha(self, alpha):
        self.image.fill((0, 0, 0, alpha))

    def set_col(self, col):
        self.image.fill(col)


def convert_pos(pos: tuple) -> int:
    if not Board.on_board(pos[0], pos[1]):
        raise IndexError(f'Position {pos} is not on the board... Dum Dum')
    return pos[0]*length+pos[1]


def reset_grid():
    for tile in grid:
        tile.set_alpha(0)


def init(Length, Height, Tilesize) -> None:
    global tilesize, ai_tiles, grid, length, height
    tilesize = Tilesize
    length = Length
    height = Height

    ai_tiles = pygame.sprite.Group()
    grid = []
    for h in range(Height):
        for l in range(Length):
            grid.append(Ai_tile((l*tilesize, h*tilesize)))
    ai_tiles.add(grid)        

# The 'M' is not used, this could be re-writin as {...[y][x] in ['1','2','3' ect]}
# get_mines is not acessed outside of the display
def get_prob() -> None:
    global grid
    prob_grid = [[0 for x in range(length)] for y in range(height)]
    reset_grid()
    for y in range(height):
        for x in range(length):
            if Board.board[y][x] not in [' ', '0', 'F', 'M']:

                if Board.get_flags(y, x) == Board.board[y][x] and Board.get_spaces(y, x) not in [0, '0']:
                    grid[convert_pos((y, x))].set_col((255, 0, 0, 175))
                    return None

                for diff in ((1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1)):

                    Y = y + diff[0]
                    X = x + diff[1]

                    if not Board.on_board(Y, X):
                        continue

                    if Board.board[Y][X] not in [' ', 'M']:
                        continue

                    mines = Board.get_mines(y, x)
                    spaces = Board.get_spaces(y, x)

                    if spaces == 0 or mines == '0':
                        continue

                    prob_grid[Y][X] += int(mines)/spaces

    heighest = 0

    for arr in prob_grid:
        if max(arr) > heighest:
            heighest = max(arr)

    for y in range(height):
        for x in range(length):
            if prob_grid[y][x] == 0:
                continue

            offset = prob_grid[y][x] * math.floor((255 / heighest))
            grid[convert_pos((y, x))].set_col((255-offset,255-offset,255))

