T=int(input())
def dfs(now):
    global ssum
    global result
    if now==N:
        if result>ssum:
            result=ssum
        return

    if result <= ssum:
        return

    for i in range(N):
        if visited[i]==0:
            ssum+=arr[now][i]

            visited[i]=1
            dfs(now+1)
            visited[i]=0
            ssum-=arr[now][i]
    return result

for t in range(T):
    N = int(input())
    arr=[list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    ssum=0
    result=9999
    print(f'#{t+1} {dfs(0)}')

