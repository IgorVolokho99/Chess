import copy
from abc import ABC, abstractmethod

from src.core.chess_engine import ChessEngine
from src.core.coord import Coord
from src.core.constants import MOVES_OF_KNIGHT, MOVES_OF_BISHOP, MOVES_OF_ROOK


class Figure(ABC):
    def __init__(self, type_of_figure: str, coord: Coord, board: ChessEngine):
        self.type_of_figure = type_of_figure
        self.coord = coord
        self.moves = []
        self.board = board

    @abstractmethod
    def generate_move(self):
        pass

    @abstractmethod
    def check_attack_to_king(self) -> bool:
        pass

    @staticmethod
    def swap(board, fr, to):
        board[fr.y][fr.x], board[to.y][to.x] = board[to.y][to.x], board[fr.y][fr.x]
        return board

    @staticmethod
    def new_coord(coord, to):
        return Coord(coord.y + to[0], coord.x + to[1])


class King(Figure):
    def __init__(self, type_of_figure: str, coord: Coord, board: ChessEngine):
        super().__init__(type_of_figure, coord, board)

    def generate_move(self):
        board = self.board.board

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


def check_attack_to_king(self) -> bool:
        pass
