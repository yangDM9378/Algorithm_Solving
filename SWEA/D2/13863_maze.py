T=int(input())

def dfs(arr,y,x):
    global flag

    if arr[y][x]=='3':
        flag=1
        return

    for i in range(4):
        diry=[0,0,-1,1]
        dirx=[1,-1,0,0]
        dy=y+diry[i]
        dx=x+dirx[i]
        if dy<0 or dx<0 or dy>N-1 or dx>N-1:continue
        if (arr[dy][dx]=='0' or arr[dy][dx]=='3') and used[dy][dx]==0:
            used[dy][dx]=1
            dfs(arr,dy, dx)
            used[dy][dx]=0

for t in range(1,T+1):
    N=int(input())
    arr=[list(input()) for _ in range(N)]
    used=[[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j]=='2':
                y=i
                x=j
    flag=0
    used[y][x]==1
    dfs(arr,y,x)
    print(f'#{t} {flag}')