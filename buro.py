from constant import BuroConstant
from tile import Tile


class Buro:
    def __init__(self, tile):
        self._tile = tile


class Chi(Buro):
    # type : 0 -> a-2, a-1, a
    #        1 -> a-1, a, a+1
    #        2 -> a, a+1, a+2
    def __init__(self, tile, type):
        super().__init__(tile)
        self._type = type

    def __str__(self):
        raise NotImplementedError()


class Pon(Buro):

    # where : 0 -> 상가
    #         1 -> 대가
    #         2 -> 하가

    def __init__(self, tile, where):
        super().__init__(tile)
        self._where = where

    def __str__(self):
        return " ".join([BuroConstant.WHERE_LIST[self._where], str(self._tile), BuroConstant.BURO_STRINGS[1]])


class BigMeldedKan(Buro):
    def __init__(self, tile, where):
        super().__init__(tile)
        self._where = where

    def __str__(self):
        return " ".join([BuroConstant.WHERE_LIST[self._where], str(self._tile), BuroConstant.BURO_STRINGS[2]])


class SmallMeldedKan(Buro):
    def __init__(self, tile, where):
        super().__init__(tile)
        self._where = where

    def __str__(self):
        return " ".join([BuroConstant.WHERE_LIST[self._where], str(self._tile), BuroConstant.BURO_STRINGS[3]])


class ConcealedKan(Buro):
    def __init__(self, tile):
        super().__init__(tile)

    def __str__(self):
        return " ".join([BuroConstant.WHERE_LIST[self._where], str(self._tile), BuroConstant.BURO_STRINGS[4]])


class BuroFactory:
    @staticmethod
    def make_buro_from_buro_code(buro_code):
        buro_prefix = buro_code[:2]
        buro_tile_code = buro_code[2:4]
        buro_etc_param = buro_code[4:]
        buro_tile = Tile(Tile.calc_tile_num(buro_tile_code))

        if buro_prefix == BuroConstant.BURO_CODES[0]:
            return Chi(buro_tile, int(buro_etc_param))

        elif buro_prefix == BuroConstant.BURO_CODES[1]:
            return Pon(buro_tile, int(buro_etc_param))

        elif buro_prefix == BuroConstant.BURO_CODES[2]:
            return BigMeldedKan(buro_tile, int(buro_etc_param))

        elif buro_prefix == BuroConstant.BURO_CODES[3]:
            return SmallMeldedKan(buro_tile, int(buro_etc_param))

        elif buro_prefix == BuroConstant.BURO_CODES[4]:
            assert len(buro_etc_param) == 0
            return ConcealedKan(buro_tile)
        else:
            raise ValueError()



