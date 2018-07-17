class Buro:
    def __init__(self, tile):
        self._tile = None

class Chi(Buro):
    # type : 0 -> a-2, a-1, a
    #        1 -> a-1, a, a+1
    #        2 -> a, a+1, a+2
    def __init__(self, tile, type):
        super.__init__(tile)
        self._type = None

class Pon(Buro):
    def __init__(self, tile, where):
        super.__init__(tile)
        self._where = where

class BigMeldedKan(Buro):
    def __init__(self, tile, where):
        super.__init__(tile)
        self._where = where

class SmallMeldedKan(Buro):
    def __init__(self, tile, where):
        super.__init__(tile)
        self._where = where

class ConcealedKan(Buro):
    def __init__(self, tile):
        super.__init__(tile)

