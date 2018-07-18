from invisible_hand import InvisibleHand
from visible_hand import VisibleHand
from constant import TileConstant
from tile import Tile
from buro import BuroFactory


class HandCodeParser:
    @staticmethod
    def parse(hand_code):
        index = 0
        invisible_hand = InvisibleHand()
        visible_hand = VisibleHand()

        hand_code_split = hand_code.split(':')

        while index < len(hand_code_split[0]):
            tile_num = Tile.calc_tile_num(hand_code_split[0][index:index + 2])
            assert tile_num in TileConstant.TILE_NUMS
            invisible_hand.append(Tile(tile_num))
            index = index + 2

        for buro_code in hand_code_split[1:]:
            visible_hand.append(BuroFactory.make_buro_from_buro_code(buro_code))

        return invisible_hand, visible_hand
