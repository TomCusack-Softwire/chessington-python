from chessington.engine.board import Board
from chessington.engine.data import Player, Square
from chessington.engine.pieces import King, Pawn


def test_king_can_move_one_square_in_any_direction():
    # Arrange
    board = Board.empty()
    king = King(Player.WHITE)
    square = Square.at(5, 2)
    board.set_piece(square, king)

    # Act
    moves = king.get_available_moves(board)

    # Assert
    expected_moves = [
        Square.at(4, 1),
        Square.at(4, 2),
        Square.at(4, 3),
        Square.at(5, 1),
        Square.at(5, 3),
        Square.at(6, 1),
        Square.at(6, 2),
        Square.at(6, 3),
    ]
    assert len(moves) == len(expected_moves)
    assert set(moves) == set(expected_moves)


def test_king_cannot_move_off_the_board():
    # Arrange
    board = Board.empty()
    king = King(Player.WHITE)
    square = Square.at(7, 7)
    board.set_piece(square, king)

    # Act
    moves = king.get_available_moves(board)

    # Assert
    expected_moves = [Square.at(7, 6), Square.at(6, 6), Square.at(6, 7)]
    assert len(moves) == len(expected_moves)
    assert set(moves) == set(expected_moves)


def test_king_can_capture_enemy_pieces():
    # Arrange
    board = Board.empty()
    king = King(Player.WHITE)
    square = Square.at(5, 2)
    board.set_piece(square, king)

    enemy = Pawn(Player.BLACK)
    enemy_square = Square.at(5, 1)
    board.set_piece(enemy_square, enemy)

    # Act
    moves = king.get_available_moves(board)

    # Assert
    assert enemy_square in moves


def test_king_cannot_capture_friendly_pieces():
    # Arrange
    board = Board.empty()
    king = King(Player.WHITE)
    square = Square.at(5, 2)
    board.set_piece(square, king)

    friendly = Pawn(Player.WHITE)
    friendly_square = Square.at(5, 1)
    board.set_piece(friendly_square, friendly)

    # Act
    moves = king.get_available_moves(board)

    # Assert
    assert friendly_square not in moves
