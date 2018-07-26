from hand_for_point_calc import HandForPointCalc
import copy


class AgariStatus(list):
    def __init__(self):
        super().__init__()
    def append(self, agari_stat):
        assert isinstance(agari_stat, AgariStat)
        super().append(agari_stat)