from tile import Tile
from buro import Buro
from constant import TileConstant


class PlayerHand:
    def __init__(self, hand_code):
        self._hand_code = hand_code
        self._invisible_hand, self._visible_hand = HandCodeParser.parse(hand_code)


class InvisibleHand:
    def __init__(self):
        self._tiles = []

    @property
    def tile_num(self):
        return len(self._tiles)

    def append(self, tile):
        assert isinstance(tile, Tile)
        self._tiles.append(tile)


class VisibleHand:
    def __init__(self):
        self._buros = []

    @property
    def buro_num(self):
        return len(self._buros)

    def append(self, buro):
        assert isinstance(buro, Buro)
        self._buros.append(buro)


class HandCodeParser:
    @staticmethod
    def parse(hand_code):
        index = 0
        invisible_hand = InvisibleHand()
        visible_hand = VisibleHand()

        while hand_code[index]!=':' or index < len(hand_code):
            tile_num = HandCodeParser._calc_tile_num(hand_code[index:index+2])
            assert tile_num in TileConstant.TILE_NUMS
            invisible_hand.append(Tile(tile_num))
            index = index + 2

        index = index+1
        while index < len(hand_code):
            raise NotImplemented

        return invisible_hand, visible_hand

    @staticmethod
    def _calc_tile_num(tile_code):
        return TileConstant.TILE_CODE_DICT[tile_code]