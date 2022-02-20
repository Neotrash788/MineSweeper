import Board

def guess(y: int, x: int) -> None:
    #[print(i) for i in Board.board]

    if Board.board[y][x] == 'M':
        print(f'Space ({y},{x}) Was A Mine')
        exit()

    if Board.board[y][x] not in [' ','M','F']:
        print('MINEs -> ' + str(Board.get_mines(y,x)))
        print('FLAGS -> ' + str(Board.get_flags(y,x)))

        if Board.get_mines(y,x) == Board.get_flags(y,x):
            for diff in ((1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1)):
                Y = y + diff[0]
                X = x + diff[1]

                if Board.on_board(Y,X):
                    if Board.board[Y][X] == ' ':
                        guess(Y,X)
            print('NUMBER FILLED')
        return None

    if Board.get_mines(y, x) != '0' and Board.board[y][x] == ' ':
        Board.board[y][x] = Board.get_mines(y, x)
        

    else:
        Board.board[y][x] = '0'
        for diff in ((1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1)):

            Y = y + diff[0]
            X = x + diff[1]

            if Board.on_board(Y, X):
                if Board.board[Y][X] != '0' and Board.get_space(Y, X) == ' ':
                    guess(Y, X)


def flag(y: int, x: int) -> None:
    Board.flag(y, x)
    Board.check_for_win()