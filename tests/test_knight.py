from chessington.engine.board import Board
from chessington.engine.data import Player, Square
from chessington.engine.pieces import Knight, Pawn


def test_knight_can_move_in_l_shape():
    # Arrange
    board = Board.empty()
    knight = Knight(Player.WHITE)
    square = Square.at(3, 5)
    board.set_piece(square, knight)

    # Act
    moves = knight.get_available_moves(board)

    # Assert
    expected_moves = [
        Square.at(4, 7),
        Square.at(4, 3),
        Square.at(5, 6),
        Square.at(5, 4),
        Square.at(2, 7),
        Square.at(2, 3),
        Square.at(1, 6),
        Square.at(1, 4),
    ]
    assert len(moves) == len(expected_moves)
    assert set(moves) == set(expected_moves)


def test_knight_can_jump_over_pieces():
    # Arrange
    board = Board.empty()
    knight = Knight(Player.WHITE)
    square = Square.at(3, 5)
    board.set_piece(square, knight)

    # Put piece surrounding the knight
    for row_delta in range(-1, 1):
        for col_delta in range(-1, 1):
            if row_delta != 0 or col_delta != 0:
                board.set_piece(
                    Square.at(square.row + row_delta, square.col + col_delta),
                    Pawn(Player.WHITE),
                )

    # Act
    moves = knight.get_available_moves(board)

    # Assert
    expected_moves = [
        Square.at(4, 7),
        Square.at(4, 3),
        Square.at(5, 6),
        Square.at(5, 4),
        Square.at(2, 7),
        Square.at(2, 3),
        Square.at(1, 6),
        Square.at(1, 4),
    ]
    assert len(moves) == len(expected_moves)
    assert set(moves) == set(expected_moves)
