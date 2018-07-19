from buro import Buro, ConcealedKan

class VisibleHand:
    def __init__(self):
        self._buros = []

    @property
    def buro_num(self):
        return len(self._buros)

    def append(self, buro):
        assert isinstance(buro, Buro)
        self._buros.append(buro)

    def __str__(self):
        return ' / '.join([str(tile) for tile in self._buros])

    def check_mensen(self):
        for buro in self._buros:
            if not isinstance(buro, ConcealedKan):
                return False
        return True

    def count_tile(self, tile_num):
        return sum(buro.count_tile(tile_num) for buro in self._buros)
