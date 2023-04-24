# dfs
def dfs(y,x):
    global cnt
    used[y][x] = 1
    if building[y][x] == 1:
        cnt +=1

    for k in range(4):
        nx = x+dx[k]
        ny = y+dy[k]
        if nx < 0 or ny<0 or nx > n-1 or ny > n-1: continue
        if used[ny][nx] == 0 and building[ny][nx] ==1:
            dfs(ny,nx)


n = int(input())
building=[list(map(int, input())) for _ in range(n)]
used = [[0]*n for _ in range(n)]
result_cnt = []
cnt = 0
dy = [0, 0, 1, -1]
dx = [-1, 1, 0, 0]
for y in range(n):
    for x in range(n):
        if building[y][x] == 1 and used[y][x] == 0:
            dfs(y,x)
            result_cnt.append(cnt)
            cnt =0

result_cnt.sort()
print(len(result_cnt))
for i in range(len(result_cnt)):
    print(result_cnt[i])
