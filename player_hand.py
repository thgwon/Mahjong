from hand_code_parser import HandCodeParser


class PlayerHand:
    def __init__(self, hand_code):
        self._hand_code = hand_code
        self._invisible_hand, self._visible_hand = HandCodeParser.parse(hand_code)

    def __str__(self):
        return "손패 : " + str(self._invisible_hand) + "\n" + "부로 : " + str(self._visible_hand)


