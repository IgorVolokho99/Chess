import time


class Coord:
    def __init__(self, y, x):
        self.y = y
        self.x = x
        self.valide = True
        self.check_valid()

    def check_valid(self):
        if self.x in range(8) and self.y in range(8):
            self.valide = True
        else:
            self.valide = False

    def __eq__(self, other):
        return self.y == other.y and self.x == other.x

    def __repr__(self):
        return f"y : {self.y} ; x : {self.x}"


class Move:
    def __init__(self):
        self.from_cell = Coord(-1, -1)
        self.to_cell = Coord(-1, -1)


class Figure:
    def __init__(self, type_of_figure: str, coord: Coord):
        self.type_of_figure = type_of_figure
        self.coord = coord
        self.moves = []

    def generate_move(self, board):
        if self.type_of_figure.upper() == 'K':
            self.generate_king_move(board)
        elif self.type_of_figure.upper() == 'R':
            self.generate_rook_move(board)
        elif self.type_of_figure.upper() == 'B':
            self.generate_bishop_move(board)
        elif self.type_of_figure.upper() == 'Q':
            self.generate_queen_move(board)
        elif self.type_of_figure.upper() == 'N':
            self.generate_knight_move(board)
        elif self.type_of_figure == 'P':
            self.generate_white_pawn_move(board)
        elif self.type_of_figure == 'p':
            self.generate_black_pawn_move(board)

    def generate_king_move(self, board):
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                if dx != 0 or dy != 0:
                    to = self.new_coord(self.coord, (dy, dx))
                    if to.valide:
                        if board[to.y][to.x] == '-':
                            self.moves.append(to)
                        elif board[self.coord.y][self.coord.x].isupper() != board[to.y][to.x].isupper():
                            self.moves.append(to)

    def generate_rook_move(self, board):
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        for dy, dx in directions:
            for i in range(1, 8):
                to = self.new_coord(self.coord, (dy * i, dx * i))
                if to.valide:
                    if board[to.y][to.x] == '-':
                        self.moves.append(to)
                    elif board[self.coord.y][self.coord.x].isupper() != board[to.y][to.x].isupper():
                        self.moves.append(to)
                        break
                    else:
                        break

    def generate_bishop_move(self, board):
        directions = ((1, 1), (-1, 1), (1, -1), (-1, -1))
        for dy, dx in directions:
            for i in range(1, 8):
                to = self.new_coord(self.coord, (dy * i, dx * i))
                if to.valide:
                    if board[to.y][to.x] == '-':
                        self.moves.append(to)
                    elif board[self.coord.y][self.coord.x].isupper() != board[to.y][to.x].isupper():
                        self.moves.append(to)
                        break
                    else:
                        break

    def generate_queen_move(self, board):
        self.generate_rook_move(board)
        self.generate_bishop_move(board)

    def generate_knight_move(self, board):
        directions = ((1, -2), (-1, -2), (1, 2), (-1, 2), (2, -1), (2, 1), (-2, -1), (-2, 1))
        for dy, dx in directions:
            to = self.new_coord(self.coord, (dy, dx))
            if to.valide:
                if board[to.y][to.x] == '-':
                    self.moves.append(to)
                elif board[self.coord.y][self.coord.x].isupper() != board[to.y][to.x].isupper():
                    self.moves.append(to)

    def generate_white_pawn_move(self, board):
        to = self.new_coord(self.coord, (-1, 0))  # SIMPLE MOVE
        if to.valide:
            if board[to.y][to.x] == '-':
                self.moves.append(to)
        if self.coord.y == 6:
            to = self.new_coord(self.coord, (-2, 0))  # SIMPLE MOVE IN FIRST MOVE
            if to.valide:
                if board[to.y][to.x] == '-' and board[to.y + 1][to.x] == '-':
                    self.moves.append(to)
        to = self.new_coord(self.coord, (-1, -1))  # ATTACK 1
        if to.valide and board[to.y][to.x] != '-':
            if board[self.coord.y][self.coord.x].isupper() != board[to.y][to.x].isupper():
                self.moves.append(to)
        to = self.new_coord(self.coord, (-1, 1))  # ATTACK 2
        if to.valide and board[to.y][to.x] != '-':
            if board[self.coord.y][self.coord.x].isupper() != board[to.y][to.x].isupper():
                self.moves.append(to)

    def generate_black_pawn_move(self, board):
        to = self.new_coord(self.coord, (1, 0))  # SIMPLE MOVE
        if to.valide:
            if board[to.y][to.x] == '-':
                self.moves.append(to)
        if self.coord.y == 1:
            to = self.new_coord(self.coord, (2, 0))  # SIMPLE MOVE IN FIRST MOVE
            if to.valide:
                if board[to.y][to.x] == '-' and board[to.y - 1][to.x] == '-':
                    self.moves.append(to)
        to = self.new_coord(self.coord, (1, -1))  # ATTACK 1
        if to.valide and board[to.y][to.x] != '-':
            if board[self.coord.y][self.coord.x].isupper() != board[to.y][to.x].isupper():
                self.moves.append(to)
        to = self.new_coord(self.coord, (1, 1))  # ATTACK 2
        if to.valide and board[to.y][to.x] != '-':
            if board[self.coord.y][self.coord.x].isupper() != board[to.y][to.x].isupper():
                self.moves.append(to)

    @staticmethod
    def new_coord(coord, to):
        return Coord(coord.y + to[0], coord.x + to[1])

    def __repr__(self):
        return f"type : {self.type_of_figure} ; coord : {self.coord}"


