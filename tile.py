from constant import TileConstant


class Tile:
    def __init__(self, num, dora_value=0):
        if num not in TileConstant.TILE_NUMS:
            raise NotImplemented

        self._num = num
        self._basic_dora_value=dora_value
        self._temp_dora_value=0

    @property
    def num(self):
        return self._num

    @property
    def dora_value(self):
        return self._basic_dora_value + self._temp_dora_value

    @property
    def type(self):
        return TileConstant.TYPES[int(self._num / 10)]

    @staticmethod
    def calc_tile_num(tile_code):
        return TileConstant.TILE_CODE_DICT[tile_code]


    def __str__(self) -> str:
        return TileConstant.TILE_STR_DICT[self._num]

    def __lt__(self, other):
        return self.num < other.num