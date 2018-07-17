from constant import TileConstant

class Tile:
    # m :  1 ~  9
    # p : 11 ~ 19
    # s : 21 ~ 29
    # w : 31 e, 33 s, 35 w, 37 n
    # d : 41 w, 43 g, 45 r

    @staticmethod
    def _is_valid(num):
        if 1 <= num <= 9:
            return True
        if 11 <= num <= 19:
            return True
        if 21 <= num <= 29:
            return True
        if num == 31 or num == 33 or num == 35 or num == 37:
            return True
        if num == 41 or num == 43 or num == 45:
            return True
        return False

    def __init__(self, num, dora_value=0):
        if not self._is_valid(num):
            raise NotImplemented
        self._num = num
        self._basic_dora_value=dora_value
        self._temp_dora_value=0

    @property
    def num(self):
        return self._num

    #property
    def dora_vaslue(self):
        return sesf._basic_dora_value + self._temp_dora_value

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