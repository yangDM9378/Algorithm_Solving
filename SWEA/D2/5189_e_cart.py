def dfs(now):
    global ssum
    global Min
    global li
    if now==n-1:
        ssum=0
        for k in range(1, len(li)):
            ssum+=arr[li[k-1]][li[k]]
        ssum+=arr[li[len(li)-1]][0]
        if Min>ssum:
            Min=ssum
        return

    for i in range(1,n):
        if used[i]==1:continue
        li.append(i)
        used[i]=1
        dfs(now+1)
        used[i]=0
        li.pop()

T=int(input())
for t in range(T):
    n=int(input())
    li=[]
    li.append(0)
    arr=[list(map(int, input().split())) for _ in range(n)]
    used=[0]*n
    ssum=0
    Min=9999
    dfs(0)
    print(f'#{t+1} {Min}')