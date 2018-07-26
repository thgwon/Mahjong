from hand_code_parser import HandCodeParser
from tile import Tile
from constant import TileConstant


class PlayerHand:
    def __init__(self, hand_code):
        self._hand_code = hand_code
        self._invisible_hand, self._visible_hand = HandCodeParser.parse(hand_code)
        self._validate_player_hand()

    def _validate_player_hand(self):
        for t in TileConstant.TILE_NUMS:
            assert self.count_tile(Tile(t)) <= 4
        assert self._visible_hand.buro_cnt * 3 + self._invisible_hand.tile_cnt == 13

    def __str__(self):
        return "손패 : " + str(self._invisible_hand) + "\n" + "부로 : " + str(self._visible_hand)

    def count_tile(self, tile):
        return self._invisible_hand.count_tile(tile) + self._visible_hand.count_tile(tile)

    def count_invisible_tile(self, tile):
        return self._invisible_hand.count_tile(tile)

    def check_mensen(self):
        return self._visible_hand.check_mensen()
