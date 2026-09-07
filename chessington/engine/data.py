"""
Data classes for easy representation of concepts such as a square on the board or a player.
"""

from dataclasses import dataclass
from enum import Enum, auto


class Player(Enum):
    """
    The two players in a game of chess.
    """

    WHITE = auto()
    BLACK = auto()

    def opponent(self) -> "Player":
        return Player.BLACK if self == Player.WHITE else Player.WHITE


@dataclass(frozen=True)
class Square:
    row: int
    col: int

    @classmethod
    def at(cls, row: int, col: int) -> "Square":
        """
        Provides backward compatibility with previous namedtuple implementation.

        Square.at(...) is equivalent to Square(...).
        """

        return cls(row=row, col=col)
