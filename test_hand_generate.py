from player_hand import PlayerHand
from hand_complete_checker import HandCompleteChecker

hcc = HandCompleteChecker()
hand1 = PlayerHand("1m1m1m2m3m4m5m6m7m8m9m9m9m")
print(hand1)

hand2 = PlayerHand("2s3s4s6s6s8s8s:PO6z0:CH3s2s4s")
print(hand2)

hand3 = PlayerHand("5z:BK1z0:SK2z1:SK3z2:CK4z")
print(hand3)

hand4 = PlayerHand("1m1m3m3m5m5m7m7m9m9m1z1z5z")
print(len(hcc.calculate_waiting(hand4)))

hand5 = PlayerHand("1m9m1p9p1s9s1z2z3z4z5z6z7z")
print(len(hcc.calculate_waiting(hand5)))