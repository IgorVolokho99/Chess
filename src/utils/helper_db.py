from sqlalchemy.orm import sessionmaker, scoped_session

from src.db import Test, engine
from src.core.main import Chess


# Simple position
type_of_position = 'Simple position'
fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"

game = Chess(fen=fen)
game.show_board()
game.show_moves()

result_pos = game.get_board()
result_moves = game.get_moves()

answer = input()
if answer.lower() == "y":
    test = Test(type_of_position=type_of_position, fen=fen, result_pos=result_pos, result_moves=result_moves)
    session_factory = sessionmaker(engine)
    session = scoped_session(session_factory)

    session.add(test)

    session.commit()
    session.close()
else:
    print("I won't save information about this test.")