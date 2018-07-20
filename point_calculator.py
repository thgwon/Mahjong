from hand_for_point_calc import HandForPointCalc
from hand_complete_checker import HandCompleteChecker
from tile import Tile
from player_hand import PlayerHand

class PointCalculator:
    def __init__(self, rule):
        self._rule = rule
        self._fu_calculator = None

    def calc_point(self, hand):
        assert isinstance(hand, HandForPointCalc)
        self._validate_agari(hand)
        return 0

    def _validate_agari(self, hand):
        assert isinstance(hand.hand, PlayerHand) and isinstance(hand.agari_tile, Tile)
        hcc = HandCompleteChecker(self._rule)
        hcc.check_waiting(hand.hand, hand.agari_tile.num)
