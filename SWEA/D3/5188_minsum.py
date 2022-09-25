# T= int(input())
# for t in range(T):
#     n=int(input())
#     arr=[list(map(int,input().split())) for _ in range(n)]
#     li=[[0]*n for _ in range(n)]
#     li[0][0]=arr[0][0]
#     for i in range(1,n):
#         li[0][i]=li[0][i-1]+arr[0][i]
#         li[i][0]=li[i-1][0]+arr[i][0]
#     for i in range(1,n):
#         for j in range(1,n):
#             li[i][j]=min(li[i-1][j],li[i][j-1])+arr[i][j]
#     print(f'#{t+1} {li[n-1][n-1]}')

def dfs(y,x,cnt):
    global Min
    if y==(n-1) and x==(n-1):
        if cnt<Min:
            Min=cnt
        return

    diry=[1,0]
    dirx=[0,1]
    for i in range(2):
        dy=y+diry[i]
        dx=x+dirx[i]
        if dy<0 or dx<0 or dy>n-1 or dx>n-1:continue
        if used[dy][dx]==1:continue
        used[dy][dx]=1
        dfs(dy,dx,cnt+arr[dy][dx])
        used[dy][dx]=0
T= int(input())
for t in range(T):
    n=int(input())
    arr=[list(map(int,input().split())) for _ in range(n)]
    used=[[0]*n for _ in range(n)]
    used[0][0]=1
    Min=9999
    dfs(0,0,arr[0][0])
    print(f'#{t+1} {Min}')
