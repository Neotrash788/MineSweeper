import random
import math


def init(Length: int, Height: int, Mines: int) -> None:
    global board, length, height, flags, mines
    mines = []
    flags = []
    length = Length
    height = Height

    board = [[' ' for i in range(length)] for ii in range(height)]

    l, h = 0, 0
    while Mines >= 1:
        if random.randint(0, math.floor((length*height)/Mines)) == 1 and board[h][l] != 'M':
            board[h][l] = 'M'
            mines.append((h, l))
            Mines -= 1
        l += 1

        if l == Length:
            l = 0
            h += 1

        if h == Height:
            h, l = 0, 0


def on_board(y: int, x: int) -> bool:
    if x <= -1:
        return False
    if y <= -1:
        return False
    if x >= length:
        return False
    if x < 0:
        return False
    if y >= height:
        return False

    if x + (y*length) >= length*height:
        return False
    if x + (y*length) <= -1:
        return False

    return True


def get_space(y: int, x: int) -> int or str:
    return board[y][x]


def get_spaces(y: int, x: int) -> int:
    spaces = 0
    for difrance in ((1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1)):

        Y = y + difrance[0]
        X = x + difrance[1]

        if not on_board(Y, X):
            continue

        if board[Y][X] in [' ', 'M']:
            spaces += 1

    return spaces


def get_mines(y: int, x: int) -> str:
    mine_count = 0
    for difrance in ((1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1)):
        if on_board(y + difrance[0], x + difrance[1]):
            Y = y + difrance[0]
            X = x + difrance[1]
            if (Y, X) in mines:
                mine_count += 1
    return str(mine_count)


def flag(y: int, x: int) -> None:

    pos = ((y, x), board[y][x])

    for i in range(len(flags)-1, -1, -1):
        if pos[0] == flags[i][0]:
            board[y][x] = flags[i][1]
            flags.pop(i)
            return None
    else:
        flags.append(pos)
        board[y][x] = 'F'


def get_flags(y: int, x: int) -> str:
    FLAGS = 0
    for difrance in ((1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1)):
        Y = y + difrance[0]
        X = x + difrance[1]
        if on_board(Y, X):
            if board[Y][X] == 'F':
                FLAGS += 1
    return str(FLAGS)


def check_for_win():
    flag_list = [FLAG[0] for FLAG in flags]

    if len(flags) > len(mines):
        return None

    for mine in mines:
        if mine not in flag_list:
            return None

    print('YOU WIN!')
    exit()
