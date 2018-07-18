from tile import Tile


class InvisibleHand:
    def __init__(self):
        self._tiles = []

    @property
    def tile_num(self):
        return len(self._tiles)

    def append(self, tile):
        assert isinstance(tile, Tile)
        self._tiles.append(tile)

    def __str__(self):
        return ' '.join([str(tile) for tile in self._tiles])