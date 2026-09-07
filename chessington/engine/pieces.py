from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, List

from chessington.engine.data import Player, Square

if TYPE_CHECKING:
    from chessington.engine.board import Board

class Piece(ABC):
    """
    An abstract base class from which all pieces inherit.
    """

    def __init__(self, player: Player):
        self.player = player

    @abstractmethod
    def get_available_moves(self, board: Board) -> List[Square]:
        """
        Get all squares that the piece is allowed to move to.
        """
        pass

    def move_to(self, board: Board, new_square: Square) -> None:
        """
        Move this piece to the given square on the board.
        """
        current_square = board.find_piece(self)
        board.move_piece(current_square, new_square)


class Pawn(Piece):
    """
    A class representing a chess pawn.
    """
    def get_available_moves(self, board: Board) -> List[Square]:
        return []


class Knight(Piece):
    """
    A class representing a chess knight.
    """

    def get_available_moves(self, board: Board) -> List[Square]:
        return []


class Bishop(Piece):
    """
    A class representing a chess bishop.
    """

    def get_available_moves(self, board: Board) -> List[Square]:
        return []


class Rook(Piece):
    """
    A class representing a chess rook.
    """

    def get_available_moves(self, board: Board) -> List[Square]:
        return []


class Queen(Piece):
    """
    A class representing a chess queen.
    """

    def get_available_moves(self, board: Board) -> List[Square]:
        return []


class King(Piece):
    """
    A class representing a chess king.
    """

    def get_available_moves(self, board: Board) -> List[Square]:
        return []
