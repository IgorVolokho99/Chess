import pytest
from sqlalchemy.orm import sessionmaker, scoped_session

from db.models import engine, Test
from main import Chess


def test_positions():
    session_factory = sessionmaker(engine)
    session = scoped_session(session_factory)

    result = session.query(Test).all()

    for item in result:
        testing_object = Chess(fen=item.fen)
        assert testing_object.get_board() == item.result_pos, f"Error in {item.type_of_position} with id - {item.id} (Board)"
        assert testing_object.get_moves() == item.result_moves, f"Error in {item.type_of_position} with id - {item.id} (Moves)"
    session.close()
    engine.dispose()

