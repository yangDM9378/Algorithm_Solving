# 시간초과
# def dfs(cnt):
#     global Min
#
#     if cnt>=B:
#         Min=min(Min,cnt)
#         return
#
#     for i in range(N):
#         if used[i]==1:continue
#         used[i]=1
#         dfs(cnt+arr[i])
#         used[i]=0
#
# T=int(input())
# for t in range(T):
#     N,B=map(int, input().split())
#     used=[0]*N
#     arr=list(map(int, input().split()))
#     Min=200001
#     dfs(0)
#     print(f'#{t+1} {Min-B}')

def dfs(i,cnt):
    global Min
    if i>N-1:
        if cnt >= B:
            Min = min(Min, cnt)
        return

    if cnt>=B:
        Min=min(Min,cnt)
        return
    dfs(i+1,cnt+arr[i])
    dfs(i+1,cnt)

T=int(input())
for t in range(T):
    N,B=map(int, input().split())
    used=[0]*N
    arr=list(map(int, input().split()))
    Min=200001
    dfs(0,0)
    print(f'#{t+1} {Min-B}')