from collections import deque

def bfs(x,y):
    q=deque()
    q.append([x,y])
    dirx=[0,0,-1,1]
    diry=[-1,1,0,0]
    while q:
        x,y = q.popleft()
        for i in range(4):
            dx = dirx[i]+x
            dy = diry[i]+y
            if dx < 0 or dy<0 or dx>N-1 or dy>M-1: continue
            if used[dx][dy] == 0 and arr[dx][dy] == 1:
                used[dx][dy]=1
                q.append([dx,dy])

T=int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    arr = list([0] * M for _ in range(N))
    used = list([0] * M for _ in range(N))
    cnt = 0
    for _ in range(K):
        a,b = map(int, input().split(' '))
        arr[b][a]=1

    for y in range(M):
        for x in range(N):
            if arr[x][y] == 1 and used[x][y] == 0:
                bfs(x,y)
                cnt= cnt+1
    print(cnt)