from constant import BuroConstant
from tile import Tile


class Buro:
    def __init__(self, tile):
        self._tile = tile

    def count_tile(self, tile):
        raise NotImplementedError()

class Chi(Buro):
    def __init__(self, tile, tile1, tile2):
        super().__init__(tile)
        self._tile1 = tile1
        self._tile2 = tile2
        self._validate_chi()

    def _validate_chi(self):
        tile_nums = [self._tile.num, self._tile1.num, self._tile2.num]
        tile_nums.sort()
        assert tile_nums[0] + 1 == tile_nums[1] and tile_nums[1] + 1 == tile_nums[2]

    def __str__(self):
        return " ".join([str(self._tile), str(self._tile1), str(self._tile2), BuroConstant.BURO_STRINGS[BuroConstant.CHI_CODE]])

    def count_tile(self, tile):
        return sum (1 for t in [self._tile1, self._tile2, self._tile] if tile.num == t.num)

class Pon(Buro):
    # where : 0 -> 상가
    #         1 -> 대가
    #         2 -> 하가

    def __init__(self, tile, where):
        super().__init__(tile)
        self._where = where

    def __str__(self):
        return " ".join([BuroConstant.WHERE_LIST[self._where], str(self._tile),
                         BuroConstant.BURO_STRINGS[BuroConstant.PON_CODE]])

    def count_tile(self, tile):
        return 3 * (1 if self._tile.num == tile.num else 0)

class BigMeldedKan(Buro):
    def __init__(self, tile, where):
        super().__init__(tile)
        self._where = where

    def __str__(self):
        return " ".join([BuroConstant.WHERE_LIST[self._where], str(self._tile),
                         BuroConstant.BURO_STRINGS[BuroConstant.BIG_MELDED_KAN_CODE]])

    def count_tile(self, tile):
        return 4 * (1 if self._tile.num == tile.num else 0)


class SmallMeldedKan(Buro):
    def __init__(self, tile, where):
        super().__init__(tile)
        self._where = where

    def __str__(self):
        return " ".join([BuroConstant.WHERE_LIST[self._where], str(self._tile),
                         BuroConstant.BURO_STRINGS[BuroConstant.SMALL_MELDED_KAN_CODE]])

    def count_tile(self, tile):
        return 4 * (1 if self._tile.num == tile.num else 0)


class ConcealedKan(Buro):
    def __init__(self, tile):
        super().__init__(tile)

    def __str__(self):
        return " ".join([str(self._tile), BuroConstant.BURO_STRINGS[BuroConstant.CONCEALED_KAN_CODE]])

    def count_tile(self, tile):
        return 4 * (1 if self._tile.num == tile.num else 0)


class BuroFactory:
    @staticmethod
    def make_buro_from_buro_code(buro_code):
        buro_prefix = buro_code[:2]
        buro_tile_code = buro_code[2:4]
        buro_etc_param = buro_code[4:]
        buro_tile = Tile(Tile.calc_tile_num(buro_tile_code))

        if buro_prefix == BuroConstant.CHI_CODE:
            buro_tile1 = Tile(Tile.calc_tile_num(buro_etc_param[:2]))
            buro_tile2 = Tile(Tile.calc_tile_num(buro_etc_param[2:]))
            return Chi(buro_tile, buro_tile1, buro_tile2)

        elif buro_prefix == BuroConstant.PON_CODE:
            return Pon(buro_tile, int(buro_etc_param))

        elif buro_prefix == BuroConstant.BIG_MELDED_KAN_CODE:
            return BigMeldedKan(buro_tile, int(buro_etc_param))

        elif buro_prefix == BuroConstant.SMALL_MELDED_KAN_CODE:
            return SmallMeldedKan(buro_tile, int(buro_etc_param))

        elif buro_prefix == BuroConstant.CONCEALED_KAN_CODE:
            assert len(buro_etc_param) == 0
            return ConcealedKan(buro_tile)
        else:
            raise ValueError()



