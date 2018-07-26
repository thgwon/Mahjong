from player_hand import PlayerHand
from hand_complete_checker import HandCompleteChecker
from rule import Rule
from point_calculator import PointCalculator
from hand_for_point_calc import HandForPointCalc
from constant import HandForPointCalcConstant
from tile import Tile

def main():
    rule = Rule()
    hcc = HandCompleteChecker(rule)
    print("화료점 계산기")
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

        agari_tile_code = input("화료 패 코드 입력하세요: ")
        try:
            agari_tile = Tile(Tile.calc_tile_num(agari_tile_code))
        except:
            print("코드가 이상하다.")
            continue
        print(agari_tile)

        agari_type_num = input("론인가 쯔모인가: (0/1)")
        try:
           agari_type = HandForPointCalcConstant.AGARI_TYPES[int(agari_type_num)]
        except:
            print("코드가 이상하다.")
            continue
        print(agari_type)

        hand_pc = HandForPointCalc(hand, agari_tile, agari_type,
                          HandForPointCalcConstant.EAST, HandForPointCalcConstant.EAST)

        print("점수 :", PointCalculator(rule).calc_agari_status(hand_pc))


if __name__ == '__main__':
    main()

# 1m1m1m2m3m4m5m6m7m8m9m9m9m
# 2s3s4s6s6s8s8s:PO6z0:CH3s2s4s
# 5z:BK1z0:SK2z1:SK3z2:CK4z
# 1m1m3m3m5m5m7m7m9m9m1z1z5z
# 1m9m1p9p1s9s1z2z3z4z5z6z7z