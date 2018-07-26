from hand_for_point_calc import HandForPointCalc
from hand_complete_checker import HandCompleteChecker
from player_hand import PlayerHand
from agari_stat import AgariStatus
class PointCalculator:
    def __init__(self, rule):
        self._rule = rule

    def calc_agari_status(self, hand):
        assert isinstance(hand, HandForPointCalc)
        self._validate_agari(hand)
        agari_status = self._get_agari_status(hand)
        agari_status.sort()

        return agari_status[0]

    def _validate_agari(self, hand):
        assert isinstance(hand.hand, PlayerHand)
        hcc = HandCompleteChecker(self._rule)
        assert hcc.check_waiting(hand.hand, hand.agari_tile)

    def _get_agari_status(self, hand):
        agari_status = AgariStatus()
