from constant import TileConstant
from tile import Tile
from player_hand import PlayerHand

class HandCompleteChecker:
    def __init__(self, four_tile_chitoi=False):
        self._four_tile_chitoi = four_tile_chitoi

    def check_tenpai(self, hand):
        return len(self.calculate_waiting(hand)) != 0

    def calculate_waiting(self, hand):
        return [Tile(tile_num) for tile_num in TileConstant.TILE_NUMS if self.check_waiting(hand, Tile(tile_num))]

    def check_waiting(self, hand, tile):
        if hand.count_tile(tile) == 4: return False
        return self.check_normal_waiting(hand, tile) or \
            self.check_chitoi_waiting(hand, tile) or \
            self.check_koukusi_waiting(hand, tile)

    def check_normal_waiting(self, hand, tile):
        return False

    def check_chitoi_waiting(self, hand, tile):
        assert isinstance(hand, PlayerHand) and isinstance(tile, Tile)

        if not hand.check_mensen(): return False
        for tile_num in TileConstant.TILE_NUMS:
            iter_tile = Tile(tile_num)
            tile_num = hand.count_tile(iter_tile) + (1 if tile.num == iter_tile.num else 0)
            if tile_num % 2 == 1:
                return False
            elif not self._four_tile_chitoi and tile_num > 2:
                return False
        return True

    def check_koukusi_waiting(self, hand, tile):
        assert isinstance(hand, PlayerHand) and isinstance(tile, Tile)
        if not hand.check_mensen(): return False

        pair_count = False
        for tile_num in TileConstant.HONORS + TileConstant.TERMINALS:
            iter_tile = Tile(tile_num)
            tile_num = hand.count_tile(iter_tile) + (1 if tile.num == iter_tile.num else 0)
            if tile_num == 0 or tile_num > 2:
                return False
            elif pair_count and tile_num == 2:
                return False
            elif tile_num == 2:
                pair_count = True
        return pair_count
