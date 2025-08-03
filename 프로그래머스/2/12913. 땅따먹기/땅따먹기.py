def solution(land):
    answer = 0
    dp_map = [[0]*4 for _ in land]
    for i in range(4):
        dp_map[0][i] = land[0][i]
    for depth in range(1, len(land)):
        for k in range(4):
            for idx in range(4):
                if k == idx: continue
                dp_map[depth][k] = max(dp_map[depth][k],dp_map[depth-1][idx] + land[depth][k])
    return max(dp_map[-1])
