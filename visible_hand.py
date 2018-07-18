from buro import Buro


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
        return ' '.join([str(tile) for tile in self._buros])
