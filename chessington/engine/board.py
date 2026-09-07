"""
A module providing a representation of a chess board. The rules of chess are not implemented - 
this is just a "dumb" board that will let you move pieces around as you like.
"""

from typing import TYPE_CHECKING, List, Optional

from chessington.engine.data import Player, Square
from chessington.engine.pieces import Bishop, King, Knight, Pawn, Queen, Rook, Piece

BoardType = List[List[Optional[Piece]]]
BOARD_SIZE = 8


class MissingPiece(Exception):
    pass

class Board:
    """
    A representation of the chess board, and the pieces on it.
    """

    def __init__(self, player: Player, board_state: BoardType):
        self.current_player = player
        self.board = board_state

    @staticmethod
    def empty() -> "Board":
        return Board(Player.WHITE, Board._create_empty_board())

    @staticmethod
    def at_starting_position() -> "Board":
        return Board(Player.WHITE, Board._create_starting_board())

    @staticmethod
    def _create_empty_board() -> BoardType:
        return [[None] * BOARD_SIZE for _ in range(BOARD_SIZE)]

    @staticmethod
    def _create_starting_board() -> BoardType:

        # Create an empty board
        board: BoardType = [[None] * BOARD_SIZE for _ in range(BOARD_SIZE)]

        # Setup the rows of pawns
        board[1] = [Pawn(Player.WHITE) for _ in range(BOARD_SIZE)]
        board[6] = [Pawn(Player.BLACK) for _ in range(BOARD_SIZE)]

        # Setup the rows of pieces
        piece_row: List[type[Piece]] = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        board[0] = list(map(lambda piece: piece(Player.WHITE), piece_row))
        board[7] = list(map(lambda piece: piece(Player.BLACK), piece_row))

        return board

    def set_piece(self, square: Square, piece: Optional[Piece]) -> None:
        """
        Places the piece at the given position on the board.
        """
        self.board[square.row][square.col] = piece

    def get_piece(self, square: Square) -> Optional[Piece]:
        """
        Retrieves the piece from the given square of the board.
        """
        return self.board[square.row][square.col]

    def find_piece(self, piece_to_find: Piece) -> Square:
        """
        Searches for the given piece on the board and returns its square.
        """
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                if self.board[row][col] is piece_to_find:
                    return Square.at(row, col)
        raise MissingPiece('The supplied piece is not on the board')

    def move_piece(self, from_square: Square, to_square: Square) -> None:
        """
        Moves the piece from the given starting square to the given destination square.
        """
        moving_piece = self.get_piece(from_square)
        if moving_piece is not None and moving_piece.player == self.current_player:
            self.set_piece(to_square, moving_piece)
            self.set_piece(from_square, None)
            self.current_player = self.current_player.opponent()
