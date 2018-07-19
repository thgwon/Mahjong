class HandCompleteChecker:
    def __init__(self, four_tile_chitoi=False):
        self._four_tile_chitoi = four_tile_chitoi

    def check_tenpai(self, hand):
        return False

    def calculate_waiting(self, hand):
        return []

    def check_waiting(self, hand, tile):
        return self.check_normal_wating(hand, tile) or \
            self.check_chitoi_wating(hand, tile) or \
            self.check_koukusi_waiting(hand, tile)

    def check_normal_waiting(self, hand, tile):
        return False

    def check_chitoi_waiting(self, hand, tile):
        return False

    def check_koukusi_waiting(self, hand, tile):
        return False