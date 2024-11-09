from src.core.coord import Coord
from src.core.figure import Figure


class ChessEngine:
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
                        f = Figure(board_fen[i][k], Coord(i, j), self)
                        self.white_figures.append(f)
                        self.white_figures_d[board_fen[i][k]] = f
                        if board_fen[i][k] == 'K':
                            self.white_king_coord = Coord(i, k)
                    else:
                        f = Figure(board_fen[i][k], Coord(i, j), self)
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

    def get_board(self) -> str:
        result = ''
        for i in range(len(self.board)):
            result += ''.join(self.board[i])
        return result

    def generate_moves(self):
        if self.order_of_move == 'w':
            for figure in self.white_figures:
                figure.generate_move(self.board)
        elif self.order_of_move == 'b':
            for figure in self.black_figures:
                figure.generate_move(self.board)

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
                print('---------------')

    def get_moves(self) -> str:
        figures = self.white_figures if self.order_of_move == 'w' else self.black_figures
        result = ''
        for figure in figures:
            if len(figure.moves) > 0:
                for i in range(len(self.board)):
                    for j in range(len(self.board[i])):
                        if Coord(i, j) == figure.coord:
                            # print(figure.type_of_figure, end=' ')
                            result += figure.type_of_figure
                        elif Coord(i, j) in figure.moves:
                            # print('*', end=' ')
                            result += '*'
                        else:
                            # print('-', end=' ')
                            result += '-'
                    # print()
                # print('---------------')
        return result

    @staticmethod
    def from_letters_to_coord(coord_with_letters: str) -> Coord:
        if coord_with_letters == '-':
            return Coord(-1, -1)
        helper = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
        coord = Coord(7 - (int(coord_with_letters[1]) - 1), helper[coord_with_letters[0]])
        return coord


if __name__ == "__main__":
    c = ChessEngine('3r4/7k/8/8/3Q4/3KR2q/8/8 w - - 0 1')
    c.show_board()
    c.show_moves()