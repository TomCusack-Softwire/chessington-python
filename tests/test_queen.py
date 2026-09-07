from chessington.engine.board import Board
from chessington.engine.data import Player, Square
from chessington.engine.pieces import Pawn, Queen


def test_queen_can_move_diagonally_and_laterally():
    # Arrange
    board = Board.empty()
    queen = Queen(Player.WHITE)
    square = Square.at(4, 4)
    board.set_piece(square, queen)

    # Act
    moves = queen.get_available_moves(board)

    # Assert
    expected_moves = [
        Square.at(0, 0),
        Square.at(1, 1),
        Square.at(2, 2),
        Square.at(3, 3),
        Square.at(5, 5),
        Square.at(6, 6),
        Square.at(7, 7),
        Square.at(1, 7),
        Square.at(2, 6),
        Square.at(3, 5),
        Square.at(5, 3),
        Square.at(6, 2),
        Square.at(7, 1),
        Square.at(0, 4),
        Square.at(1, 4),
        Square.at(2, 4),
        Square.at(3, 4),
        Square.at(5, 4),
        Square.at(6, 4),
        Square.at(7, 4),
        Square.at(4, 0),
        Square.at(4, 1),
        Square.at(4, 2),
        Square.at(4, 3),
        Square.at(4, 5),
        Square.at(4, 6),
        Square.at(4, 7),
    ]
    assert len(moves) == len(expected_moves)
    assert set(moves) == set(expected_moves)


def test_queen_is_blocked_by_enemy_pieces():
    # Arrange
    board = Board.empty()
    queen = Queen(Player.WHITE)
    square = Square.at(4, 4)
    board.set_piece(square, queen)

    enemy = Pawn(Player.BLACK)
    enemy_square = Square.at(6, 6)
    board.set_piece(enemy_square, enemy)

    # Act
    moves = queen.get_available_moves(board)

    # Assert
    assert Square.at(7, 7) not in moves


def test_queen_is_blocked_by_friendly_pieces():
    # Arrange
    board = Board.empty()
    queen = Queen(Player.WHITE)
    square = Square.at(4, 4)
    board.set_piece(square, queen)

    friendly = Pawn(Player.WHITE)
    friendly_square = Square.at(6, 6)
    board.set_piece(friendly_square, friendly)

    # Act
    moves = queen.get_available_moves(board)

    # Assert
    assert Square.at(7, 7) not in moves
