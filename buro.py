class Buro:
    def __init__(self, tile, base_fu):
        self._tile = None
        self._base_fu = None

    @property
    def fu(self):
        return self._base_fu * (2 if self._tile.is_terminal_and_honor else 1)


class Chi(Buro):
    # type : 0 -> a-2, a-1, a
    #        1 -> a-1, a, a+1
    #        2 -> a, a+1, a+2
    def __init__(self, tile, type):
        super.__init__(tile, 0)
        self._type = None
        self._fu = 0

class Pon(Buro):
    def __init__(self, tile, where):
        super.__init__(tile, 2)
        self._where = where

class BigMeldedKan(Buro):
    def __init__(self, tile, where):
        super.__init__(tile, 8)
        self._where = where

class SmallMeldedKan(Buro):
    def __init__(self, tile, where):
        super.__init__(tile, 8)
        self._where = where

class ConcealedKan(Buro):
    def __init__(self, tile):
        super.__init__(tile, 16)

