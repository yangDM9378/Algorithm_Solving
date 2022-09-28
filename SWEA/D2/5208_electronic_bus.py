def dfs(level,cnt,dnl):
    global temp
    if cnt>=N-1:
        if level<temp:
            temp=level
        return
    for i in range(1,dnl+1):
        if level+1>temp:continue
        dfs(level+1,cnt+i,li[cnt+i])

T=int(input())
for t in range(T):
    arr=list(map(int,input().split()))
    N=arr.pop(0)
    li=[0]*999
    for k in range(len(arr)):
        li[k]=arr[k]
    temp=21e8
    dfs(0,0,li[0])
    print(f'#{t+1} {temp-1}')

