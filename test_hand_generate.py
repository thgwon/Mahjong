from player_hand import PlayerHand
from hand_complete_checker import HandCompleteChecker

def main():
    hcc = HandCompleteChecker()
    print("대기패 계산기")
    while True:
        hand_code = input("손패 코드 입력하세요: (exit 입력으로 종료)")
        if hand_code == "exit":
            return
        try:
            hand = PlayerHand(hand_code)
        except:
            print("코드가 이상하다.")
            continue

        print(hand)
        waiting = hcc.calculate_waiting(hand)
        print("대기 :", ' '.join(map(str,waiting)))


if __name__ == '__main__':
    main()

# 1m1m1m2m3m4m5m6m7m8m9m9m9m
# 2s3s4s6s6s8s8s:PO6z0:CH3s2s4s
# 5z:BK1z0:SK2z1:SK3z2:CK4z
# 1m1m3m3m5m5m7m7m9m9m1z1z5z
# 1m9m1p9p1s9s1z2z3z4z5z6z7z