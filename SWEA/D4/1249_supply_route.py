def bfs(y,x):
    q=deque()
    q.append([y,x])
    while q:
        node=q.popleft()
        nowy,nowx=node[0], node[1]
        diry=[0,0,-1,1]
        dirx=[-1,1,0,0]
        for i in range(4):
            dy=nowy+diry[i]
            dx=nowx+dirx[i]
            if dy<0 or dx<0 or dy>N-1 or dx>N-1:continue
            if li[dy][dx]==-1:
                li[dy][dx]=int(arr[dy][dx])+li[nowy][nowx]
                q.append([dy,dx])
            else:
                if li[dy][dx] == min(li[dy][dx],int(arr[dy][dx])+li[nowy][nowx]): continue
                else:
                    li[dy][dx]=int(arr[dy][dx])+li[nowy][nowx]
                    q.append([dy, dx])

from collections import deque
T=int(input())
for t in range(T):
    N=int(input())
    arr=[list(input()) for _ in range(N)]
    li=[[-1]*N for _ in range(N)]
    li[0][0]=0
    bfs(0,0)
    print(f'#{t+1} {li[N-1][N-1]}')