class Chess:
    def __init__(self, fen: str):
        self.board = [['-'] * 8 for _ in range(8)]
        self.order_of_move = 'w'
        self.castling = {'K': False, 'Q': False, 'k': False, 'q': False}
        self.move_in_two_cells = Coord(-1, -1)
        self.amount_of_moves = 0
        self.amount_of_moves_without_pawn = 1
        self.white_figuers = []
        self.black_figuers = []

        self.parse_fen(fen)

        self.generate_moves()  # Реализовать

    def parse_fen(self, fen: str):
        data = fen.split(' ')
        # data[0] = data[0][::-1]
        board_fen = data[0].split('/')

        for i in range(len(board_fen)):
            j, k = 0, 0
            while j < len(self.board[i]):
                if not board_fen[i][k].isdigit():
                    if board_fen[i][k].isupper():
                        self.white_figuers.append(Figure(board_fen[i][k], Coord(i, j)))
                    else:
                        self.black_figuers.append(Figure(board_fen[i][k], Coord(i, j)))
                    self.board[i][j] = board_fen[i][k]
                    j += 1
                else:
                    j += int(board_fen[i][k])
                k += 1

        self.order_of_move = data[1]

        for char in data[2]:
            self.castling[char] = True

        self.move_in_two_cells = self.from_letters_to_coord(data[3])

        self.amount_of_moves_without_pawn = int(data[4])
        self.amount_of_moves = int(data[5])

    def show_board(self):
        for i in range(len(self.board)):
            print(self.board[i])

    def generate_moves(self):
        if self.order_of_move == 'w':
            for figure in self.white_figuers:
                figure.generate_move(self.board)
        if self.order_of_move == 'w':
            for figure in self.black_figuers:
                figure.generate_move(self.board)

    def show_moves(self):
        for figure in self.white_figuers:
            if len(figure.moves) > 0:
                for i in range(len(self.board)):
                    for j in range(len(self.board[i])):
                        if Coord(i, j) == figure.coord:
                            print(figure.type_of_figure, end=' ')
                        elif Coord(i, j) in figure.moves:
                            print('*', end=' ')
                        else:
                            print('-', end=' ')
                    print()
                print('------------------------------------------')

        for figure in self.black_figuers:
            if len(figure.moves) > 0:
                for i in range(len(self.board)):
                    for j in range(len(self.board[i])):
                        if Coord(i, j) == figure.coord:
                            print(figure.type_of_figure, end=' ')
                        elif Coord(i, j) in figure.moves:
                            print('*', end=' ')
                        else:
                            print('-', end=' ')
                    print()
                print('------------------------------------------')

    @staticmethod
    def from_letters_to_coord(coord_with_letters: str) -> Coord:
        if coord_with_letters == '-':
            return Coord(-1, -1)
        helper = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
        coord = Coord(helper[coord_with_letters[0]], coord_with_letters[1])
        return coord


# # TEST 1 - START POSITION
# c = Chess('rnbq1bnr/pppkpppp/8/2p2p1R/4P3/5N2/PPPP1PPP/RNBQKB1R w KQ - 2 3')
# c.show_board()
# c.show_moves()

# # TEST 2 - ONE KING POSITION
# c = Chess('8/8/8/3ppp3/3pKp3/3ppp3/8/8 w - - 0 1')
# c.show_board()
# c.show_moves()

# # TEST 3 -  TWO KINS POSITION
# c = Chess('8/3PPP2/3PkP2/3PPP2/8/3ppp2/3pKp2/3ppp2 w - - 0 1')
# c.show_board()
# c.show_moves()

# # TEST 4 - ONE ROOK POSITION
# c = Chess('8/8/8/8/8/8/8/7R w - - 0 1')
# c.show_board()
# c.show_moves()

# # TEST 5 - ONE ROOK POSITION
# c = Chess('8/8/8/8/8/7p/8/5P1R w - - 0 1')
# c.show_board()
# c.show_moves()

# # TEST 6 - SEVERAL ROOKS POSITION
# c = Chess('r6R/8/8/8/8/8/8/r6R w - - 0 1')
# c.show_board()
# c.show_moves()

# # TEST 7 - ONE BISHOP POSITION
# c = Chess('8/8/8/8/4B3/8/8/8 w - - 0 1')
# c.show_board()
# c.show_moves()

# # TEST 8 - ONE QUEEN POSITION
# c = Chess('8/8/8/8/4Q3/8/8/8 w - - 0 1')
# c.show_board()
# c.show_moves()

# # TEST 9 - ONE KNIGHT POSITION
# c = Chess('8/8/8/8/4N3/8/8/8 w - - 0 1')
# c.show_board()
# c.show_moves()

# # TEST 10 - ONE KNIGHT POSITION
# c = Chess('8/8/8/8/7N/8/8/8 w - - 0 1')
# c.show_board()
# c.show_moves()


# # TEST 11 - SEVERAL PAWNS POSITION
# c = Chess('8/4p3/4p3/8/8/4P3/4P3/8 w - - 0 1')
# c.show_board()
# c.show_moves()

# # TEST 12 - SEVERAL PAWNS POSITION
# c = Chess('8/8/8/8/8/3p1p2/4P3/8 w - - 0 1')
# c.show_board()
# c.show_moves()


start = time.time()
for _ in range(10_000):
    c = Chess('rnbq1bnr/pppkpppp/8/2p2p1R/4P3/5N2/PPPP1PPP/RNBQKB1R w KQ - 2 3')
    #c.show_board()
    #c.show_moves()

finish = time.time()
print(finish - start)
