from chessington.engine.board import Board
from chessington.engine.data import Player, Square
from chessington.engine.pieces import Bishop, Pawn


def test_bishop_can_move_diagonally():
    # Arrange
    board = Board.empty()
    bishop = Bishop(Player.WHITE)
    square = Square.at(3, 5)
    board.set_piece(square, bishop)

    # Act
    moves = bishop.get_available_moves(board)

    # Assert
    expected_moves = [
        Square.at(0, 2),
        Square.at(1, 3),
        Square.at(2, 4),
        Square.at(4, 6),
        Square.at(5, 7),
        Square.at(1, 7),
        Square.at(2, 6),
        Square.at(4, 4),
        Square.at(5, 3),
        Square.at(6, 2),
        Square.at(7, 1),
    ]
    assert len(moves) == len(expected_moves)
    assert set(moves) == set(expected_moves)


def test_bishop_can_capture_enemy_pieces():
    # Arrange
    board = Board.empty()
    bishop = Bishop(Player.WHITE)
    square = Square.at(3, 5)
    board.set_piece(square, bishop)

    enemy = Pawn(Player.BLACK)
    enemy_square = Square.at(5, 3)
    board.set_piece(enemy_square, enemy)

    # Act
    moves = bishop.get_available_moves(board)

    # Assert
    assert enemy_square in moves


def test_bishop_is_blocked_by_enemy_pieces():
    # Arrange
    board = Board.empty()
    bishop = Bishop(Player.WHITE)
    square = Square.at(3, 5)
    board.set_piece(square, bishop)

    enemy = Pawn(Player.BLACK)
    enemy_square = Square.at(5, 3)
    board.set_piece(enemy_square, enemy)

    # Act
    moves = bishop.get_available_moves(board)

    # Assert
    assert Square.at(6, 2) not in moves


def test_bishop_cannot_capture_friendly_pieces():
    # Arrange
    board = Board.empty()
    bishop = Bishop(Player.WHITE)
    square = Square.at(3, 5)
    board.set_piece(square, bishop)

    friendly = Pawn(Player.WHITE)
    friendly_square = Square.at(5, 3)
    board.set_piece(friendly_square, friendly)

    # Act
    moves = bishop.get_available_moves(board)

    # Assert
    assert friendly_square not in moves


def test_bishop_is_blocked_by_friendly_pieces():
    # Arrange
    board = Board.empty()
    bishop = Bishop(Player.WHITE)
    square = Square.at(3, 5)
    board.set_piece(square, bishop)

    friendly = Pawn(Player.WHITE)
    friendly_square = Square.at(5, 3)
    board.set_piece(friendly_square, friendly)

    # Act
    moves = bishop.get_available_moves(board)

    # Assert
    assert Square.at(6, 2) not in moves
