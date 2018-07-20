from

class PointCalculator:
    def __init__(self, rule=None):
        self._rule = {} if rule is None else rule
        self._fu_calculator = None

    def calc_point(self, self):