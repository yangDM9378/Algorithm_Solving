from collections import deque

def bfs(y,x):
    q=deque()
    q.append([y,x])
    diry=[0,0,-1,1]
    dirx=[1,-1,0,0]
    while q:
        y,x = q.popleft()
        for i in range(4):
            dy=diry[i]+y
            dx=dirx[i]+x
            if dy<0 or dx<0 or dy>N-1 or dx>M-1:continue
            if arr[dy][dx] == 1:
                q.append([dy,dx])
                arr[dy][dx] = arr[y][x]+1
    return arr[N-1][M-1]



N,M = map(int, input().split(' '))
arr = [list(input()) for _ in range(N)]
for y in range(N):
    for x in range(M):
        arr[y][x]= int(arr[y][x])
used=list([0]*M for _ in range(N))
used[0][0]=1
print(bfs(0,0))