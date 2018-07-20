from constant import RuleConstant


class Rule(dict):
    def __init__(self):
        self[RuleConstant.FOUR_TILE_CHITOI] = False