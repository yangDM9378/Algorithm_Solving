def dfs(y, x, computers):
    global used
    used[y][x] = 1
    for dy in range(len(computers)):
        if computers[x][dy] == 1 and used[x][dy] == 0:
            used[x][dy] = 1
            dfs(x,dy,computers)

def solution(n, computers):
    global used
    answer = 0
    used = [[0] * n for _ in range(n)]
    for y in range(n):
        for x in range(n):
            if used[y][x] == 0 and computers[y][x] == 1:
                dfs(y, x, computers)
                answer += 1
    return answer