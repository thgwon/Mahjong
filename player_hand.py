from tile import Tile
from buro import Buro

class PlayerHand:
    class InvisibleHand(list):
        def __init__(self):
            super.__init__()

        @property
        def tile_num(self):
            return len(super)

        def append(self, tile):
            assert isinstance(tile, Tile)
            super.append(tile)

    class VisibleHand(list):
        def __init__(self):
            super.__init__()

        @property
        def buro_num(self):
            return len(super)

        def append(self, buro):
            assert isinstance(buro, Buro)
            super.append(buro)

    def __init__(self):
        self._visible_hand = PlayerHand.VisibleHand()
        self._invisible_hand = PlayerHand.InvisibleHand()