import copy

from src.core.coord import Coord
from src.core.constants import MOVES_OF_KNIGHT, MOVES_OF_BISHOP, MOVES_OF_ROOK


class Figure:
    def __init__(self, type_of_figure: str, coord: Coord, object_of_board):
        self.type_of_figure = type_of_figure
        self.coord = coord
        self.moves = []
        self.object = object_of_board

    def generate_move(self, board):
        # self.object = object_of_board
        if self.type_of_figure.upper() == 'K':
            self.generate_king_move(board)
            self.make_castling(copy.deepcopy(board))
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

    def make_castling(self, board):
        if self.type_of_figure.isupper():
            if self.object.castling['K']:
                if board[self.coord.y][self.coord.x + 1] != '-' or board[self.coord.y][self.coord.x + 2] != '-':
                    return
                counter = 0
                self.coord = Coord(self.coord.y, self.coord.x + 1)
                board = self.swap(board, self.coord, Coord(self.coord.y, self.coord.x - 1))
                if self.check_attack_to_king(board):
                    counter += 1
                board = self.swap(board, self.coord, Coord(self.coord.y, self.coord.x - 1))
                self.coord = Coord(self.coord.y, self.coord.x + 1)

                board = self.swap(board, self.coord, Coord(self.coord.y, self.coord.x - 2))
                if self.check_attack_to_king(board):
                    counter += 1
                board = self.swap(board, self.coord, Coord(self.coord.y, self.coord.x - 2))

                if counter == 0:
                    self.moves.append(Coord(self.coord.y, self.coord.x))
                self.coord = Coord(self.coord.y, self.coord.x - 2)
            if self.object.castling['Q']:
                if board[self.coord.y][self.coord.x - 1] != '-' or board[self.coord.y][self.coord.x - 2] != '-':
                    return
                counter = 0
                self.coord = Coord(self.coord.y, self.coord.x - 1)
                board = self.swap(board, self.coord, Coord(self.coord.y, self.coord.x + 1))
                if self.check_attack_to_king(board):
                    counter += 1
                board = self.swap(board, self.coord, Coord(self.coord.y, self.coord.x + 1))
                self.coord = Coord(self.coord.y, self.coord.x - 1)

                board = self.swap(board, self.coord, Coord(self.coord.y, self.coord.x + 2))
                if self.check_attack_to_king(board):
                    counter += 1
                board = self.swap(board, self.coord, Coord(self.coord.y, self.coord.x + 2))

                if counter == 0:
                    self.moves.append(Coord(self.coord.y, self.coord.x))
                self.coord = Coord(self.coord.y, self.coord.x + 2)
        else:
            if self.object.castling['k']:
                if board[self.coord.y][self.coord.x + 1] != '-' or board[self.coord.y][self.coord.x + 2] != '-':
                    return
                counter = 0
                self.coord = Coord(self.coord.y, self.coord.x + 1)
                board = self.swap(board, self.coord, Coord(self.coord.y, self.coord.x - 1))
                if self.check_attack_to_king(board):
                    counter += 1
                board = self.swap(board, self.coord, Coord(self.coord.y, self.coord.x - 1))
                self.coord = Coord(self.coord.y, self.coord.x + 1)

                board = self.swap(board, self.coord, Coord(self.coord.y, self.coord.x - 2))
                if self.check_attack_to_king(board):
                    counter += 1
                board = self.swap(board, self.coord, Coord(self.coord.y, self.coord.x - 2))

                if counter == 0:
                    self.moves.append(Coord(self.coord.y, self.coord.x))
                self.coord = Coord(self.coord.y, self.coord.x - 2)
            if self.object.castling['q']:
                if board[self.coord.y][self.coord.x - 1] != '-' or board[self.coord.y][self.coord.x - 2] != '-':
                    return
                counter = 0
                self.coord = Coord(self.coord.y, self.coord.x - 1)
                board = self.swap(board, self.coord, Coord(self.coord.y, self.coord.x + 1))
                if self.check_attack_to_king(board):
                    counter += 1
                board = self.swap(board, self.coord, Coord(self.coord.y, self.coord.x + 1))
                self.coord = Coord(self.coord.y, self.coord.x - 1)

                board = self.swap(board, self.coord, Coord(self.coord.y, self.coord.x + 2))
                if self.check_attack_to_king(board):
                    counter += 1
                board = self.swap(board, self.coord, Coord(self.coord.y, self.coord.x + 2))

                if counter == 0:
                    self.moves.append(Coord(self.coord.y, self.coord.x))
                self.coord = Coord(self.coord.y, self.coord.x + 2)

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

        to = self.new_coord(self.coord, (2, 0))
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
