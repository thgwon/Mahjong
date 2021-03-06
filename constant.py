class TileConstant:
    TYPES = ['만', '통', '삭', '풍', '원']
    WINDS = ['동', '남', '서', '북']
    DRAGONS = ['백', '발', '중']

    TILE_NUMS = [1, 2, 3, 4, 5, 6, 7, 8, 9,
                 11, 12, 13, 14, 15, 16, 17, 18, 19,
                 21, 22, 23, 24, 25, 26, 27, 28, 29,
                 31, 33, 35, 37,
                 41, 43, 45]

    TILE_STR_DICT = { 1: "1만",  2: "2만",  3: "3만",  4: "4만",  5: "5만",  6: "6만",  7: "7만",  8: "8만",  9: "9만",
                     11: "1통", 12: "2통", 13: "3통", 14: "4통", 15: "5통", 16: "6통", 17: "7통", 18: "8통", 19: "9통",
                     21: "1삭", 22: "2삭", 23: "3삭", 24: "4삭", 25: "5삭", 26: "6삭", 27: "7삭", 28: "8삭", 29: "9삭",
                     31: "동",  33: "남",  35: "서",  37: "북",  41: "백",  43: "발",  45: "중"}

    TILE_CODE_DICT = {'1m':  1, '2m':  2, '3m':  3, '4m':  4, '5m':  5, '6m':  6, '7m':  7, '8m':  8, '9m':  9,
                      '1p': 11, '2p': 12, '3p': 13, '4p': 14, '5p': 15, '6p': 16, '7p': 17, '8p': 18, '9p': 19,
                      '1s': 21, '2s': 22, '3s': 23, '4s': 24, '5s': 25, '6s': 26, '7s': 27, '8s': 28, '9s': 29,
                      '1z': 31, '2z': 33, '3z': 35, '4z': 37, '5z': 41, '6z': 43, '7z': 45}

    TERMINALS = [1, 9, 11, 19, 21, 29]
    HONORS = [31, 33, 35, 37, 41, 43, 45]
    GREENS = [22, 23, 24, 26, 28, 43]
    REVERSIBLES = [11, 12, 13, 14, 15, 18, 19, 22, 24, 25, 26, 28, 29, 41]


class BuroConstant:
    CHI_CODE = 'CH'
    PON_CODE = 'PO'
    BIG_MELDED_KAN_CODE = 'BK'
    SMALL_MELDED_KAN_CODE = 'SK'
    CONCEALED_KAN_CODE = 'CK'
    WHERE_LIST = ['상가', '대가', '하가']
    BURO_STRINGS = {CHI_CODE:'치',
                    PON_CODE:'퐁',
                    BIG_MELDED_KAN_CODE:'대명깡',
                    SMALL_MELDED_KAN_CODE:'소명깡',
                    CONCEALED_KAN_CODE:'안깡'}

class HandForPointCalcConstant:
    RON = 'RON'
    TSUMO = 'TSUMO'
    AGARI_TYPES = [RON, TSUMO]

    EAST = 'E'
    SOUTH = 'S'
    WEST = 'W'
    NORTH = 'N'
    WINDS = [EAST, SOUTH, WEST, NORTH]

    NO_RIICHI = 'NO'
    RIICHI = 'RI'
    DOUBLE_RIICHI = 'DR'
    OPEN_RIICHI = 'OR'
    RIICHI_TYPES = [NO_RIICHI, RIICHI, DOUBLE_RIICHI, OPEN_RIICHI]

    NO_SPECIAL = 'NO'
    ROBBING_QUAD_WIN = 'RQ'
    DEAD_WALL_WIN = 'DW'
    LAST_TILE_WIN = 'LT'
    FIRST_TURN_WIN = 'FT'
    SPECIAL_WINS = [NO_SPECIAL, ROBBING_QUAD_WIN, DEAD_WALL_WIN, LAST_TILE_WIN, FIRST_TURN_WIN]

class RuleConstant:
    FOUR_TILE_CHITOI = "ftc"