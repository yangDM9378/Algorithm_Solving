def dfs(level):
    global cnt
    global result
    if level==N:
        if cnt<result:
            result=cnt
        return

    if cnt > result:
        return

    for i in range(N):
        if li[i]==1:continue
        cnt+=arr[level][i]
        li[i]=1
        dfs(level+1)
        li[i]=0
        cnt-=arr[level][i]



T=int(input())
for t in range(T):
    N=int(input())
    arr=[list(map(int, input().split())) for _ in range(N)]
    cnt=0
    result=9999
    li=[0]*N
    dfs(0)
    print(f'#{t+1} {result}')