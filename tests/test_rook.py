from chessington.engine.board import Board
from chessington.engine.data import Player, Square
from chessington.engine.pieces import Pawn, Rook


def test_rook_can_move_laterally():
    # Arrange
    board = Board.empty()
    rook = Rook(Player.WHITE)
    square = Square.at(2, 5)
    board.set_piece(square, rook)

    # Act
    moves = rook.get_available_moves(board)

    # Assert
    expected_moves = [
        Square.at(2, 0),
        Square.at(2, 1),
        Square.at(2, 2),
        Square.at(2, 3),
        Square.at(2, 4),
        Square.at(2, 6),
        Square.at(2, 7),
        Square.at(0, 5),
        Square.at(1, 5),
        Square.at(3, 5),
        Square.at(4, 5),
        Square.at(5, 5),
        Square.at(6, 5),
        Square.at(7, 5),
    ]
    assert len(moves) == len(expected_moves)
    assert set(moves) == set(expected_moves)
