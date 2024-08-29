from moves import MOVES_OF_KNIGHT, MOVES_OF_ROOK, MOVES_OF_BISHOP


class Coord:
    def __init__(self, y=-1, x=-1):
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

    def generate_move(self, board, object_of_board):
        self.object = object_of_board
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

    def check_attack_to_king(self, board):
        directions = MOVES_OF_ROOK
        for dy, dx in directions:
            for i in range(1, 8):
                to = self.new_coord(self.coord, (dy * i, dx * i))
                if to.valide:
                    if board[to.y][to.x] != '-':
                        if board[self.coord.y][self.coord.x].isupper() != board[to.y][to.x].isupper():
                            if board[to.y][to.x].upper() in ('Q', 'R'):
                                return True
                            else:
                                break
                        else:
                            break

        directions = MOVES_OF_BISHOP
        for dy, dx in directions:
            for i in range(1, 8):
                to = self.new_coord(self.coord, (dy * i, dx * i))
                if to.valide:
                    if board[to.y][to.x] != '-':
                        if board[self.coord.y][self.coord.x].isupper() != board[to.y][to.x].isupper():
                            if board[to.y][to.x].upper() in ('Q', 'B'):
                                return True
                            else:
                                break
                        else:
                            break

        directions = MOVES_OF_KNIGHT
        for dy, dx in directions:
            to = self.new_coord(self.coord, (dy, dx))
            if to.valide:
                if board[to.y][to.x] != '-':
                    if board[self.coord.y][self.coord.x].isupper() != board[to.y][to.x].isupper():
                        if board[to.y][to.x].upper() == 'N':
                            return True

        directions_of_white_pawns = ((1, -1), (1, 1))
        directions_of_black_pawns = ((-1, -1), (-1, 1))
        directions = directions_of_black_pawns if self.type_of_figure.isupper() else directions_of_white_pawns
        for dy, dx in directions:
            to = self.new_coord(self.coord, (dy, dx))
            if to.valide:
                if board[to.y][to.x] != '-':
                    if board[self.coord.y][self.coord.x].isupper() != board[to.y][to.x].isupper():
                        if board[to.y][to.x].upper() == 'P':
                            return True

        return False

    @staticmethod
    def swap(board, fr, to):
        board[fr.y][fr.x], board[to.y][to.x] = board[to.y][to.x], board[fr.y][fr.x]
        return board

    def generate_king_move(self, board):
        figures_d = self.object.white_figures_d if self.type_of_figure.isupper() else self.object.black_figures_d
        union_king = figures_d['K' if self.type_of_figure.isupper() else 'k']

        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                if dx != 0 or dy != 0:
                    to = self.new_coord(self.coord, (dy, dx))
                    if to.valide:
                        if board[to.y][to.x] == '-':
                            self.swap(board, self.coord, to)
                            c = self.coord
                            self.coord = to
                            if not union_king.check_attack_to_king(board):
                                self.moves.append(to)
                                self.coord = c
                                self.swap(board, self.coord, to)

                            else:
                                self.coord = c
                                self.swap(board, self.coord, to)

                        elif board[self.coord.y][self.coord.x].isupper() != board[to.y][to.x].isupper():
                            fig = board[to.y][to.x]
                            board[to.y][to.x] = '-'
                            self.swap(board, self.coord, to)
                            c = self.coord
                            self.coord = to
                            if not union_king.check_attack_to_king(board):
                                self.moves.append(to)
                                self.coord = c
                                self.swap(board, self.coord, to)
                                board[to.y][to.x] = fig
                            else:
                                self.coord = c
                                self.swap(board, self.coord, to)
                                board[to.y][to.x] = fig

    def generate_rook_move(self, board):
        figures_d = self.object.white_figures_d if self.type_of_figure.isupper() else self.object.black_figures_d
        union_king = figures_d['K' if self.type_of_figure.isupper() else 'k']

        directions = MOVES_OF_ROOK
        for dy, dx in directions:
            for i in range(1, 8):  # 5  , 0
                to = self.new_coord(self.coord, (dy * i, dx * i))
                if to.valide:
                    if board[to.y][to.x] == '-':
                        self.swap(board, self.coord, to)
                        if not union_king.check_attack_to_king(board):
                            self.moves.append(to)
                            self.swap(board, self.coord, to)
                        else:
                            self.swap(board, self.coord, to)
                            # break
                    elif board[self.coord.y][self.coord.x].isupper() != board[to.y][to.x].isupper():
                        fig = board[to.y][to.x]
                        board[to.y][to.x] = '-'
                        self.swap(board, self.coord, to)
                        if not union_king.check_attack_to_king(board):
                            self.moves.append(to)
                            self.swap(board, self.coord, to)
                            board[to.y][to.x] = fig
                            break
                        else:
                            self.swap(board, self.coord, to)
                            board[to.y][to.x] = fig
                            # break
                    else:
                        break

    def generate_bishop_move(self, board):
        figures_d = self.object.white_figures_d if self.type_of_figure.isupper() else self.object.black_figures_d
        union_king = figures_d['K' if self.type_of_figure.isupper() else 'k']

        directions = MOVES_OF_BISHOP
        for dy, dx in directions:
            for i in range(1, 8):
                to = self.new_coord(self.coord, (dy * i, dx * i))
                if to.valide:
                    if board[to.y][to.x] == '-':
                        self.swap(board, self.coord, to)
                        if not union_king.check_attack_to_king(board):
                            self.moves.append(to)
                            self.swap(board, self.coord, to)
                        else:
                            self.swap(board, self.coord, to)
                            break
                    elif board[self.coord.y][self.coord.x].isupper() != board[to.y][to.x].isupper():
                        fig = board[to.y][to.x]
                        board[to.y][to.x] = '-'
                        self.swap(board, self.coord, to)
                        if not union_king.check_attack_to_king(board):
                            self.moves.append(to)
                            self.swap(board, self.coord, to)
                            board[to.y][to.x] = fig
                        else:
                            self.swap(board, self.coord, to)
                            board[to.y][to.x] = fig
                            break
                    else:
                        break

    def generate_queen_move(self, board):
        self.generate_rook_move(board)
        self.generate_bishop_move(board)

    def generate_knight_move(self, board):
        figures_d = self.object.white_figures_d if self.type_of_figure.isupper() else self.object.black_figures_d
        union_king = figures_d['K' if self.type_of_figure.isupper() else 'k']

        directions = MOVES_OF_KNIGHT
        for dy, dx in directions:
            to = self.new_coord(self.coord, (dy, dx))
            if to.valide:
                if board[to.y][to.x] == '-':
                    self.swap(board, self.coord, to)
                    if not union_king.check_attack_to_king(board):
                        self.moves.append(to)
                        self.swap(board, self.coord, to)
                    else:
                        self.swap(board, self.coord, to)
                elif board[self.coord.y][self.coord.x].isupper() != board[to.y][to.x].isupper():
                    fig = board[to.y][to.x]
                    board[to.y][to.x] = '-'
                    self.swap(board, self.coord, to)
                    if not union_king.check_attack_to_king(board):
                        self.moves.append(to)
                        self.swap(board, self.coord, to)
                        board[to.y][to.x] = fig
                    else:
                        self.swap(board, self.coord, to)
                        board[to.y][to.x] = fig

    def generate_white_pawn_move(self, board):
        figures_d = self.object.white_figures_d if self.type_of_figure.isupper() else self.object.black_figures_d
        union_king = figures_d['K' if self.type_of_figure.isupper() else 'k']

        to = self.new_coord(self.coord, (-1, 0))
        if to.valide and board[to.y][to.x] == '-':
            self.swap(board, self.coord, to)
            if not union_king.check_attack_to_king(board):
                self.moves.append(to)
                self.swap(board, self.coord, to)
            else:
                self.swap(board, self.coord, to)
        to = self.new_coord(self.coord, (-2, 0))
        if self.coord.y == 6 and to.valide and board[to.y][to.x] == '-' and board[to.y + 1][to.x] == '-':
            self.swap(board, self.coord, to)
            if not union_king.check_attack_to_king(board):
                self.moves.append(to)
                self.swap(board, self.coord, to)
            else:
                self.swap(board, self.coord, to)

        for c in (-1, -1), (-1, 1):
            to = self.new_coord(self.coord, c)
            if to.valide and board[to.y][to.x] != '-':
                if board[self.coord.y][self.coord.x].isupper() != board[to.y][to.x].isupper():
                    fig = board[to.y][to.x]
                    board[to.y][to.x] = '-'
                    self.swap(board, self.coord, to)
                    if not union_king.check_attack_to_king(board):
                        self.moves.append(to)
                        self.swap(board, self.coord, to)
                        board[to.y][to.x] = fig
                    else:
                        self.swap(board, self.coord, to)
                        board[to.y][to.x] = fig
            elif to.valide and to == self.object.move_in_two_cells:
                fig = board[to.y][to.x]
                board[to.y][to.x] = '-'
                self.swap(board, self.coord, to)
                if not union_king.check_attack_to_king(board):
                    self.moves.append(to)
                    self.swap(board, self.coord, to)
                    board[to.y][to.x] = fig
                else:
                    self.swap(board, self.coord, to)
                    board[to.y][to.x] = fig

    def generate_black_pawn_move(self, board):
        figures_d = self.object.white_figures_d if self.type_of_figure.isupper() else self.object.black_figures_d
        union_king = figures_d['K' if self.type_of_figure.isupper() else 'k']

        to = self.new_coord(self.coord, (1, 0))
        if to.valide and board[to.y][to.x] == '-':
            self.swap(board, self.coord, to)
            if not union_king.check_attack_to_king(board):
                self.moves.append(to)
                self.swap(board, self.coord, to)
            else:
                self.swap(board, self.coord, to)

        to = self.new_coord(self.coord, (-2, 0))
        if self.coord.y == 1 and to.valide and board[to.y][to.x] == '-' and board[to.y + 1][to.x] == '-':
            self.swap(board, self.coord, to)
            if not union_king.check_attack_to_king(board):
                self.moves.append(to)
                self.swap(board, self.coord, to)
            else:
                self.swap(board, self.coord, to)

        for c in (1, -1), (1, 1):
            to = self.new_coord(self.coord, c)
            if to.valide and board[to.y][to.x] != '-':
                if board[self.coord.y][self.coord.x].isupper() != board[to.y][to.x].isupper():
                    fig = board[to.y][to.x]
                    board[to.y][to.x] = '-'
                    self.swap(board, self.coord, to)
                    if not union_king.check_attack_to_king(board):
                        self.moves.append(to)
                        self.swap(board, self.coord, to)
                        board[to.y][to.x] = fig
                    else:
                        self.swap(board, self.coord, to)
                        board[to.y][to.x] = fig
            elif to.valide and to == self.object.move_in_two_cells:
                fig = board[to.y][to.x]
                board[to.y][to.x] = '-'
                self.swap(board, self.coord, to)
                if not union_king.check_attack_to_king(board):
                    self.moves.append(to)
                    self.swap(board, self.coord, to)
                    board[to.y][to.x] = fig
                else:
                    self.swap(board, self.coord, to)
                    board[to.y][to.x] = fig

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
        self.white_figures = []
        self.black_figures = []

        self.white_figures_d = {}
        self.black_figures_d = {}

        self.white_king_coord = Coord()
        self.black_king_coord = Coord()

        self.parse_fen(fen)

        self.generate_moves()

    def parse_fen(self, fen: str):
        data = fen.split(' ')
        board_fen = data[0].split('/')

        for i in range(len(board_fen)):
            j, k = 0, 0
            while j < len(self.board[i]):
                if not board_fen[i][k].isdigit():
                    if board_fen[i][k].isupper():
                        f = Figure(board_fen[i][k], Coord(i, j))
                        self.white_figures.append(f)
                        self.white_figures_d[board_fen[i][k]] = f
                        if board_fen[i][k] == 'K':
                            self.white_king_coord = Coord(i, k)
                    else:
                        f = Figure(board_fen[i][k], Coord(i, j))
                        self.black_figures.append(f)
                        self.black_figures_d[board_fen[i][k]] = f
                        if board_fen[i][k] == 'k':
                            self.black_king_coord = Coord(i, k)
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
            for figure in self.white_figures:
                figure.generate_move(self.board, self)
        elif self.order_of_move == 'b':
            for figure in self.black_figures:
                figure.generate_move(self.board, self)

    def show_moves(self):
        figures = self.white_figures if self.order_of_move == 'w' else self.black_figures
        for figure in figures:
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
        coord = Coord(7 - (int(coord_with_letters[1]) - 1), helper[coord_with_letters[0]])
        return coord


class Game:
    def __init__(self):
        pass
