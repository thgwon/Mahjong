from constant import TileConstant

class Tile:
    # m :  1 ~  9
    # p : 11 ~ 19
    # s : 21 ~ 29
    # w : 31 e, 33 s, 35 w, 37 n
    # d : 41 w, 43 g, 45 r

    def __init__(self, num, dora_value=0):
        if num not in TileConstant.TILE_NUM_LIST:
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
        return TileConstant.TYPE_LIST[int(self._num/10)]

    def __repr__(self) -> str:
        if self.num < 30:
            return str(self.num % 10)+self.type
        if self.num < 40:
            return TileConstant.WIND_LIST[int(self.num % 10/2)]
        return TileConstant.DRAGON_LIST[int(self.num % 10/2)]

    def __lt__(self, other):
        return self.num < other.num