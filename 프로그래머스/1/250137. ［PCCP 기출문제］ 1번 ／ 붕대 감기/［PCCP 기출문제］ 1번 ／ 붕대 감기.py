from collections import deque
def solution(bandage, health, attacks):
    answer = 0
    attack_chk = 0
    bandage_chk = 0
    max_health = health
    for stage_time in range(attacks[-1][0]+1):
        if attacks[attack_chk][0] == stage_time:
            health -= attacks[attack_chk][1]
            if health < 1 :
                return -1
            bandage_chk = 0
            attack_chk += 1
        else:
            bandage_chk += 1
            health = min(max_health, health+bandage[1])
            if bandage_chk == bandage[0]:
                health = min(max_health, health+bandage[2])
                bandage_chk = 0
    return health