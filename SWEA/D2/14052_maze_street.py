def bfs(y,x,N):
    visited=[[0]*N for _ in range(N)]
    q=[]
    q.append((y,x))
    visited[y][x]=1
    while q:
        y,x=q.pop(0)
        if arr[y][x]==3:
            return visited[y][x]-2
        for i in range(4):
            diry=[0,1,0,-1]
            dirx=[1,0,-1,0]
            dy=y+diry[i]
            dx=x+dirx[i]
            if dy<0 or dy>N-1 or dx<0 or dx>N-1:continue
            if arr[dy][dx]!=1 and visited[dy][dx]==0:
                q.append((dy,dx))
                visited[dy][dx]=visited[y][x]+1
    return 0

T= int(input())
for t in range(T):
    N=int(input())
    arr=[list(map(int, input())) for _ in range(N)]

    sty=-1
    stx=-1

    for y in range(N):
        for x in range(N):
            if arr[y][x]==2:
                sty, stx=y,x
                break
    print(f'#{t+1} {bfs(sty,stx,N)}')