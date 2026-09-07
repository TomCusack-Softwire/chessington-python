import os
from typing import Dict, List, Optional

from PIL import Image, ImageTk

from chessington.engine.data import Player
from chessington.engine.pieces import (Bishop, King, Knight, Pawn, Piece,
                                       Queen, Rook)
from chessington.ui.colours import Colour

IMAGES_BASE_DIRECTORY = 'images'


class ImageRepository:
    """
    Tkinter can't handle a non-rectangular overlay on a coloured background. This is
    troublesome when programming a chess board.

    This class works around the limitation by providing pre-processed piece images
    with all possible backgrounds.
    """

    PIECES_WITH_IMAGES: List[type[Piece]] = [Pawn, Knight, Bishop, King, Queen, Rook]

    def __init__(self):
        self._images = {}
        self._empty_images = {}
        self._load_from_disk()

    def _load_from_disk(self) -> None:
        """Load all possible images into memory to optimise performance"""

        def piece_on_all_backgrounds(piece: Optional[Piece]) -> Dict[Colour, Image.Image]:
            return {colour: self._get_image_with_background(piece, colour) for colour in Colour}

        for piece in self.PIECES_WITH_IMAGES:
            self._images[piece] = {
                Player.WHITE: piece_on_all_backgrounds(piece(Player.WHITE)),
                Player.BLACK: piece_on_all_backgrounds(piece(Player.BLACK)),
            }

        self._empty_images = piece_on_all_backgrounds(None)

    def _get_filename_for_piece(self, piece: Optional[Piece]) -> str:
        """Find the correct PNG file for a piece"""
        if piece is None:
            return os.path.join(IMAGES_BASE_DIRECTORY, 'blank.png')
        image_name = piece.__class__.__name__.lower() + piece.player._name_.lower()[0] + '.png'
        return os.path.join(IMAGES_BASE_DIRECTORY, image_name)

    def _get_image_for_piece(self, piece: Optional[Piece]) -> Image.Image:
        """Load a piece image from disk"""
        file = self._get_filename_for_piece(piece)
        return Image.open(file)

    def _get_image_with_background(self, piece: Optional[Piece], background_colour: Colour) -> Image.Image:
        """Load a piece image from disk and add background colour.

        You can't make tkinter elements transparent, and they are all rectangular.
        This function pre-processes piece PNGs to give appropriate background colours.
        """
        image = self._get_image_for_piece(piece)
        new_image = Image.new("RGBA", image.size, background_colour.value)

        try:
            # This will error on an empty image
            new_image.paste(image, (0, 0), image)
        except ValueError:
            pass

        return new_image

    def get_image(self, piece: Optional[Piece], background_colour: Colour) -> Image.Image:
        """Get a GUI-ready image of a piece on the specified background colour"""
        if piece:
            image = self._images[piece.__class__][piece.player][background_colour]
        else:
            image = self._empty_images[background_colour]
        return ImageTk.PhotoImage(image.convert('RGB'))
