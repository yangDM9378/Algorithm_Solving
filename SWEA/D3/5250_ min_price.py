def bfs(y,x):
    q=deque()
    q.append([y,x])

    while q:
        node=q.popleft()
        nowy,nowx= node[0],node[1]

        diry=[-1,1,0,0]
        dirx=[0,0,-1,1]
        for i in range(4):
            dy=nowy+diry[i]
            dx=nowx+dirx[i]
            if dy<0 or dy>N-1 or dx<0 or dx>N-1:continue

            d=arr[dy][dx]-arr[nowy][nowx]
            if d>0:
                temp=li[nowy][nowx]+d+1
            else:
                temp=li[nowy][nowx]+1

            if temp<li[dy][dx]:
                li[dy][dx]=temp
                q.append((dy,dx))


from collections import deque
T=int(input())
for t in range(T):
    N=int(input())
    arr=[list(map(int, input().split())) for _ in range(N)]
    li=[[21e8]*N for _ in range(N)]
    li[0][0]=0
    bfs(0,0)
    print(f'#{t+1} {li[N-1][N-1]}')


