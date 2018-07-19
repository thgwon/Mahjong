from constant import TileConstant
from tile import Tile
from player_hand import PlayerHand
from collections import OrderedDict


class HandCompleteChecker:
    def __init__(self, four_tile_chitoi=False):
        self._four_tile_chitoi = four_tile_chitoi

    def check_tenpai(self, hand):
        return len(self.calculate_waiting(hand)) != 0

    def calculate_waiting(self, hand):
        return [Tile(tile_num) for tile_num in TileConstant.TILE_NUMS if self.check_waiting(hand, Tile(tile_num))]

    def check_waiting(self, hand, tile):
        if hand.count_tile(tile.num) == 4: return False
        return self.check_normal_waiting(hand, tile) or \
            self.check_chitoi_waiting(hand, tile) or \
            self.check_koukusi_waiting(hand, tile)

    def check_normal_waiting(self, hand, tile):
        tile_count_od = OrderedDict()
        for tile_num in TileConstant.TILE_NUMS:
            tile_count_od[tile_num] = hand.count_tile(tile_num) + (1 if tile.num == tile_num else 0)

        return self._check_normal_waiting_from_od(tile_count_od, False)

    def _check_normal_waiting_from_od(self, tile_count_od, head_erase):
        if sum(tile_count_od.values())==0:
            return True
        smallest_tile_num = self._find_first_nonzero_tile_num(tile_count_od)
        return self._check_straight_use(tile_count_od, smallest_tile_num, head_erase) or\
               self._check_head_use(tile_count_od, smallest_tile_num, head_erase) or\
               self._check_triplet_use(tile_count_od, smallest_tile_num, head_erase)

    def _find_first_nonzero_tile_num(self, tile_count_od):
        for k,v in tile_count_od.items():
            if v != 0:
                return k

    def _check_straight_use(self, tile_count_od, tile_num, head_erase):
        if not tile_count_od.get(tile_num + 1) or not tile_count_od.get(tile_num + 2):
            return False
        if tile_count_od[tile_num] < 1 or tile_count_od[tile_num + 1] < 1 or tile_count_od[tile_num + 2] < 1:
            return False

        new_tile_count_od = tile_count_od.copy()
        new_tile_count_od[tile_num] -= 1
        new_tile_count_od[tile_num + 1] -= 1
        new_tile_count_od[tile_num + 2] -= 1
        return self._check_normal_waiting_from_od(new_tile_count_od, head_erase)

    def _check_head_use(self, tile_count_od, tile_num, head_erase):
        if tile_count_od[tile_num] < 2 or head_erase:
            return False

        new_tile_count_od = tile_count_od.copy()
        new_tile_count_od[tile_num] -= 2
        return self._check_normal_waiting_from_od(new_tile_count_od, True)

    def _check_triplet_use(self, tile_count_od, tile_num, head_erase):
        if tile_count_od[tile_num] < 3:
            return False

        new_tile_count_od = tile_count_od.copy()
        new_tile_count_od[tile_num] -= 3
        return self._check_normal_waiting_from_od(new_tile_count_od, head_erase)

    def check_chitoi_waiting(self, hand, tile):
        assert isinstance(hand, PlayerHand) and isinstance(tile, Tile)

        if not hand.check_mensen(): return False
        for tile_num in TileConstant.TILE_NUMS:
            tile_num = hand.count_tile(tile_num) + (1 if tile.num == tile_num else 0)
            if tile_num % 2 == 1:
                return False
            elif not self._four_tile_chitoi and tile_num > 2:
                return False
        return True

    def check_koukusi_waiting(self, hand, tile):
        assert isinstance(hand, PlayerHand) and isinstance(tile, Tile)
        if not hand.check_mensen(): return False

        exist_pair = False
        for tile_num in TileConstant.HONORS + TileConstant.TERMINALS:
            tile_count = hand.count_tile(tile_num) + (1 if tile.num == tile_num else 0)
            if tile_count == 0 or tile_count > 2:
                return False
            elif exist_pair and tile_count == 2:
                return False
            elif tile_count == 2:
                exist_pair = True
        return exist_pair
