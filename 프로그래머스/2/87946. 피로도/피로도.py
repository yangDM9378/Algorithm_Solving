def dfs(dungeons, k, cnt):
    global used
    max_cnt = cnt

    for i in range(len(dungeons)):
        if used[i] == 0 and k >= dungeons[i][0]:
            used[i] = 1
            result = dfs(dungeons, k - dungeons[i][1], cnt + 1)
            max_cnt = max(max_cnt, result)
            used[i] = 0
    
    return max_cnt

def solution(k, dungeons):
    global used
    used = [0] * len(dungeons)
    return dfs(dungeons, k, 0)
