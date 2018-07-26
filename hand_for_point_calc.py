from player_hand import PlayerHand
from constant import HandForPointCalcConstant, TileConstant
from tile import Tile

class HandForPointCalc:
    def __init__(self, hand, agari_tile, agari_type, prevalent_wind, seat_wind,
                 dora_count=0, ipatsu=False,
                 riichi_type=HandForPointCalcConstant.NO_RIICHI,
                 special_win = HandForPointCalcConstant.NO_SPECIAL):
        self._hand = hand
        self._agari_tile = agari_tile
        self._agari_type = agari_type
        self._dora_count = dora_count
        self._prevalent_wind = prevalent_wind
        self._seat_wind = seat_wind
        self._riichi_type = riichi_type
        self._ipatsu = ipatsu
        self._special_win = special_win

        self._validate_params()

    def _validate_params(self):
        assert isinstance(self._hand, PlayerHand)
        assert isinstance(self._dora_count, int)
        assert isinstance(self._ipatsu, bool)
        assert isinstance(self._agari_tile, Tile)
        assert self._agari_type in HandForPointCalcConstant.AGARI_TYPES
        assert self._prevalent_wind in HandForPointCalcConstant.WINDS
        assert self._seat_wind in HandForPointCalcConstant.WINDS
        assert self._riichi_type in HandForPointCalcConstant.RIICHI_TYPES
        assert self._special_win in HandForPointCalcConstant.SPECIAL_WINS

        assert self._riichi_type == HandForPointCalcConstant.NO_RIICHI or self._hand.check_mensen()
        assert self._riichi_type == HandForPointCalcConstant.NO_RIICHI or not self._ipatsu
        assert self._special_win != HandForPointCalcConstant.ROBBING_QUAD_WIN or\
            self._agari_type == HandForPointCalcConstant.RON
        assert self._special_win != HandForPointCalcConstant.DEAD_WALL_WIN or\
            self._agari_type == HandForPointCalcConstant.TSUMO
        assert self._hand.count_tile(self._agari_tile) <= 3
        assert self._dora_count >= 0

    @property
    def hand(self):
        return self._hand

    @property
    def agari_tile(self):
        return self._agari_tile